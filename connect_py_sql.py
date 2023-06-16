import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="",database="amp" )
cursor = connection.cursor()
amp_seq=[]
for p in open('c:\\Users\\Administrator\\microbiome_code\\only_amp_genes_all_with_sample_id_final_formated.txt','r'):
    #print(x)
    q=p.split(" ")
    #print(q[3])
    seq_desc=str(q[2])+str(q[3])+str(q[4])+str(q[5])+str(q[6])
    amp_seq.append(seq_desc)
    #print(amp_seq)
print (len(amp_seq))
print (amp_seq[-1])

#print(amp_seq)
i=0
for z in open('d:\\human_microbiome_merged\\all_50_seq.txt','r'):
    #print(x)
    y=z.split(" ")
    amp_str=(str(y[0])+str(y[1])+str(y[2])+str(y[3])+str(y[4]))
    #print(amp_str)
    #print(y[5])
    #print(y[0])
    if amp_str in amp_seq:
    #if y[0] in amp_seq:
        #print (y[0], y[2], y[4], y[5])
        #i+=1
        #print (i)
        #insert1 = "INSERT INTO seq(Gene_ID, Sequence) VALUES(\'"+y[0]+"\', \'"+y[1]+"\');"
        insert1 = "INSERT INTO seq(Gene_ID, Start, Stop, Sequence) VALUES(\'"+y[0]+"\', \'"+y[2]+"\', \'"+y[4]+"\', \'"+y[5]+"\');"
        print (insert1)
        cursor.execute(insert1)
        connection.commit()
connection.close()
