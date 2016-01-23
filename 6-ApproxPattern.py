#input
#ATTCTGGA
#CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
#3

#output
#6 7 26 27 78

import sys

with open(sys.argv[1]) as fh:
	pattern = fh.next().strip()
	seq = fh.next().strip()
	misMatchesAllowed = int( fh.next().strip())

matches = []
for i in range(len(seq) - len(pattern)):
	misMatches = int(0)
	kmer = seq[i:i+len(pattern)]
	for j in range(len(pattern)):
		if kmer[j] != pattern[j]:
			misMatches += 1
	if misMatches <= misMatchesAllowed:
		matches.append(str(i))

print " ".join(matches)
