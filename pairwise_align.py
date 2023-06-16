'''
from Bio import pairwise2
from Bio import SeqIO
seq1 = SeqIO.read("C:\\Users\\Administrator\\Desktop\\denv2.txt", "fasta")
seq2 = SeqIO.read("C:\\Users\\Administrator\\Downloads\\1R6R_A.fasta.txt", "fasta")
alignments = pairwise2.align.localxx(seq1.seq, seq2.seq)
print (alignments)
'''
"""
from Bio.Emboss.Applications import NeedleCommandline
needle_cline = NeedleCommandline(asequence="C:\\Users\\Administrator\\Desktop\\denv2.txt", bsequence="C:\\Users\\Administrator\\Downloads\\1R6R_A.fasta.txt", gapopen=10, gapextend=0.5, outfile="C:\\Users\\Administrator\\Downloads\\blast_t.txt")
print (needle_cline)
stdout, stderr = needle_cline()
print(stdout + stderr)
"""
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
seq1 = SeqIO.read("C:\\Users\\Administrator\\Downloads\\1R6R_A.fasta.txt", "fasta")
seq2 = SeqIO.read("C:\\Users\\Administrator\\Desktop\\denv2.txt", "fasta")
alignments = pairwise2.align.localxx(seq1.seq, seq2.seq)
print(len(alignments))
print(alignments[0])
#for a in pairwise2.align.localxx(seq1.seq, seq2.seq):
#    print(format_alignment(*a))
