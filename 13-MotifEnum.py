#input
#3 1
#ATTTGGC
#TGCCTTA
#CGGTATC
#GAAAATT

#output
#ATA ATT GTT TTT


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

dna = set()
with open(sys.argv[1]) as fh:
        ints = fh.next().strip()
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
nums = []
nums = ints.split()
k = int( nums[0] )
d = int( nums[1] )


#print seq
#print nex


final = set()
first = True
for a in dna:
	#print d
	temp = set()
	counts = dict()
	seq = a
	for i in range( len(seq)-k+1):

		kmer = seq[ i : i + k]

		mutated_kmers = set()
		for mutated_kmer in mutations (kmer, d):
			mutated_kmers.add( mutated_kmer)
		for unique_mutated_kmer in mutated_kmers:
			#print unique_mutated_kmer

			unique_mutated_kmer_revcom = get_reverse(unique_mutated_kmer)
			#print "  "+unique_mutated_kmer_revcom
			temp.add(unique_mutated_kmer)
			#temp.add(unique_mutated_kmer_revcom)


		#if unique_mutated_kmer_revcom in counts:
		#	counts[ unique_mutated_kmer_revcom ] += 1
		#else:
		#	counts[ unique_mutated_kmer_revcom] = 1

		#if unique_mutated_kmer in counts:
		#	counts[ unique_mutated_kmer ] += 1
		#else:
		#	counts[ unique_mutated_kmer ] = 1

	if first == True:
		#print "first"
		final = temp
	else:
		#print "not first"
		temp2 = set()
		for c in final:
			if c in temp:
				temp2.add(c)
		final.clear()
		temp.clear()
		#print len(final)
		#print len(temp)
		final = temp2
	first = False

for b in final:
	print b

#highest_count = 0
for key, val in counts.iteritems():
	print key, val
#	if val > highest_count:
#		highest_count = val

#for key, val in counts.iteritems():
#	if val == highest_count:
#		print key
