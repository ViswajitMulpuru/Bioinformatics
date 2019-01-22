cd D:\test1591
$z=get-content .\ids.txt # input a file containing KEGG Entries. One entry in a line
For ($i=0; $i -lt $z.length; $i++) {
$x=$z[$i]
$webreq = Invoke-WebRequest "https://www.genome.jp/dbget-bin/www_bget?cpd:$x"
$webreq.Content >> .\htmlparseout123.txt
$webreq.links >> .\zzz1.txt
}
get-content .\zzz1.txt -ReadCount 1000 |
foreach { $_ -match 'outerHTML : <A href="https://pubchem' } >>.\zzz2.txt
get-content .\zzz2.txt -ReadCount 1000 |
foreach { $result = $_ -creplace '^[^\>]*\>', '' }
$result >> .\zzz3.txt # output file comtaining the PubChem IDs in the exact order of the input ids.txt file
