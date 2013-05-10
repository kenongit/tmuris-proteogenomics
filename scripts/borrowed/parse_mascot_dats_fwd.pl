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
#    print "Mascotparser> working on file $filer  \n";
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
	    # $qexp{$1}=$2;
	} elsif( $ln =~ /^qmatch(\S+)=(\S+)/){
	    $snum=$1;
	    $snum.="\_$mgffile";
            $qmatch{$snum}=$2;
            # print "qmatch $snum = $2 \n";
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
                       # $spec=$qmatch2{$snum};
                        #$snum.="\_$mgffile";
                       # print "whats this $snum\n";
                       ## $qmatch{$snum}=$spec;
	} elsif ($ln =~ m/^q\d+\_p\d+\=\-.+/){
	#			print "no match for $ln ";
	} elsif (( $ln =~ /^q(\d+)\_p(\d+)\=(\d+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,([^\,]+)\,[^\;]+\;(.+)/)&&($7!~m/X/)){
			chomp $ln;
			$spectra = "$1" . "\_$mgffile";
                       # print "whats this $spectra";
                        $peprank = $2;
		#	print "ranks: $spectra $peprank\n";
			$pepkey = $spectra . "_" . $peprank;
	#		$missed_cleavages = $3;
	#		$peptide_mr = $4;
        #		$delta = $5;
	#		$ions_matched = $6;
			$aa=$7;
	#		$ions1_peaks = $8;
	#		$vmods = $9;
			$score = $10;
	
                         # $Peptide{sequence}{$pepkey} = $aa;
			if (  ! defined $qmatch{$spectra} ) {
				print "problem with $spectra for qmatch ? \n";
			}
                        $spec_num=$qmatch{$spectra};
                        $spec_num=~s/(\S+)\_\S+/$1/;
                        if  ( $qmatch{$spectra} < 1 ) {
				$identity = -10.0 * log(1.0/10.0)/log(10);
			} else {
				$identity = -10.0 * log(1.0/(1.0 * $qmatch{$spectra} ))/log(10);
#				print "sp> $spectra $qmatch{$spectra} $score => $identity \n";
			}
			$Peptide{identity}{$pepkey} = $identity;
			$score -= $identity if ( $diffscore );
			$Peptide{score}{$pepkey} = $score;
                        $prot=$11;  
	#		print "seq $aa score $score prot $prot \n";
			$expect = 0.05 * $qmatch{$spectra} * (10 ** (-$score/10.0));
                        @proteins = split /\,/, $prot;
			$proteins="@proteins";
                        $proteins=~s/\:\S+/,/g;
                        $proteins=~s/"//g;
                        $proteins=~s/\s+//g;
                        #print "here $aa,$score,$proteins\n";
                        $direction = "rev";
			#$direction = "rev" if ( $ln =~ /REV_/ );
                        my @prots=split(/,/,$proteins);
                          foreach my $p (@prots){
                          	
                            if ($p=~m/[0-9]+\_[0-9]+/){
                              $direction = "for" if ($p !~ /REV_/ );

                           }
                          }
                        if ( $peprank <= $maxpeprank && $printpeps ) {
				#print "pep$peprank> spectra $spectra\t$score\t$identity\t$aa\t$direction\n";
#				printf "pep%2.2d> spec %6d score %7.4f thrsh %4d %-50s %s\n",
#						$peprank,$spectra,$score,$identity,$aa,$direction;
				my $s = sprintf "pep> %d sp %6s sc %7.4f  id %4d %-50s %s %s",
						$peprank,$spectra,$score,$identity,$aa,$direction,$proteins;
			      if ( $score >= $ionscore_threshold && $expect <= $ionexpect_threshold) {
				   $Sequence_hits{$aa}++;
				   $pephits++;
				   $Peplist{$pephits} = $s;
				   $PepScore{$pephits} = $score;
			           $PepDir{$pephits} = $direction;
			           #print "$direction\n";
                               }
			}
	}
    }
    close(INF);
}
#exit(1);
#
# sort scores
#
my @sortpeps = sort by_pepscore ( keys %PepScore );
my $tp = 0;
my $fp = 0;
my $tat = 0;
my $qval = 0.0;
my $gygi_fpos;
my $gygi_tp = 0;
my $gygi_fdr;
my $gygi_qval = 0.0;
my $status = "PASS";
my $fdr;
my $fdrold;
my $allhits;
my $fpos;
foreach my $spep ( @sortpeps ) {
    my $info=$Peplist{$spep};
    $allhits++;
    $tat++ if ( $PepDir{$spep} eq "for" );
    $fp++ if ( $PepDir{$spep} eq "for" );
    $gygi_fpos= 2 * $fp;
    $tp = $tat - $fp;
    $gygi_tp= $allhits - $gygi_fpos;
    $fdr=1;
    #$fdr = $fp / ($tp + $fp);
    $qval = $fdr if ( $fdr > $qval);
    $gygi_fdr = $gygi_fpos / ($gygi_tp + $gygi_fpos);
    $gygi_qval = $gygi_fdr if ($gygi_fdr > $gygi_qval);
    $info.="\t$qval\t$gygi_qval";
    print "$info\n";
    #print "psm:$spep score:$PepScore{$spep} tot:$allhits tgt:$tat decoy:$fp fdr:$fdr q:$qval gygi_fdr:$gygi_fdr gygi_qval:$gygi_qval dir:$PepDir{$spep}\n";
}
sub by_pepscore{ $PepScore{$b} <=> $PepScore{$a} }
