#input
#4
#CTTA
#ACCA
#TACC
#GGCT
#GCTT
#TTAC

#output
#GGCTTACCA

import sys, itertools

s = list()
with open(sys.argv[1]) as fh:
	num = fh.next().strip()
	dna = fh.next().strip()
	for line in fh:
		line = line.strip()
		s.append(line)
n = int( num )
changed = True
temp = list()
temp = s
while changed:
	changed = False

	s = temp
	for a in s:
		#print "--------"
		#print a
		first_part = a[0:0 +n-1]
		second_part = a[1:1 +n-1]
		if second_part in dna[0:0+n-1]:
			dna = a[0:0+1] + dna
			#print "second"
			temp.remove(a)
			changed = True
		elif first_part in dna[len(dna)-len(first_part):len(dna)-len(first_part)+n-1]:
			#print "first"
			#print a[n-1:]
			dna = dna + a[n-1:]
			temp.remove(a)
			changed = True

print dna
