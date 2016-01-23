#input
#GCGTGCCTGGTCA$

#output
#ACTGGCT$TGCGGC

import sys

with open( sys.argv[1]) as fh:
       	seq = fh.next().strip()


seqs = list()
for i in range(len(seq)):
	t1 = seq[:i]
	t2 = seq[i:]
	t3 = t2+t1
	seqs.append(t3)

seqs.sort()
final = ""
for l in seqs:
	final=final+ l[len(l)-1:]

print final
