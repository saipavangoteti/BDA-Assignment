# BDA-Assignment


# Example Input Format (initial graph with equal rank distribution):
# A	0.2|B,C
# B	0.2|A,D
# C	0.2|A
# D	0.2|B

# Example Usage (assuming input.txt contains the graph data):
# cat input.txt | python mapper.py | sort | python reducer.py > output.txt

# Iterate the MapReduce job until convergence (ranks stabilize).
# You'll use the output.txt of one iteration as the input.txt for the next iteration.
# You can check for convergence by comparing the PageRank values between iterations.
