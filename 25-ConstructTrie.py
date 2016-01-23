#input
#ATAGA
#ATC
#GAT

#output
#0->1:A
#1->2:T
#2->3:A
#3->4:G
#4->5:A
#2->6:C
#0->7:G
#7->8:A
#8->9:T

import sys

class Node:
	def __init__(self, nuc):
		self.nucleotide = nuc
		self.children = list()
		self.preNum = int(0)

	def getNuc(self):
		return self.nucleotide

	def getChildren(self):
		return self.children

	def setPreNum(self, num):
		self.preNum = num

	def getPreNum(self):
		return self.preNum

	def setChild(self, newNode):
		self.children.append(newNode)

	def hasNode(self, char):
		hasNode = False
		for i in self.children:
			if i.getNuc() == char:
				hasNode = True
		return hasNode

	def getChild(self, char):
		for i in self.children:
			if i.getNuc() == char:
				return i



def preorderTraversal(root):
	if root.getChildren() > 0:
		for x in root.getChildren():
			print str(root.getPreNum())+"->"+str(x.getPreNum())+":"+x.getNuc()
			preorderTraversal(x)



with open(sys.argv[1]) as fh:
	patterns = list()
	for line in fh:
		patterns.append(line.strip())

root = Node("R")
currentPreNum = int(1)
for pattern in patterns:
	refNode = root
	for char in pattern:
		if refNode.hasNode(char) == True:
			refNode = refNode.getChild(char)
		else:
			newNode = Node(char)
			newNode.setPreNum(currentPreNum)
			currentPreNum += 1
			refNode.setChild(newNode)
			refNode = refNode.getChild(char)



preorderTraversal(root)
