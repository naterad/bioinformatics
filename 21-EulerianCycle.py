#input
#0 -> 3
#1 -> 0
#2 -> 1,6
#3 -> 2
#4 -> 2
#5 -> 4
#6 -> 5,8
#7 -> 9
#8 -> 7
#9 -> 6

#output
#6->8->7->9->6->5->4->2->1->0->3->2->6

import sys, itertools

def start_rec():
	c = s[s.keys()[0]]
	b = c[0]
	first = b
	# t = s[b]
	# t.remove(b)
	# s[b] = t
	rec(b)

def rec(b):
	#print b
	l = s[b]
	#print l

	while(len(l)>0):
		c = l[0]
		if c != first:
			t = s[b]
			t.remove(c)
			s[b] = t
			rec(c)
	#print b
	order.append(b)

first = 0
dna = list()
order = list()
with open(sys.argv[1]) as fh:
        for line in fh:
        	line = line.strip()
        	dna.append(line)
s = dict()
for a in dna:
	#print a
	parts =[]
	parts = a.split()
	#print len(parts)
	parts[0]
	#print len(parts[2])
	nums = parts[2]
	nums = nums.replace(',',' ')
	c = nums.split()

	l = list()
	for b in c:
		l.append(b)
	s[parts[0]] = l



for key in sorted(s.iterkeys()):
        val = s[key]
        val.sort()
        #print ""
        #print key + "->" + ",".join(val)

start_rec()

order.reverse()


print "->".join(order )
