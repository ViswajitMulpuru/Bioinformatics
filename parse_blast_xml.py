from Bio.Blast import NCBIXML
import re

result = open("blast_results.xml", "r")
#result = open("blast_result_1.xml", "r")
records = NCBIXML.parse(result)
char1 = '['
char2 = ']'
print("Sequence S.No. Genus         ")
for i, record in enumerate(records):
    #print (i+1, end=" ")
    #print (record.query)
    #print(dir(record))
    #print(record.hsps_no_gap)
    for align in record.alignments:
        #print("Iteration {}".format(i))
        #print(i+1)
        #print(align.hit_id)
        #print(i+1, align.hit_def)#, end=" ")
        x=str(align.hit_def)
        print (record.alignments[0].hsps[0].query, end=" ")
        #print (dir((record.alignments[0].hsps[0])))
        #y=str(align.title)
        #y=str(align.hsps)
        #print(dir(align.hsps))
        #print (y)
        print (i+1, x[x.find(char1)+1 : x.find(char2)])
        #print(i, align.title)
        break
