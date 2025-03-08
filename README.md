# BDA-Assignment


Example Input Format (initial graph with equal rank distribution):
A	0.2|B,C
B	0.2|A,D
C	0.2|A
D	0.2|B

Example Usage (assuming input.txt contains the graph data):
cat input.txt | python mapper.py | sort | python reducer.py > output.txt

Iterate the MapReduce job until convergence (ranks stabilize).
You'll use the output.txt of one iteration as the input.txt for the next iteration.
You can check for convergence by comparing the PageRank values between iterations.


## Explanation

    1. Clearer Data Representation: The code now explicitly uses tuples (rank, neighbors) to represent the original node data and floats for rank contributions. This makes the logic in the reducer much cleaner.
    2. Dangling Node Handling: The mapper now checks for dangling nodes (nodes with no outgoing links) to avoid division by zero errors. It simply doesn't distribute rank from a dangling node.
    3. Type Handling in Reducer: The reducer now includes a try-except block to handle potential ValueError exceptions when parsing the values. This makes the code more robust to malformed input. It also checks if the value is a tuple (original data) or a float (rank contribution).
    4. Explicit Damping Factor: The PageRank calculation now includes the damping factor d (set to 0.85 in this example) explicitly.
    5. Re-emitting Graph Structure: The reducer now correctly re-emits the graph structure (node and its neighbors) along with the updated PageRank value. This is crucial for the next iteration of MapReduce.
    6. Output Format: The output format from the reducer is now consistent with the input format, making it easy to chain multiple MapReduce jobs. It's node\tRank|neighbor1,neighbor2,...
    7. Convergence: The code doesn't include explicit convergence checking. You would typically implement this in a driver script that runs the MapReduce job multiple times. After each iteration, you'd compare the PageRank values with the previous iteration. If the changes are below a certain threshold, you consider the algorithm to have converged.


## How to Run and Iterate:
    1. Save: Save the mapper code as mapper.py and the reducer code as reducer.py. Make them executable: chmod +x mapper.py reducer.py
    2. Initial Input: Create a file named input.txt with your initial graph data in the specified format.
    3. Run First Iteration:
cat input.txt | ./mapper.py | sort -k1,1 | ./reducer.py > output.txt

    4. Subsequent Iterations: Copy output.txt to input.txt (or rename it). Then run the same command again. Repeat this process until the PageRank values in output.txt stabilize (converge).
    5. Convergence Check: You'll need to write a small script (e.g., in Python) to compare the PageRank values between iterations to determine when the algorithm has converged. This script would read the output.txt files from consecutive iterations and calculate the difference in PageRank values.
