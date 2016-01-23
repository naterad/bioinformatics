#input
#ATGCG
#GCATG
#CATGC
#AGGCA
#GGCAT

#output
#AGGCA -> GGCAT
#CATGC -> ATGCG
#GCATG -> CATGC
#GGCAT -> GCATG

import sys, itertools

dna = set()
with open(sys.argv[1]) as fh:
        #ints = fh.next().strip()
        #test2 = fh.next().strip()
        #test = fh.next().strip()
        for line in fh:
        	#print line
        	line = line.strip()
        	dna.add(line)
        #while fh.next()
        #	print fh.hasnext()
	#seq = fh.next().strip()
	#nex = fh.next().strip()
#print len(dna)
#nums = []
#nums = ints.split()
#k = int( nums[0] )
#d = int( nums[1] )

for d in dna:
        #print d
        for a in dna:
                if d != a:
                        if d[ 1 : 1 + len(d)-1] in a:
                                #print d[ 1 : 1 + 4 ]
                                print d + " -> " + a
