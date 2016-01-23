#input
#AAAACCCGGT

#output
#ACCGGGTTTT

import sys

with open( sys.argv[1] ) as fh:
	seq = fh.next().strip()

result = ""

for i in seq:
	if i == "A":
		result+="T"
	elif i == "T":
		result+="A"
	elif i == "C":
		result+="G"
	elif i == "G":
		result+="C"

result = result[::-1]

print result
