#input
#LEQN

#output
#0 113 114 128 129 227 242 242 257 355 356 370 371 484

import sys



with open(sys.argv[1]) as fh:
	aaChain = fh.next().strip()

map = { "G":"57",  "A":"71",  "S":"87",  "P":"97",
	"V":"99",  "T":"101", "C":"103", "I":"113",
	"L":"113", "N":"114", "D":"115", "K":"128",
	"Q":"128", "E":"129", "M":"131", "H":"137",
	"F":"147", "R":"156", "Y":"163", "W":"186",}

aaList = list()
aaLen = len(aaChain)
for k in range(1,aaLen):
	loopeptide = aaChain + aaChain[0:k-1]
	for x in range(0,len(loopeptide)-k+1):
		subPeptide = loopeptide[x:x+k]
		aaList.append(subPeptide)

l = list()
l.append(int(0))
aaList.append(aaChain)
for subPep in aaList:
	weight = int(0)
	for aa in subPep:
		weight += int(map[aa])
	l.append(weight)

l.sort()
for w in l:
	print w,
