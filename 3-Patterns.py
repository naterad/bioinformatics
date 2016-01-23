#input
#ATAT
#GATATATGCATATACTT

#output
#1 3 9

import sys

with open( sys.argv[1]) as fh:
	seq = fh.next().strip()
	gen = fh.next().strip()

nums = []

for i in range( len( gen )):
	if gen.find(seq,i)!=-1:
		if str(gen.find(seq,i)) not in nums:
			nums.append(str(gen.find(seq,i)))

print " ".join(sorted (nums))
