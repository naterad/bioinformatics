#input
#5
#CAATCCAAC

#output
#AATCC
#ATCCA
#CAATC
#CCAAC
#TCCAA

import sys, itertools

with open(sys.argv[1]) as fh:
        k_t= fh.next().strip()
        seq = fh.next().strip()

k = int( k_t );

#print k
#print seq
s = list()
for i in range( len(seq)-k+1):
        kmer = seq[ i : i + k]
        #print kmer
        s.append(kmer)

s.sort()
for a in s:
	print a
