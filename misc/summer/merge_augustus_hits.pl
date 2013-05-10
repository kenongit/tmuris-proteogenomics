#!/usr/bin/perl
# Merge genes from a parsed DAT (arg_1) with scored PSMs (arg_2)

$a = shift;
$b = shift;

open(FH, $a) or die;

while(<FH>){
  chomp $_;  
  @tmp = split/\s+/, $_;
  $matches{$tmp[8]} = $tmp[10];
}close FH;





open(FH, $b) or die;
while(<FH>){
    chomp $_;
    @tmp =split/\t/, $_;
    if(exists $matches{$tmp[0]}){
      print $_."\t".$matches{$tmp[0]}."\n";
    }
}close FH;
