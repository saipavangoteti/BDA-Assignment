#!/usr/bin/env python

import sys

def reduce_pagerank(key, values):
    total_contribution = 0
    neighbors = None
    for value in values:
        if isinstance(value, tuple):  # Original node data
            rank, neighbors = value
        else:  # Rank contribution from a neighbor
            total_contribution += value

    # PageRank calculation with damping factor (e.g., 0.85)
    d = 0.85
    new_rank = (1 - d) + d * total_contribution

    # Re-emit the node and its updated rank, along with the neighbors
    yield key, (new_rank, neighbors)


current_key = None
values = []

for line in sys.stdin:
    key, value = line.strip().split('\t')

    try:  # Handle potential type errors (value could be float or tuple)
        if value.startswith('('): # It's a tuple (original data)
            rank_str, neighbors_str = value[1:-1].split(',')
            value = (float(rank_str), neighbors_str.split(' '))
        else:
          value = float(value) # it's a contribution from a neighbor

    except ValueError:
        continue  # Skip lines with invalid format



    if key == current_key:
        values.append(value)
    else:
        if current_key:
            for k, v in reduce_pagerank(current_key, values):
                print(f"{k}\t{v[0]}|{','.join(v[1])}") # Output the updated rank and neighbors
        current_key = key
        values = [value]

# Process the last key
if current_key:
    for k, v in reduce_pagerank(current_key, values):
        print(f"{k}\t{v[0]}|{','.join(v[1])}")
