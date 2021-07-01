# Google STEP 2021: Week 7 Assignment

## Assignment
Get a best score solving the TSP

## Improvements from Previous Solution
Previously, I have tried to randomely select a starting node, get the greedy solution from the node, run two-opt once on the greedy solution, them repeat the whole process multiple times in order to find the most optimized path. 
But, because the program was written in python, the execution time was extremely slow, thus computing for challenge 7 is near-impossible, as well as the resulting path not being very efficient.
So, I decided to implement a different algorithm, the neatest insertion for faster execution and a better result than modifying the greedy solution. 
I have also further improved the program generally to ask for the challenge No. when running the program instead of having to change the input and output file name in the code. This also guarantees that the input and output file names are corresponding.

## Algorithm Outline
To optimize the result, nearest insertion was implemented, which initially starts with two nodes in the path and repeats the process of inserting an unvisited node inbetween visited nodes in a way so the resulring path is the shortest, until there are no unvisited cities left.

These are the steps of this algorithm:
1. Initialize all vertices as unvisited
2. Select an arbitrary vertex, set it as the current vertex *u*. Mark *u* as visited.
3. Find out the shortest edge connecting the current vertex *u* and an unvisited vertex *v*.
4. Set *v* as the current vertex *u*. Mark *v* as visited.
5. If all the vertices in the domain are visited, then terminte. Else, go to step 3.

from Wikipedia Page ["Nearest neighbour algorithm"](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm)

As for selection of the unvisited vertex *v*, I tried implementing two different versions; `nearest_neighbour_insertion.py` selects the most nearest node of the most recently visited node, while `nearest_insertion_in_order.py` selects nodes in an increasing order starting from 0.

Although this algorithm executes decently fast, the result may not be the best. So, as I did in the previous solution, I have randomized the intial node and repeated the process in order to determine the best result of 20 runs, implemented in `random_nearest_neighbour.py` and `random_in_order.py`.

## Evaluation
The result of nearest insertion algorithm + multiple runs from random starting point generally resulted in a better score than the greedy solution. 
Following tables are the results of actual execution:
Challenge 6:
|                   | Starting from 0 | Random start + 20 runs #1 | Random start + 20 runs #2 |
|-------------------|:---------------:| -------------------------:| -------------------------:|
| nearest neighbour | 50136.88        | 49532.19                  | 49682.33                  |
| in order from 0   | 44556.49        | 43989.06                  | 44384.93                  |

Challenge 7:
|                   | Starting from 0 | Random start + 20 runs #1 | Random start + 20 runs #2 |
|-------------------|:---------------:| -------------------------:| -------------------------:|
| nearest neighbour | 99415.42        | 99675.47                  | 99946.28                  |
| in order from 0   | 88790.80        | 88450.89                  | 88914.11                  |

Interestingly, rather than selecting the nearest neighbour of the current node, inserting nodes in an increasing order resulted in a shorter path. The randomized starting point + multiple runs usually resulting in a better result, which was expected.

## Possible improvements
With the current program, it first calculates and saves the distance between all nodes to use later, but this process consumes time, especially with challenge 7 due to its nature. Therefore, to further improve the program, rather than initially calculating every distance, implement a structure which calculates the distance only when needed and if a distance between two nodes are calculated, it is stored for later use so the calculation is done only once.