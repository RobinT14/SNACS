# Code snippet 3 for code review session
# By Roos Wensveen & Robin The
#
# This code snippet is used to approximate the betweenness
# centrality using the networkit library. In this library
# the approach from "Geisberger" is used as well as the
# one from our paper "Riondato"
#
# To run: python3 codeReview3.py [FILE]

import networkit as nk
import sys
import time

filename = sys.argv[1]

# Read a graph
# This accepts edge lists that are separated by a tab or space
# To get matching node IDs and nodes, start with a vertex 0
try:
    G = nk.readGraph(filename, nk.Format.EdgeListTabZero, directed=False)
except:
    try:
        G = nk.readGraph(filename, nk.Format.EdgeListSpaceZero, directed=False)
    except:
        print("Wrong format")
        exit(1)

# "Geisberger" approach:
betweenness = nk.centrality.EstimateBetweenness(G, 50, True, False)
start_time = time.time()

betweenness.run()
print("--- Geisberger approach --- ")
print('Betweenness centrality ranked', betweenness.ranking())
print("Total execution time: %s seconds " % (time.time() - start_time))

# "Riondato" approach:
betweenness_riondato = nk.centrality.ApproxBetweenness(G,
                                                       epsilon=0.1,
                                                       delta=0.1,
                                                       universalConstant=0.5)
betweenness_riondato.run()
print("--- Riondato approach --- ")
print('Betweenness centrality ranked', betweenness_riondato.ranking())
print("Total execution time: %s seconds " % (time.time() - start_time))

# "Bergamini and Meyerhenke" approach:
betweenness_bergamini = nk.centrality.DynApproxBetweenness(
    G, epsilon=0.01, delta=0.1, storePredecessors=True, universalConstant=0.5)
betweenness_bergamini.run()
print("--- Bergamini approach --- ")
print('Betweenness centrality ranked', betweenness_bergamini.ranking())
print("Total execution time: %s seconds " % (time.time() - start_time))
