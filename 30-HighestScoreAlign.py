#input
#PLEASANTLY
#MEANLY

#output
#8
#PLEASANTLY
#-MEA--N-LY

#using
#   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
#A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
#C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
#D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
#E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
#F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
#G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
#H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
#I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
#K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
#L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
#M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
#N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
#P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
#Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
#R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
#S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
#T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
#V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
#W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
#Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7

import sys, itertools

def get_alignment_dict():
    with open("blosum.txt") as fh:
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
    phash-=5
    pcount+=1
for m in range(len(meanly)+1):
    key = "0_"+str(mcount)
    values[key]=mhash
    transitions[key]="horizontal"
    mhash-=5
    mcount+=1

mcount=1
indel = (-5)
for m in meanly:
    pcount=1


    for p in pleasantly:
        #print a_dict[p]['M']
        #print str(pcount)+","+str(mcount)
        highest = 0
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

        key = str(pcount)+"_"+str(mcount)
        values[key] = highest
        transitions[key] = best
        #print highest
        #print best
        pcount+=1
    mcount+=1




# for key, val in sorted(values.iteritems()):
#     print key, val
p_final = ""
m_final = ""
key = str(len(pleasantly))+"_"+str(len(meanly))
print values[key]

# def findPath(p,m):
#     #print str(p)+","+str(m)
#     key = str(p)+"_"+str(m)
#     global p_final
#     global m_final
#     if p!=0 or m!=0:
#         #print transitions[key]
#         if transitions[key] == "diagonal":
#             p_final = pleasantly[p-1]+p_final
#             m_final = meanly[m-1]+m_final
#             #print pleasantly[p-1], meanly[m-1]
#             findPath(p-1,m-1)
#         elif transitions[key] == "horizontal":
#             #print "-", meanly[m-1]
#             p_final = "-"+p_final
#             m_final = meanly[m-1]+m_final
#             findPath(p,m-1)
#         elif transitions[key] == "vertical":
#             #print pleasantly[p-1], "-"
#             p_final = pleasantly[p-1]+p_final
#             m_final = "-"+m_final
#             findPath(p-1,m)

#findPath(len(pleasantly), len(meanly))
p = len(pleasantly)
m = len(meanly)
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



print p_final
print m_final
