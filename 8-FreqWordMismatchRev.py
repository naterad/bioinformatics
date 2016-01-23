#input
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4 1

#output
#ATGT ACAT


import sys, itertools

def mutations(word, hamming_distance, charset='ATCG'):
    # this enumerates all the positions in word
    for indices in itertools.combinations( range( len( word ) ), hamming_distance ):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            mutation = list(word)
            for index, replacement in zip( indices, replacements ):
                mutation[ index ] = replacement
            yield "".join( mutation )

def get_reverse(word):
	result = ""
	for i in word:
		if i == "A":
			result+="T"
		elif i == "T":
                        result+="A"
		elif i == "C":
                        result+="G"
		elif i == "G":
                        result+="C"
	result = result[::-1]
	return result


with open(sys.argv[1]) as fh:
        seq = fh.next().strip()
  	ints = fh.next().strip()

nums = []
nums = ints.split()
k = int( nums[0] )
d = int( nums[1] )


#print " ".join(matches)

counts = dict()
for i in range( len(seq)-k+1):
	kmer = seq[ i : i + k]

	mutated_kmers = set()
	for mutated_kmer in mutations (kmer, d):
		mutated_kmers.add( mutated_kmer)
	for unique_mutated_kmer in mutated_kmers:
#		print unique_mutated_kmer

		unique_mutated_kmer_revcom = get_reverse(unique_mutated_kmer)

		if unique_mutated_kmer_revcom in counts:
			counts[ unique_mutated_kmer_revcom ] += 1
		else:
			counts[ unique_mutated_kmer_revcom] = 1

		if unique_mutated_kmer in counts:
			counts[ unique_mutated_kmer ] += 1
		else:
			counts[ unique_mutated_kmer ] = 1

highest_count = 0
for key, val in counts.iteritems():
	#print key, val
	if val > highest_count:
		highest_count = val

for key, val in counts.iteritems():
	if val == highest_count:
		print key
