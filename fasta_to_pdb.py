from Bio import SeqIO
import openbabel
"""
my_record=[]
#for seq_record in SeqIO.parse("d:\\human_microbiome\\SRS019068\\out_proteins.faa", "fasta"):
#for seq_record in SeqIO.parse("D:\\microbe_test\\fa_t.txt", "fasta"):
for seq_record in SeqIO.parse("/mnt/c/Users/Administrator/OneDrive/microbiome_code/amp_seq_no_X.txt", "fasta"):
    a=seq_record
    #print(a.seq)
    #print(a.id)
    #if len(seq_record)<=50:
    #    a=seq_record
    #    print(a.seq)
        #my_record.append(a)
seq=str(a.seq)
print(seq)
"""
#SeqIO.write(my_record, "d:\\human_microbiome\\SRS019068\\less_than_50aa.faa", "fasta")
#SeqIO.write(my_record, "less_than_50aa.faa", "fasta")
conv=openbabel.OBConversion()
#conv.OpenInAndOutFiles("/mnt/d/microbe_test/fa_t.txt","/mnt/d/microbe_test/test.pdb")
conv.SetInAndOutFormats("fasta","pbd")
mol=openbabel.OBMol()
conv.ReadFile(mol, "/mnt/d/microbe_test/fa_t.txt")
mol.AddHydrogens()

print (mol.NumAtoms())
print (mol.NumBonds())
print (mol.NumResidues())

x=str(conv.WriteFile(mol,'/mnt/d/microbe_test/test.pdb'))
print(x)
"""
conv.ReadString(mol, seq)
print(mol.NumAtoms())
#conv.WriteFile(mol, '/mnt/d/microbe_test/test.pdb')
#conv.Convert()
#print(mol)
mol.AddHydrogens()
print(mol.NumAtoms())
#conv.WriteFile(mol,'/home/invivis/test.pdb')
outMDL = conv.WriteString(mol)
print(outMDL)
print(str(outMDL))
"""
