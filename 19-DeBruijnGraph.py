#input
#4
#AAGATTCTCTAC

#output
#AAG -> AGA
#AGA -> GAT
#ATT -> TTC
#CTA -> TAC
#CTC -> TCT
#GAT -> ATT
#TCT -> CTA,CTC
#TTC -> TCT


import sys, itertools

with open(sys.argv[1]) as fh:
        k_t= fh.next().strip()
        seq = fh.next().strip()

k = int( k_t );

#print k
#print seq
l = list()
s = dict()
for i in range( len(seq)-k+1):
        kmer = seq[ i : i + k-1]
        next_kmer = seq[ i+1 : i+1 +k-1]
        #print kmer
        #print next_kmer +" (n)"
        if kmer in s:
        	c = s[kmer]
        	c.append(next_kmer)
        	s[kmer] = c
        else:
       		#s[ kmer ] += 1
       		c = list()
       		c.append(next_kmer)
       		s[kmer] = c

#s.sort()
# for a in s:
# 	print a
#for key in sorted(s.iterkeys()):
    #print "%s: %s" % (key, s[key])

for key in sorted(s.iterkeys()):
	val = s[key]
	val.sort()
	#print ""
	print key + "->" + ",".join(val)
	#count = 0
	#for v in val:
	#	print
		# if count != 0:
		# 	print ",",
		# print v,
		# count += 1
