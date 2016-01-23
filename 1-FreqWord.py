#input
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4

#output
#CATG GCAT

import sys

with open( sys.argv[1] ) as fh:
	seq = fh.next().strip()
	k = int( fh.next().strip())

print seq
print k

highest_count = 0
counts = dict()

for i in range( len( seq )):
	print seq[ i : i + k ]
	kmer = seq[ i : i +k ]
	if kmer in counts:
		counts[ kmer ]+= 1
	else:
		counts[ kmer ] = 1

	if counts[ kmer ] > highest_count:
		highest_count = counts[ kmer ]

print highest_count

highest_freq_kmers = []
for key, val in counts.iteritems():
	print key, val
	if val==highest_count:
		highest_freq_kmers.append( key )


print " ".join(sorted ( highest_freq_kmers ))
