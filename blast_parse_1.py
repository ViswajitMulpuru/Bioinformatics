from Bio.Blast import NCBIXML
from Bio import SeqIO
import glob
import re

result = open("multi.xml", "r")
records = NCBIXML.parse(result)
for i, record in enumerate(records):
    #print (i+1, end=" ")
    #print (record.query)
    #print(dir(record))
    #print(record.hsps_no_gap)
    for align in record.alignments:
        #print("Iteration {}".format(i))
        #print(i+1)
        #print (align.hit_id)

        #print (align.hsps[0].sbjct_start)
        #print(i+1, align.hit_def)#, end=" ")
        x=str(align.hit_def)
        #print (align.hit_id)
        #print (align.hsps[0].sbjct_start)
        #print (align.hit_def)
        #print (record.alignments[0].hsps[0].query, end=" ")
        id=align.hit_id
        start=align.hsps[0].sbjct_start
        end=align.hsps[0].sbjct_end
        #id_split=id.split("|")
        #id_main=str(id_split[1])
        #print (start, end)
        organism=align.hit_def
        #print (organism)
        id_split=id.split("|")
        id_main=str(id_split[1])
        #print (start, end, id_main)
        i=i+1
        for seq_record in SeqIO.parse("./genomes/full.fasta", "fasta"):
                if id_main == seq_record.id:
                        sequence=str(seq_record.seq[start:end])
                        print ('>', id, organism, end="\n")
                        print(sequence)

"""
                        #print(seq_record.seq.complement())
                        print (str(sequence[0:3]))
                        if (str(sequence[0:3])== 'ATG' or str(sequence[0:3])== 'TTG' or str(sequence[0:3])== 'GTG' or str(sequence[0:3])== 'CTG'):
                                #print (str(sequence[0:3]))
                                #print (str(sequence[0:3])== 'ATG')
                                print ('>', id, organism, end="\n")
                                print(sequence)
                        elif (str(sequence[0:3])== 'TAC' or str(sequence[0:3])== 'AAC' or str(sequence[0:3])== 'CAC' or str(sequence[0:3])== 'GAC'):
                                sequence=seq_record.seq.complement()
                                print ('>', id, organism, end="\n")
                                print(sequence)
                        else:
                                sequence=seq_record.seq.reverse_complement()
                                if (str(sequence[0:3])== 'ATG' or str(sequence[0:3])== 'TTG' or str(sequence[0:3])== 'GTG' or str(sequence[0:3])== 'CTG'):
                                        print ('>', id, organism, end="\n")
                                        print(sequence)
                #else:
                        #print ("no match")
                #print ('>', id, organism, end="\n")
                #print(sequence)
"""

"""
for i, record in enumerate(records):
	for align in record.alignments:
		#print (align)
		id=record.alignments[i].hit_id
		print (id)
		i=i+1
		print (i)
"""

"""
		organism=record.alignments[0].hit_def
		start=record.alignments[i].hsps[i].sbjct_start
		end=record.alignments[i].hsps[i].sbjct_end
		id_split=id.split("|")
		id_main=str(id_split[1])
		print (start, end, id_main)
		i=i+1
"""
"""
		for seq_record in SeqIO.parse("./genomes/full.fasta", "fasta"):
			if id_main == seq_record.id:
				sequence=str(seq_record.seq[start:end])
				print ('>', id, organism, end="\n")
				#print(sequence)
			#else:
				#print ("no match")
		#print ('>', id, organism, end="\n")
		#print(sequence)
		j=j+1
"""
'''
for file in files:
	for seq_record in SeqIO.parse("p_putida.fasta", "fasta"):
		x=str(seq_record.seq[start:end])
	print ('>', id, end="\n")
	print(x)
'''
