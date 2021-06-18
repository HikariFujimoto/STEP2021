# Google STEP 2021: Travelling Salesman Problem Challenges

## Assignment
Modify the greedy algorithm solving TSP to find a more optimized path.
Original/sample program is given [here](https://github.com/hayatoito/google-step-tsp)

## Algorithm
In order to optimize the path, the modified greedy solution repeats the process of finding greedy solution starting from different starting point and two-opts the path before comparing with previous greedy solution to determine the shortest run.

The overall process is as follows:
- Randomly select a starting point within the given dataset
- Determine the greedy solution (connecting the nearest unvisited points)
- Run two-opt to further improve the path given by greedy solution
- Compare the total distance of the path to shortest distance of previous paths, replace if shorter.

The above process is repeated multiple times in the program. (From challenge 0~4, incresing the number of repetition does not take too much time; as for challenge 5, 10 times is decent while for challenge 6, generating one path takes time so tried with 5 trials.) To further improve the output, increasing the number of trials is suggested, although it takes a while to complete challenge 5 and 6.

