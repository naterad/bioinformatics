#input
#ATG
#ATG
#TGT
#TGG
#CAT
#GGA
#GAT
#AGA

#output
#AGA ATG ATG CAT GAT TGGA TGT

import sys

kmers = []
with open( sys.argv[ 1 ] ) as fh:
    for line in fh:
        kmers.append( line.strip() )

g = dict()
counts = dict()
edge_count = 0

for kmer in kmers:
    #print kmer
    left = kmer[ : -1 ]
    right = kmer[ 1 : ]
    edge_count += 1

    if left in g:
        g[ left ].append( right )
    else:
        g[ left ] = [ right ]

    if left in counts:
        counts[ left ][ 1 ] += 1
    else:
        counts[ left ] = [ 0, 1 ]

    if right in counts:
        counts[ right ][ 0 ] += 1
    else:
        counts[ right ] =[ 1, 0 ]

non_branching = set()
contigs = []

def build_graph( start, g ):
    global edge_count
    path = [ start ]
    cur_node = start

    while len( cur_node ) > 0:
        next_node = g[ cur_node ][ 0 ]
        del g[ cur_node ][ 0 ]
        #if len( g[ cur_node ] ) == 0:
        #    del g[ cur_node ]

        edge_count -= 1

        #print cur_node
        if next_node in non_branching:
            #print "non branching:", cur_node
            path.append( next_node )
            cur_node = next_node
            continue
        else:
            path.append( next_node )
            break

    return path

#print g
#print counts

def merge_nodes( nodes ):
    contig = nodes[ 0 ]
    for i in range( 1, len( nodes ) ):
        contig += nodes[ i ][ -1 ]
    return contig

def has_outgoing( node ):
    if len( g[ node ] ) > 0:
        return True
    else:
        return False

for key, item in counts.iteritems():
    if item[ 0 ] == 1 and item[ 1 ] == 1:
        non_branching.add( key )

#print non_branching

start = g.keys()[ 0 ]
start = 'TG'
#while( edge_count > 0 ):
#    print edge_count
while edge_count > 0:
    for i in g.keys():
        if i in non_branching or len( g[ i ] ) == 0:
            continue
        start = i
        break
    #print "starting with:", start
    c = build_graph( start, g )
    contigs.append( c )

for contig in contigs:
    print merge_nodes( contig )
