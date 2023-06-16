import difflib
from Bio import SeqIO
#b="MAAAAGSGGAGSGFLAGSASLAWAPPAGLAAAAWTAAGTCAPAAGAA"
i=0
#score=[[0]*(15) for z in range(15)]
score=[[0]*(1087) for z in range(1087)]
#print(score)
#for seq_record in SeqIO.parse("C:\\Users\\Administrator\\Desktop\\nox_seq_test.txt", "fasta"):
for seq_record in SeqIO.parse("C:\\Users\\Administrator\\Desktop\\nox_seq.txt", "fasta"):
    a=str(seq_record.seq)
    #print(i)
    j=0
    #for seq_record in SeqIO.parse("C:\\Users\\Administrator\\Desktop\\nox_seq_test.txt", "fasta"):
    for seq_record in SeqIO.parse("C:\\Users\\Administrator\\Desktop\\nox_seq.txt", "fasta"):
        #print (seq_record.seq)
        b=str(seq_record.seq)
        #a=str(b)
        #b=str(seq_record.seq)
        #print (a)
        #print(b)
        #seq=difflib.SequenceMatcher(a=a.lower(),b=b.lower())
        seq1=difflib.SequenceMatcher(None,a,b).ratio()
        seq2=round(seq1,2)
        #print (seq2)
        #seq=difflib.SequenceMatcher(a,b)
        #print(seq)
        #print(seq1)
        #d=seq.ratio()*100
        #print (d)
        #print(j)
        score[i][j] = seq2
        if score[i][j]>=0.5:
            if i!=j:    
                #print (i,j,score[i][j])
                print (a,b,score[i][j])
                #print(score[i][j])
        #print(i)
        #print(j)
        #print (score[i][j])
        j=j+1
    i=i+1
#print (score)
    

    #print ("**************")

"""
#%%
import matplotlib.pyplot as plt
plt.imshow(score, cmap='hot', interpolation='none')
#plt.show()
plt.savefig('C:\\Users\\Administrator\\Desktop\\heatmap.png')
"""
