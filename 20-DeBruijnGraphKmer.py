#input
#GAGG
#CAGG
#GGGG
#GGGA
#CAGG
#AGGG
#GGAG

#output
#AGG -> GGG
#CAG -> AGG,AGG
#GAG -> AGG
#GGA -> GAG
#GGG -> GGA,GGG

import sys, itertools

dna = list()
with open(sys.argv[1]) as fh:
        #ints = fh.next().strip()
        #test2 = fh.next().strip()
        #test = fh.next().strip()
        for line in fh:
        	#print line
        	line = line.strip()
        	dna.append(line)
        #while fh.next()
        #	print fh.hasnext()
	#seq = fh.next().strip()
	#nex = fh.next().strip()
#print len(dna)
#nums = []
#nums = ints.split()
#k = int( nums[0] )
#d = int( nums[1] )
s = dict()
for d in dna:
        #print d
        #print d[0:0+len(d)-1]
        first = d[0:0+len(d)-1]
        first_two = d[0:0+len(d)-2]
        #print d[ 1 : 1 + len(d)-1]
        second = d[ 1 : 1 + len(d)-1]
        #print d[ 2 : 2 + len(d)-1]
        # for a in dna:
        #         if d != a:
        if first in s:
                c = s[first]
                c.append(second)
                s[first] = c
        else:
                c = list()
                c.append(second)
                s[first] = c

for key in sorted(s.iterkeys()):
        val = s[key]
        val.sort()
        #print ""
        print key + "->" + ",".join(val)
