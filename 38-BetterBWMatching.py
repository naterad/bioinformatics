#input
#GGCGCCGC$TAGTCACACACGCCGTA
#ACC CCG CAG

#output
#1 2 1

__author__ = 'masaki'

import sys, itertools

oo = sys.maxint / 2

class Node:
    def __init__( self, start, end ):
        self.start = start
        self.end = end
        self.edges = {} # key: single character, value: pointer to node
        self.link = 0

    def edge_length( self, position ):
        return min( self.end, position + 1 ) - self.start

    def get_edges( self ):
        return self.edges

    def set_start( self, start ):
        self.start = start

    def get_start( self ):
        return self.start

    def get_end( self ):
        return self.end

    def set_end( self, end ):
        self.end = end

    def put_edge( self, key, val ):
        self.edges[ key ] = val

    def set_link( self, node ):
        self.link = node

    def get_link( self ):
        return self.link

    def get_edge( self, key ):
        if key in self.edges:
            return self.edges[ key ]
        else:
            return None

    def str_val( self ):
        string = "start: " + str( self.start ) + " end: " + str( self.end ) + " edges: " + str( self.edges )
        return string

    def increment_start( self, val ):
        self.start += val


class SuffixTree:
    def __init__( self, t_len ):
        self.cur_node = 0
        self.nodes_added = 0
        self.nodes = [ Node( 0, oo ) ] * ( 2 * t_len + 2 )
        self.text = ""
        self.root = self.new_node( -1, -1 )
        self.pos = -1
        self.need_link = 0
        self.r = 0 # the remainder of suffixes to add

        self.active_node = self.root
        self.active_length = 0
        self.active_edge = 0

    def add_char( self, c ):
        self.text += c
        self.pos += 1

        self.need_link = -1
        self.r += 1

        # while there are suffixes to be added
        while self.r > 0:
            # set the active edge
            # if the active edge is 0, set it to the current position
            if self.active_length == 0:
                self.active_edge = self.pos
            # if active_edge is in active_nodes list of edges
            if self.get_active_edge() not in self.nodes[self.active_node].get_edges(): # self.active_edge is equivalent to self.get_active_edge()
                # the dege doesn't exist, create a new leaf node
                leaf = self.new_node(self.pos, oo)
                # add the leaf node as a child node and use the active_edge as the key for the edge
                self.nodes[self.active_node].put_edge(self.get_active_edge(), leaf)
                # check to see if you need to add a suffix link to the active node
                self.add_suffix_link(self.active_node)
            # else
            else:
                # the edge does exist
                # set nex = the node to walk down
                nex = self.nodes[self.active_node].get_edge(self.get_active_edge())
                # walk_down nex
                if self.walk_down(nex):
                    continue
                # if the current character is the same as the character as pos active_length
                # in the node nex
                if self.text[self.nodes[nex].get_start() + self.active_length] == c:
                    # it is, so we increment the active length
                    self.active_length += 1
                    # we add a suffix link to the active node
                    self.add_suffix_link(self.active_node)

                    # no longer need to continue as the current string is subsumed in the
                    # the current node, so we break out of the while loop
                    break

                # if the current character is not subsumed within the current node,
                # this means that we must split a node
                # create a new node called 'split' where:
                #   start = nex's start
                #   end = nex's start + the active_length
                split = self.new_node(self.nodes[nex].get_start(), self.nodes[nex].get_start() + self.active_length)

                # add split as an edge in active_node where the key is the active_edge
                self.nodes[self.active_node].put_edge(self.get_active_edge(), split)

                # createa  new leaf, node( current_position, #)
                leaf = self.new_node(self.pos, oo)

                # add leaf as an edge to the node split with c as the key
                self.nodes[split].put_edge(c, leaf)

                # change the start position of nex by incrementing it by active_length
                self.nodes[nex].increment_start(self.active_length)

                # add nex as an edge to split using the character referred to by
                # the new start position of nex
                self.nodes[split].put_edge(self.text[self.nodes[nex].get_start()], nex)

                # add a suffix link
                self.add_suffix_link(split)

            # decrement remainder because we've added a suffix
            self.r -= 1

            # if the active node is root and the active_length is > 0
            if self.active_node == self.root and self.active_length > 0:
                # decrement the active_length
                self.active_length -= 1

                # set active_edge to the current position - the number of suffixes to add + 1
                self.active_edge = self.pos - self.r + 1

            # else
            else:
                # set the active node to the node pointed to by the active_node's link if it has a link
                self.active_node = self.nodes[self.active_node].get_link() if self.nodes[self.active_node].get_link() > 0 else self.root
                # if it doesn't have a link, set it to root

    def walk_down( self, nex ):
        if self.active_length >= self.nodes[ nex ].edge_length( self.pos ):
            self.active_edge += self.nodes[ nex ].edge_length( self.pos )
            self.active_length -= self.nodes[ nex ].edge_length( self.pos )
            self.active_node = nex
            return True
        return False

    def in_depth_traverse( self, node, count, sa ):
        if len(node.edges) == 0:
            sa.append( node.start - count )
            return node.start - count
        count += node.end - node.start
        for n in sorted(node.edges):
            child = node.edges[n]
            self.in_depth_traverse(self.nodes[ child ], count, sa)

    def get_suffix_array( self, sa ):
        self.in_depth_traverse( self.nodes[ self.root ], 0, sa )
        return sa

    def get_active_edge( self ):
        return self.text[ self.active_edge ]

    def new_node( self, start, end ):
        self.cur_node += 1
        self.nodes[ self.cur_node ] = Node( start, end )
        self.nodes_added += 1
        return self.cur_node

    def add_suffix_link( self, node ):
        if self.need_link > 0:
            self.nodes[ self.need_link ].set_link( node )
        self.need_link = node

    def edge_string( self, node ):
        start = self.nodes[ node ].get_start()
        end = min( self.pos + 1, self.nodes[ node ].get_end() )
        return text[ start : end ]

    def print_tree(self ):
        self.print_edges( self.root )

    def print_graphviz_tree( self ):
        print "digraph {"
        print "\trankdir = LR;"
        print "\tedge [arrowsize=0.4,fontsize=10]"
        print "\tnode1 [label=\"\",style=filled,fillcolor=lightgrey,shape=circle,width=.1,height=.1];"
        print "//------leaves------"
        self.print_gv_leaves( self.root )
        print "//------internal nodes------"
        self.print_gv_internal_nodes( self.root )
        print "//------edges------"
        self.print_gv_edges( self.root )
        print "//------suffix links------"
        #self.print_gv_suffix_links( self.root )
        print "}"

    def print_edges( self, x ):
        for key, child in self.nodes[ x ].get_edges().iteritems():
            print self.edge_string( child )
            self.print_edges( child )

    """def inorderTraversal( self, x ):
        for key, child in self.nodes[ x ].get_edges().iteritems():
            print child
            self.inorderTraversal( child )"""

    def print_gv_internal_nodes( self, x ):
        if x != self.root and len( self.nodes[ x ].get_edges() ) > 0:
            print "\tnode" + str( x ) + " [label=\"\",style=filled,fillcolor=lightgrey,shape=circle,width=.07,height=.07]"
        for key, child in self.nodes[ x ].get_edges().iteritems():
            self.print_gv_internal_nodes( child )

    def print_gv_suffix_links( self, x ):
        if self.nodes[ x ].get_link() > 0:
            print "\tnode" + str( x ) + " -> node" + str( self.nodes[ x ].get_link() ) + " [label=\"\",weight=1,style=dotted]"
        for key, child in self.nodes[ x ].get_edges().iteritems():
            self.print_gv_suffix_links( child )

    def print_gv_edges( self, x ):
        for key, child in self.nodes[ x ].get_edges().iteritems():
            print "\tnode" + str( x ) + " -> node" + str( child ) + " [label=\"" + self.edge_string( child ) + "\",weight=3]"
            self.print_gv_edges( child )

    def print_gv_leaves( self, x ):
        if len( self.nodes[ x ].get_edges() ) == 0:
            print "\tnode" + str( x ) + " [label=\"\",shape=point]"
        else:
            for key, child in self.nodes[ x ].get_edges().iteritems():
                self.print_gv_leaves( child )

def genFirstBWT(sa, seq):
    firstBWT = []
    for i in sa:
        firstBWT.append(seq[i])
    return firstBWT

def genBWT(sa, seq):
    BWT = []
    for i in sa:
        BWT.append(seq[i - 1])
    return BWT

def genFirstToLast(firstBWT, BWT):
    firstToLast = []
    bpIndexes = dict()
    bpIndexes["$"] = 0
    bpIndexes["A"] = firstBWT.index("A")
    bpIndexes["C"] = firstBWT.index("C")
    bpIndexes["G"] = firstBWT.index("G")
    bpIndexes["T"] = firstBWT.index("T")
    for i in BWT:
        firstToLast.append(bpIndexes[i])
        bpIndexes[i] += 1
    return firstToLast

def getUpperRange(char, list):
    for i in reversed(range(len(list))):
        if list[i] == char:
            return i

def getLowerRange(char, list):
    for i in range(len(list)):
        if list[i] == char:
            return i

def getIndexesInRange(char, BWT, firstToLast, lowerRange, upperRange):
    indexesInBWT = []
    indexesInFirstToLast = []
    for i in xrange(lowerRange, upperRange + 1):
        if BWT[i] == char:
            indexesInBWT.append(firstToLast[i])
    return indexesInBWT

def getLowestIndex(list):
    if len(list) == 0:
        return
    lowestValue = list[0]
    for i in list:
        if i < lowestValue:
            lowestValue = i
    return lowestValue

def getHighestIndex(list):
    if len(list) == 0:
        return
    highestValue = list[0]
    for i in list:
        if i > highestValue:
            highestValue = i
    return highestValue

def findSeq(query, sa, firstBWT, BWT, firstToLast):
    occurences = []
    lowerRange = getLowerRange(query[-1], firstBWT)
    upperRange = getUpperRange(query[-1], firstBWT)
    for char in reversed(query[:-1]):
        indexesOfNextChar = getIndexesInRange(char, BWT, firstToLast, lowerRange, upperRange)
        if len(indexesOfNextChar) == 0:
            return None
        lowerRange = getLowestIndex(indexesOfNextChar)
        upperRange = getHighestIndex(indexesOfNextChar)
    occurences.extend(sa[indexesOfNextChar[0]:indexesOfNextChar[-1] + 1])
    return occurences

with open( sys.argv[ 1 ] ) as fh:
    BWT = fh.next().strip()
    #seq = fh.next().strip()
    #seq += "$"
    qLine = fh.next().strip()
    queries = qLine.split()

genome = BWT

first_column = sorted(genome)

prevMap = {}

for i in range(len(genome)):
    if first_column[i] not in prevMap:
        prevMap[first_column[i]] = []
    prevMap[first_column[i]].append((i, genome[i]))

answer = "$"
occurance = 0

while len(answer) < len(genome):
    index,letter = prevMap[answer[0]][occurance]
    answer = letter + answer
    occurance = genome[0:int(index)].count(letter)

try:
    file = open("results_overrite.txt", "w")
except:
    print("Failed to write")
    sys.exit(0)

#file.write(answer)
seq = answer

tree = SuffixTree( len( seq ) )
for char in seq:
    tree.add_char( char )

#if len( sys.argv ) > 2:
#    if sys.argv[ 2 ] == "gv":
#        tree.print_graphviz_tree()
#else:
    #tree.print_tree()

sa = []
tree.get_suffix_array(sa)
firstBWT = genFirstBWT(sa, seq)
BWT = genBWT(sa, seq)
firstToLast = genFirstToLast(firstBWT, BWT)

occurences = []

for query in queries:
    #print query
    num = 0
    o = findSeq(query, sa, firstBWT, BWT, firstToLast)
    if o != None:
        #occurences.extend(o)
        num = len(o)
        #print num
    occurences.append(num)

for i in occurences:
    print i,
#print sa
#print firstBWT
#print BWT
#print firstToLast
