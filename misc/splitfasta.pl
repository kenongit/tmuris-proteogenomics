#!/usr/bin/perl -w
#

use vars qw($opt_n $opt_s);   # do this if using strict
use Getopt::Std;    # you need this in order to use the module !
getopts('n:s:');

my $nchunks   = ( defined $opt_n ) ? $opt_n : 10;
my $chunksize = ( defined $opt_s ) ? $opt_s : 0;

foreach my $filename ( @ARGV ) {

	open(FILE,$filename) or die "problem with $filename \n";
	$nseqs=0;
	while ( <FILE> ) {
		next if /^\s*$/;
		if ( /^>\s*(\S.+)/ ) {
			$h = $1;
			$nseqs++;
		} else {
			s/\s*//g;
			chomp();
			$seq{$h} .= uc $_;
		}	
	}
	if ( defined $opt_n ) {
		$chunksize = 1 + int(($nseqs-1)/$nchunks);
	}
	print "spliting $nseqs into $nchunks chunks of size $chunksize\n";

	$count=0;
	$ccount=0;
	foreach my $s (sort keys %seq) {
	    if ( $ccount == 0 ) {
		$chunk++;
		close(OFILE) if ( $count );
		$ofilename = $filename . "_o$chunk.fa";
		print "$count $ccount $chunk file to open = $ofilename \n";
		open(OFILE,">$ofilename") or die "prob with $ofilename\n";
	    }
	    $count++;
	    $ccount++;
	    
	    print OFILE ">$s\n";
		fastaprint($seq{$s},100);

		$ccount = 0 if ( $ccount > $chunksize );
	}

}

sub fastaprint {
	my ($s,$l) = @_;
	for(my $pos=0; $pos< length $s; $pos+=$l) {
		print OFILE substr($s,$pos,$l),"\n";
	}
}
