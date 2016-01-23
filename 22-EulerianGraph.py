#input
#0 -> 2
#1 -> 3
#2 -> 1
#3 -> 0,4
#6 -> 3,7
#7 -> 8
#8 -> 9
#9 -> 6

#output
#6->7->8->9->6->3->0->2->1->3->4

import sys, itertools

def start_rec():
	c = s[s.keys()[0]]
	b = c[0]
	b = 3
	first = b
	# t = s[b]
	# t.remove(b)
	# s[b] = t
	rec(b)

def rec(b):
	#print b
	if b in s:
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

def find_last():
	for key, val in s.iteritems():
		for v in val:
			if v not in s:
				print "not found"
				print v
				t = s[key]
				t.remove(v)
				s[key] = t
				print key
				first = key
				rec(first)

def make_dict():
	for key, val in s.iteritems():
		a = list()
		count = 0
		for k, vv in s.iteritems():
			for v in vv:
				if v == key:
					count += 1
		a.append(len(val))
		a.append(count)
		t[key] = a
		# print "--------"
		# print key
		# print len(val)
		# print count
		if len(val) != count:
			#print key
			rec(key)


first = 0
dna = list()
order = list()
with open(sys.argv[1]) as fh:
        for line in fh:
        	line = line.strip()
        	dna.append(line)
s = dict()
t = dict()
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



for key in sorted(t.iterkeys()):
        val = s[key]
        val.sort()
        #print ""
        #print key + "->" + ",".join(val)

#find_last()
#start_rec()
make_dict()

order.reverse()


print "->".join(order )
