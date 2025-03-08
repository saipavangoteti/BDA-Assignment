#!/usr/bin/env python

import sys

def map_pagerank(line):
    node, data = line.strip().split('\t')
    rank, neighbors = data.split('|')
    rank = float(rank)
    neighbors = neighbors.split(',')

    # Emit the current node and its rank (for rebuilding the graph)
    yield node, (rank, neighbors)

    # Distribute rank to neighbors
    num_neighbors = len(neighbors)
    if num_neighbors > 0:  # Avoid division by zero for dangling nodes
        contribution = rank / num_neighbors
        for neighbor in neighbors:
            yield neighbor, contribution


for line in sys.stdin:
    for key, value in map_pagerank(line):
        print(f"{key}\t{value}")
