#sample code to extract sequences with less than or equal to specific bases/aa from FASTA file along with the description. 
from Bio import SeqIO
my_record=[]
#for seq_record in SeqIO.parse("c:\\Users\\Administrator\\microbiome_code\\all_50_seq_A.txt", "fasta"):
#for seq_record in SeqIO.parse("out_proteins.faa", "fasta"):
for seq_record in SeqIO.parse("c:\\Users\\Administrator\\microbiome_code\\all_50_seq_B.txt", "fasta"):
    if len(seq_record)<=50:
        a=seq_record
        my_record.append(a)
        #print(seq_record)
        #print(seq_record.description)
        desc=seq_record.description
        desc1=desc.split(" ")
        print(desc1[0], desc1[1], desc1[2], desc1[3], desc1[4], end =" ")
        #print(seq_record.id, end =" ")
        #print(seq_record.seq)
        #print(seq_record.id, end =" ")
        print(seq_record.seq)
#SeqIO.write(my_record, "d:\\human_microbiome\\SRS01\\less_than_50aa.faa", "fasta")
#SeqIO.write(my_record, "less_than_50aa.faa", "fasta")
