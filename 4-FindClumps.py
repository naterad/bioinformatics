#input
#CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
#5 75 4

#output
#CGACA GAAGA AATGT


import sys

with open( sys.argv[1]) as fh:
       	seq = fh.next().strip()
        ints = fh.next().strip()

nums = []
nums = ints.split()
k = int ( nums[0] )
L = int ( nums[1] )
t = int ( nums[2] )


clumps_set = set()
for j in range( len( seq )-L):
	counts = dict()
	for i in range(j,L+j):
		kmer = seq[ i : i +k ]
        	if kmer in counts:
        	        counts[ kmer ]+= 1
        	else:
        	        counts[ kmer ] = 1

        for key, val in counts.iteritems():
	       # print key, val
	        if val>=t:
			clumps_set.add( key )

print " ".join(clumps_set)
