#input
#MEANLY
#PENALTY

#output
#15
#EANL-Y
#ENALTY

#using
#  A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
#A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
#C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
#D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
#E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
#F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
#G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
#H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
#I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
#K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
#L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
#M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
#N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
#P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
#Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
#R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
#S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
#T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
#V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2

import sys, itertools

def get_alignment_dict():
    with open("pam.txt") as fh:
            first_row = fh.readline().strip().split()
            lines = fh.readlines()
    #print first_row
    value_dict = {}
    for line in lines:
            values = line.strip().split()
            line_dict = {}
            amino_acid = values[0]
            for i in range(1, len(values)):
                    line_dict[ first_row[i-1] ] = values[i]
            value_dict[amino_acid] = line_dict
    return value_dict

a_dict = get_alignment_dict()
# for key,value in a_dict.iteritems():
#     print key, value
with open(sys.argv[1]) as fh:
    pleasantly = fh.next().strip()
    meanly = fh.next().strip()

# pleasantly="#"+pleasantly
# meanly="#"+meanly
#print pleasantly
#print meanly

values = dict()
transitions = dict()
phash = 0
mhash = 0
pcount=0
mcount=0
for p in range(len(pleasantly)+1):
    key = str(pcount)+"_0"
    values[key]=phash
    transitions[key]="vertical"
    pcount+=1
for m in range(len(meanly)+1):
    key = "0_"+str(mcount)
    values[key]=mhash
    transitions[key]="horizontal"
    mcount+=1

start_value = 0
start_pos = "0_0"
start_p = 0
start_m = 0
mcount=1
indel = (-5)
for m in meanly:
    pcount=1


    for p in pleasantly:
        #print a_dict[p]['M']
        #print str(pcount)+","+str(mcount)

        best = "diagonal"
        highest = values[str(pcount-1)+"_"+str(mcount-1)] + int(a_dict[p][m])

        if len(meanly)>= mcount:
            second = values[str(pcount)+"_"+str(mcount-1)] + indel
            # if second == highest:
            #     print "duplicate second"
            #     print str(mcount)+","+str(pcount)
            if second >= highest:
                highest = second
                best = "horizontal"
        if len(pleasantly)>= pcount:
            third = values[str(pcount-1)+"_"+str(mcount)] + indel
            # if third == highest:
            #     print "duplicate third"
            #     print str(mcount)+","+str(pcount)
            if third >= highest:
                highest = third
                best = "vertical"
        if highest <= 0:
            highest = 0
            best = "done"
        key = str(pcount)+"_"+str(mcount)
        values[key] = highest
        transitions[key] = best
        if highest > start_value:
            #print highest
            start_pos = key
            start_value = highest
            start_p = pcount
            start_m = mcount
        #print highest
        #print best
        pcount+=1
    mcount+=1

# for key, val in sorted(values.iteritems()):
#     print key, val
#
# print start_pos
# print start_value


p_final = ""
m_final = ""
# key = str(len(pleasantly))+"_"+str(len(meanly))
key = start_pos
print values[key]

# p = len(pleasantly)
# m = len(meanly)
p = start_p
m = start_m
while p!=0 or m!=0:
    key = str(p)+"_"+str(m)
    if transitions[key] == "diagonal":
        p_final = pleasantly[p-1]+p_final
        m_final = meanly[m-1]+m_final
        #print pleasantly[p-1], meanly[m-1]
        #findPath(p-1,m-1)
        p-=1
        m-=1
    elif transitions[key] == "horizontal":
        #print "-", meanly[m-1]
        p_final = "-"+p_final
        m_final = meanly[m-1]+m_final
        #findPath(p,m-1)
        m-=1
    elif transitions[key] == "vertical":
        #print pleasantly[p-1], "-"
        p_final = pleasantly[p-1]+p_final
        m_final = "-"+m_final
        #findPath(p-1,m)
        p-=1
    elif transitions[key] == "done":
        p=0
        m=0



print p_final
print m_final
