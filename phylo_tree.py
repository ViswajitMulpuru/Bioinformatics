from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
with open("output.aln","r") as aln:
  alignment = AlignIO.read(aln,"clustal")

from Bio.Phylo.TreeConstruction import DistanceCalculator 
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
print(distance_matrix)

from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor = DistanceTreeConstructor(calculator)
tree = constructor.build_tree(alignment)
tree.rooted = True
print(tree)

import matplotlib
import matplotlib.pyplot as plt
fig = Phylo.draw(tree)
#fig.savefig("cladogram.png")

fig = plt.figure(figsize=(13, 20), dpi=100)
matplotlib.rc('font', size=12) 
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10)
#tree.ladderize()
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes)

Phylo.write(tree, "tree.xml", "phyloxml")

tree = Phylo.read("tree.xml", "phyloxml")
#tree.ladderize()
Phylo.draw_ascii(tree)
