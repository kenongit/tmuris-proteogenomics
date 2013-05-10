#!/usr/bin/perl -w
##
##  Simon's mascot .dat file parser
##
##
#use strict;

$|++;

use vars qw($opt_i $opt_s $opt_b $opt_r $opt_z $opt_q $opt_d $opt_p $opt_e $opt_n $opt_m);
use Getopt::Std;
#
# options variables
#
getopts('i:s:r:bqzde:pn:m:');
my $ionscore_threshold  = ( defined $opt_i ) ? $opt_i : 0.0;
my $ionexpect_threshold  = ( defined $opt_e ) ? $opt_e : 0.05;
my $min_pep_rank = ( defined $opt_r ) ? $opt_r : 5;
my $fdrthreshold = ( defined $opt_s ) ? $opt_s : 0.05;
my $require_boldred = ( defined $opt_b ) ? 1 : 0;
my $diffscore = ( defined $opt_d ) ? 1 : 0;
my $ensembl = ( defined $opt_n ) ? $opt_n : "NULL";
my $summary = ( defined $opt_z ) ? 1 : 0;
my $quiet = ( defined $opt_q ) ? 1 : 0;
my $printpeps = ( defined $opt_p ) ? 1 : 0;
my $maxpeprank = ( defined $opt_m ) ? $opt_m : 0;

( @ARGV > 0 ) or die("not enough arguments - you must supply at least a filename ");


my %Peplist;
my %PepScore;
my %PepDir;
my $pephits=0;

foreach $filer ( @ARGV ) {
    open(INF, $filer) || die "Couldn't open file1. $!\n";
    %Sequence_hits = ();
	
    $mgffile="unknown";
    print "Mascotparser> working on file $filer  \n";
#	print "\n" unless ( $quiet);
    while ( $ln = <INF> ) {
	chop($ln);
	if ( $ln =~ m/^queries=(\d+)/){
	    chomp $ln;
	    $noofpeptides=$1;
	    if ( ! $quiet ) {
				print "File: $filer $mgffile\t";
				print "Queries: $noofpeptides\t";
				print "Db: $DB \t";
				print "Cleavage Enzyme: $CLE \t";
				print "Charge: $CHARGE \t";
				print "Allowed_Missed_Cleavages: $PFA \t";
				print "Fixed Mods: $MODS \t";
				print "Variable Mods: $IT_MODS \t";
				print "Instrmnt: $INSTRUMENT \n";
	    }
	} elsif($ln=~/^qexp(\d+)=(.+)\,/){
	    $qexp{$1}=$2;
	} elsif( $ln =~ /^qmatch(\S+)=(\S+)/){
	    $qmatch{$1}=$2;
	    #print "qmatch $1 = $2 \n";
	} elsif ($ln=~m/^PFA\=(.+)/){
			$PFA=$1;
	} elsif ($ln =~ m/^INSTRUMENT\=(.+)/){
			$INSTRUMENT=$1;
	} elsif ($ln =~ m/^DB\=(.+)/){
			$DB=$1;
	} elsif ($ln =~ m/^MODS\=(.+)/){
			$MODS=$1;
	} elsif ($ln =~ m/^CLE\=(.+)/){
			$CLE=$1;
	} elsif ($ln =~ m/^CHARGE\=(.+)/){
			$CHARGE=$1;
	} elsif ($ln =~ m/^IT_MODS\=(.+)/){
			$IT_MODS=$1;
	} elsif ($ln =~ m/^FILE\=[A-Z]\:.+\\(.+)/){
			$mgffile=$1;
	} elsif ($ln =~ m/^q\d+\_p\d+\=\-.+/){
	#			print "no match for $ln ";
	} elsif ( $ln =~ /^q(\d+)\_p(\d+)\=(\d+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,[^\;]+\;(.+)/){
			chomp $ln;
			$spectra = $1;
			$peprank = $2;
			$pepkey = $spectra . "_" . $peprank;
	#		$missed_cleavages = $3;
	#		$peptide_mr = $4;
        #		$delta = $5;
	#		$ions_matched = $6;
			$aa=$7;
	#		$ions1_peaks = $8;
	#		$vmods = $9;
			$score = $10;
			$Peptide{sequence}{$pepkey} = $aa;
			if (  ! defined $qmatch{$spectra} ) {
				print "problem with $spectra for qmatch ? \n";
			}
			if  ( $qmatch{$spectra} < 1 ) {
				$identity = -10.0 * log(1.0/10.0)/log(10);
			} else {
				$identity = -10.0 * log(1.0/(1.0 * $qmatch{$spectra} ))/log(10);
#				print "sp> $spectra $qmatch{$spectra} $score => $identity \n";
			}
			$Peptide{identity}{$pepkey} = $identity;
			$score -= $identity if ( $diffscore );
			$Peptide{score}{$pepkey} = $score;
			$prot = $11;

	#		print "seq $aa score $score prot $prot \n";
			$expect = 0.05 * $qmatch{$spectra} * (10 ** (-$score/10.0));
			@proteins = split /\,/, $prot;
			
			$direction = "for";
			$direction = "rev" if ( $ln =~ /REV_/ );
			if ( $peprank <= $maxpeprank && $printpeps ) {
				#print "pep$peprank> spectra $spectra\t$score\t$identity\t$aa\t$direction\n";
#				printf "pep%2.2d> spec %6d score %7.4f thrsh %4d %-50s %s\n",
#						$peprank,$spectra,$score,$identity,$aa,$direction;
				my $s = sprintf "pep> sp %6d sc %7.4f  id %4d %-50s %s",
						$spectra,$score,$identity,$aa,$direction;
			      if ( $score >= $ionscore_threshold && $expect <= $ionexpect_threshold) {
				   $Sequence_hits{$aa}++;
				   $pephits++;
				   $Peplist{$pephits} = $s;
				   $PepScore{$pephits} = $score;
			           $PepDir{$pephits} = $direction;
			      }
			}
	}
    }
    close(INF);

}

#
# sort scores
#
my @sortpeps = sort by_pepscore ( keys %PepScore );
my $tp = 0;
my $fp = 0;
my $tat = 0;			  
my $qvalue = 0.0; 	  
my $status = "PASS";			  
foreach my $spep ( @sortpeps ) {
    $allhits++;
    $tat++ if ( $PepDir{$spep} eq "for" );
    $fp++ if ( $PepDir{$spep} eq "rev" );
    $tp = $tat - $fp;
    $fdr  = $fp / ($tp + $fp);
    $fdrold = 2*$fp / ( $tp+$fp);
    $qvalue = $fdr if ( $fdr > $qvalue);
    $status = "FAIL" if ( $qvalue > $fdrthreshold );
    printf "%s   %5d %5d %5d   %6.3f  %6.3f  %s\n", $Peplist{$spep}, $allhits, $tp, $fp, $fdr, $qvalue, $status;
}
    

sub by_pepscore{ $PepScore{$b} <=> $PepScore{$a} }

