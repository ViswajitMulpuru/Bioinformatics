import numpy as np
import math
atno=[]
aa=[]
cox=[]
coy=[]
coz=[]
coa=[]
diffmat=[]
diff=[]
for line in open('C:\\Users\\Admin\\Desktop\\sample.pdb'):
    if line.startswith('ATOM'):
       x=line.split()
       if x[2]=='CA':
           y=x
           atno.append(int(y[1]))
           aa.append(y[3])
           cor_ca=y[6:9]
           cox.append(float(cor_ca[0]))
           coy.append(float(cor_ca[1]))
           coz.append(float(cor_ca[2]))

for atno1,cx1,cy1,cz1 in zip(atno,cox,coy,coz):
    for atno2,cx2,cy2,cz2 in zip(atno,cox,coy,coz):
        diff.append(math.sqrt(abs((cx2-cx1)**2+(cy2-cy1)**2+(cz2-cz1)**2)))

i=0
j=0
d=0
diffmat = np.zeros(shape=(len(atno),len(atno)))

while (i<len(atno)):
    j=0
    while (j<len(atno)):
        diffmat[i][j]=abs(diff[d])
        j=j+1
        d=d+1
    i=i+1
#print (diffmat)
map = diffmat < 8.0
np.savetxt('D:\\maptest.txt', diffmat, delimiter=" ") 
np.savetxt('D:\\adjmattest.txt', map, delimiter=" ") 

import pylab
pylab.matshow(diffmat)
pylab.colorbar()
pylab.show()

pylab.hot() 
pylab.imshow(map)
pylab.show()

import collections
adjmat = np.genfromtxt("D:\\adjmattest.txt",delimiter=" ")
a=np.reshape(adjmat,(len(atno),len(atno)))
graph = collections.defaultdict(list)
edges = set()

for i, v in enumerate(a, 1):
    for j, u in enumerate(v, 1):
        if u != 0 and frozenset([i, j]) not in edges:
            edges.add(frozenset([i, j]))
            graph[i].append(j)

start, dfs = [1], []
while start:
    pos = start.pop()
    if pos in dfs:
        continue
    dfs.append(pos)
    for x in graph[pos]:
        start.append(x)
print (dfs)

#BFS
start=1
vis, tovis = set([start]), collections.deque([start])
while tovis:
    p = tovis.popleft()
    print(p)
    for x in graph[p]:
        if x not in vis:
            vis.add(x)
            tovis.append(x)
