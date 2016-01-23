#input
#CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG

#output
#53 97


import sys

with open(sys.argv[1]) as fh:
	seq = fh.next().strip()

minimum = []
min_value = 0
prefix = 0
for i in range(len(seq)):
	if prefix < min_value:
		min_value = prefix
		minimum = []
		minimum.append(i)
	elif prefix == min_value:
		minimum.append(i)
	if (seq[i] == "C"):
		prefix = prefix - 1
	elif (seq[i] == "G"):
		prefix = prefix + 1

for i in minimum:
	print i
