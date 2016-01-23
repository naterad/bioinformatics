#input
#PAWHEAE
#HEAGAWGHEE

#output
#1
#HEAE
#HEAG

import sys, itertools

with open(sys.argv[1]) as fh:
    side = fh.next().strip() #pleasantly
    top = fh.next().strip() #meanly

values = dict()
transitions = dict()
shash = 0
thash = 0
scount=0
tcount=0
for p in range(len(side)+1):
    key = str(scount)+"_0"
    values[key]=shash
    transitions[key]="vertical"
    scount+=1
for m in range(len(top)+1):
    key = "0_"+str(tcount)
    values[key]=thash
    transitions[key]="horizontal"
    tcount+=1

tcount=1
indel = (-2)
for t in top:
    scount=1


    for s in side:
        #print a_dict[p]['M']
        #print str(pcount)+","+str(mcount)
        highest = 0
        best = "diagonal"
        if s==t:
            highest = values[str(scount-1)+"_"+str(tcount-1)] + 1
        else:
            highest = values[str(scount-1)+"_"+str(tcount-1)] + indel
        # highest = values[str(scount-1)+"_"+str(tcount-1)] + 1

        if len(top)>= tcount:
            second = values[str(scount)+"_"+str(tcount-1)] + indel
            # if second == highest:
            #     print "duplicate second"
            #     print str(mcount)+","+str(pcount)
            if second >= highest:
                highest = second
                best = "horizontal"
        if len(side)>= scount:
            third = values[str(scount-1)+"_"+str(tcount)] + indel
            # if third == highest:
            #     print "duplicate third"
            #     print str(mcount)+","+str(pcount)
            if third >= highest:
                highest = third
                best = "vertical"

        key = str(scount)+"_"+str(tcount)
        values[key] = highest
        transitions[key] = best
        #print highest
        #print best
        scount+=1
    tcount+=1



n = 0
high = 0
best = ""
bestPart = "first"
while n < len(side):
    key = str(n)+"_"+str(len(top))
    # print key
    # print values[key]
    if values[key] >= high:
        high = values[key]
        best = n
    n+=1
n = 0
while n < len(top):
    key = str(len(side))+"_"+str(n)
    if values[key] >= high:
        high = values[key]
        best = n
        bestPart = "second"
    n+=1
print high
#print best
# for key, val in sorted(values.iteritems()):
#     print key, val
p_final = ""
m_final = ""

if bestPart == "first":
    p = best
    m = len(top)
else:
    p = len(side)
    m = best
#while p!=0 or m!=0:
length = 0
while length < best:
    key = str(p)+"_"+str(m)
    if transitions[key] == "diagonal":
        p_final = side[p-1]+p_final
        m_final = top[m-1]+m_final
        p-=1
        m-=1
        length+=1
    elif transitions[key] == "horizontal":
        p_final = "-"+p_final
        m_final = top[m-1]+m_final
        m-=1
        if bestPart == "second":
            length+=1
    elif transitions[key] == "vertical":
        p_final = side[p-1]+p_final
        m_final = "-"+m_final
        p-=1
        if bestPart == "first":
            length+=1
    elif transitions[key] == "done":
        p=0
        m=0


print p_final
print m_final
