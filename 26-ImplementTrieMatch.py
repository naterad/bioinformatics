#input
#AATCGGGTTCAATCGGGGT
#ATCG
#GGGT

#output
#1 4 11 15

import sys

with open(sys.argv[1]) as fh:
	text = fh.next().strip()
	patterns = list()
	for line in fh:
		patterns.append(line.strip())


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

total = list()
for p in patterns:
	positions = list(find_all(text, p))
	for pos in positions:
		total.append(pos)

total.sort()

for t in total:
	print t
