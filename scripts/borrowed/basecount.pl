#!/opt/local/bin/perl -w

# Author and contact info: David Hummel at hummel@pw.usda.gov
# Created: 10/16/00
# This perl script works on sequence files in fasta format.
# It counts the number of bases per clone and creates
# a new file with a table listing clone name and number
# of bases followed by total number of bases, total
# number of clones, and average number of bases per clone
#At command line type basecount.pl your_fasta_filename.fasta

$totalclones = 0;
$totalbases = 0;
$basesperclone = 0;
print "What is your fasta file name?:\n";
$infile = <STDIN>;
chomp ($infile);
$outfile = "$infile.out";
print ("Output file will be called $outfile\n");
if (-e $outfile) {die "$outfile already exists\!\n";}
open (INFILE, "$infile") || die ("can't open $infile: $!");
open (OUTFILE, ">$outfile") || die ("can't open $outfile: $!");
chomp ($line = <INFILE>);
while (defined ($line)) {
	if ($line =~ />/) {
		$totalclones ++;
		$line =~ /\w*\.\w*/;
		$clone = $&;
		chomp ($line = <INFILE>);
		while ($line !~ />/ && defined ($line)) { # base count loop
			$baseline = ($line =~ tr/AGCTN//);
			$basecount += $baseline;
			chomp ($line = <INFILE>);
		}
		select OUTFILE;
		write;
		$totalbases += $basecount;
		$basecount = 0;
	} else {die "Are you sure this is a fasta file?\n";}
}
$basesperclone = $totalbases / $totalclones;
$~ = "OUTFILE_BOTTOM"; # change format for OUTFILE
write;
close (INFILE) || die ("can't close $infile: $!");
close (OUTFILE) || die ("can't close $outfile: $!");				
print STDOUT ("All done\!");

# functions

# formats

format OUTFILE_TOP =
FASTAFILE: @<<<<<<<<<<<<<<<<<<<<         PAGE:  @<<
           $infile,                             $%

CLONE                                    BASES
============================             =========
.

format OUTFILE = 
@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<         @<<<<<
$clone,                                  $basecount
.

format OUTFILE_BOTTOM = 
============================             =========

                         TOTAL BASES:    @<<<<<<<<
                                         $totalbases
                        TOTAL CLONES:    @<<<<<<<<
                                         $totalclones
                    AVG. BASES/CLONE:    @<<<<<<<<
                                         $basesperclone
.
