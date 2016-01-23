#input
#TTCCTAACG$A

#output
#TACATCACGT$

import sys, itertools

with open( sys.argv[1]) as fh:
       	seq = fh.next().strip()
build = ""
def findPath(n, b):
	global build
	temp = first_right[n]
	build = build+temp[:1]
	if first_right[n]!='$1' or b:
		b=False
		pos = last_right.index(first_right[n])
		findPath(pos,b)

	return build


last_right = list()
first_right = list()
last = dict()
first_let = list()
for i in range(len(seq)):
	t = seq[i:i+1]
	first_let.append(t)

	if t in last:
		last[ t ] += 1
		last_right.append(t+str(last[t]))
	else:
		last[ t ] = 1
		last_right.append(t+str(1))

first_let.sort()
first = dict()
for f in first_let:
	if f in first:
		first[ f ] += 1
		first_right.append(f+str(first[f]))
	else:
		first[ f ] = 1
		first_right.append(f+str(1))

# for i in last_right:
# 	print i
# print "--------"
# for i in first_right:
# 	print i

final = findPath(0, True)
print final[1:]
