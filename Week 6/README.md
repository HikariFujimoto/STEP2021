# Google STEP 2021 Week 6 Malloc Challenge

## Assignment
Implement malloc without using the C library malloc() or free(). Sample Program implements first fit algorithm, implement best fit and worst fit algorithm to improve execution time and memory utilization. 
Sample programs are given by hikalium [here](https://github.com/hikalium/malloc_challenge/tree/main/real_malloc)

## Algorithm
Within the program, any data or free slot is saved by metadata placed prior to the object which also holds the size of the slot, and metadata for free slot acts as a linked list to show the free list. 
The overall flow of the program is as follows:
- Given data, determine if there are free slot wich the data can be placed
- If there is, remove the free slot from the free list, place the data in the slot, and add the remaining free space back to free list.
- If not, request new memory region
- When a data is freed, add the slot back to free list

#### First Fit:
Taken from the [sample program](https://github.com/hikalium/malloc_challenge/blob/main/real_malloc/simple_malloc.c)
Looks for the first free slot the object fits.
Example execution time and memory utilization of first fit:
```
Challenge 1: 
Time: 13ms  Utilization: 70%
Challenge 2: 
Time: 11ms  Utilization: 40%
Challenge 3: 
Time: 176ms  Utilization: 8%
Challenge 4: 
Time: 27476ms  Utilization: 15%
Challenge 5: 
Time: 22433ms  Utilization: 15%
```

#### Best Fit:
Looks for the smallest free slot the object fits, in order to minimize the size of remaining free slot generated after placing data.
The algorithm requires to loop through the whole free list in order to determine the best fitting free slot. 
Example execution time and memory utilization of best fit:
```
Challenge 1: 
Time: 2016ms  Utilization: 70%
Challenge 2: 
Time: 883ms  Utilization: 40%
Challenge 3: 
Time: 1062ms  Utilization: 50%
Challenge 4: 
Time: 13547ms  Utilization: 71%
Challenge 5: 
Time: 8450ms  Utilization: 74%
```

#### Worst Fit:
Looks for the largest free slot the object fits.
Similar to best fit, the algorithm requires to loop thorugh the whole free list in order to determine the worst fitting free slot. 
Example execution time and memory utilization of worst fit:
```
Challenge 1: 
Time: 500227ms  Utilization: 4%
Challenge 2: 
Time: 92320ms  Utilization: 2%
Challenge 3: 
Time: 145461ms  Utilization: 3%
Challenge 4: 
Time: 780767ms  Utilization: 7%
Challenge 5: 
Time: 649134ms  Utilization: 7%
```

## Analysis
For execution time, first fit is faster than best fit for challenges 1 to 3.
But, overall memory utilization is better for best fit, especially for challenges 3 to 5. 
The best fit's execution time is better than best fit for challenges 4 and 5, therefore conclude best fit is more suited for memory alloacation.

## Further Improvement
In order to further improve the best fit solution, implementing a process to merge two free slots next to each other to reduce fragmentation is a viable option.
"malloc_best_fit_merge.c" is a WIP program implementing such algorithm. (disclaimer: it does not work yet)
To implement the merge function, the add_to_free_slot function is modified to determine if there are any neighboring free slots to the slot being added to free list.
If there is, then the two free slots are merged to have one metadata. If not, the original process of free slot being added to the beggining of free list is conducted. 