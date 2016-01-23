#input
#ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
#5
#0.2 0.2 0.3 0.2 0.3
#0.4 0.3 0.1 0.5 0.1
#0.3 0.3 0.5 0.2 0.4
#0.1 0.2 0.1 0.1 0.2

#output
#CCGAG

import sys, itertools


def get_prob(word):
        total = 0.0
        c = 0
        for i in word:
                if i == "A":
                        total = total + float(prob[0][c])
                elif i == "C":
                        total = total + float(prob[1][c])
                elif i == "G":
                        total = total + float(prob[2][c])
                elif i == "T":
                        total = total + float(prob[3][c])
                c = c + 1
        return total

dna = set()
with open(sys.argv[1]) as fh:
        seq = fh.next().strip()
        print seq
        k = fh.next().strip()
        k = int( k )
        prob = []
        count =0;
        for line in fh:
        	line = line.strip()
        	print line
        	#dna.add(line)
                nums = []
                nums = line.split()
                prob.append(nums)
                count = count + 1

highest = 0.0
best = ""
for i in range( len(seq)-k+1):
        kmer = seq[ i : i + k]

        if get_prob(kmer) > highest:
                highest = get_prob(kmer)
                best = kmer
                print get_prob(kmer)
                print kmer

print best
