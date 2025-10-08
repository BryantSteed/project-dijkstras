# Project Report - Network Routing

## Baseline

### Design Experience

For the linear PQ, I will implement it as a python list and simply iterate over that list when I put something in there that has priority to know where it needs to be put. To extract from the PQ, I will simply pop the element from the front (or back) of the list.

I will implemented the actual path finding by simply translating the pseudocode into python source. The correspondence between the two is pretty much 1 to 1.

### Theoretical Analysis - Dijkstra's With Linear PQ

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Dijkstra's With Linear PQ

| N    | Density | time (ms) |
|------|---------|-----------|
| 500  | .2      |           |
| 1000 | .2      |           |
| 1500 | .2      |           |
| 2000 | .2      |           |
| 2500 | .2      |           |
| 3000 | .2      |           |
| 3500 | .2      |           |

### Comparison of Theoretical and Empirical Results - Dijkstra's With Linear PQ

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 


![img](img.png)

*Fill me in*

## Core

### Design Experience

For the heap priority queue, I will also implement the binary heap using a linked list. But instead of iterating over every element when I insert, I will insert at the bottom of the heap and have it percolate it up. When I pop from the priority queue, I will initially put the element at the bottom of the heap on the top and have that element percolate its way down. My implementation for the actual dijkstra's will be the exact same except for the use of data structure. 

### Theoretical Analysis - Dijkstra's With Heap PQ

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Dijkstra's With Heap PQ

| N    | Density | time (ms) |
|------|---------|-----------|
| 500  | .2      |           |
| 1000 | .2      |           |
| 1500 | .2      |           |
| 2000 | .2      |           |
| 2500 | .2      |           |
| 3000 | .2      |           |
| 3500 | .2      |           |



### Comparison of Theoretical and Empirical Results - Dijkstra's With Heap PQ

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

### Relative Performance Of Linear versus Heap PQ Performance

*Fill me in*

## Stretch 1

### Design Experience

To collect the data, I will simply use the command line input given to me. Then I will use matplotlib to plot the data. I will likely use the subplots feature.

I think that for both the more dense graphs and the less dense graphs, the heap will be faster for both because logarithmic time should always beat linear time regardless of how dense the graph is. I just don't think that the density will make a huge difference. Sure, the PQ does a lot of pointer arithmetic in percolation, but I still think that that will be faster than iterating over all elements of the list in every case.

### Empirical Data

| N    | Density | heap time (ms) | linear PQ time (ms) |
|------|---------|----------------|---------------------|
| 500  | .6      |                |                     |
| 1000 | .6      |                |                     |
| 1500 | .6      |                |                     |
| 2000 | .6      |                |                     |
| 2500 | .6      |                |                     |
| 3000 | .6      |                |                     |
| 3500 | .6      |                |                     |


| N    | Density | heap time (ms) | linear PQ time (ms) |
|------|---------|----------------|---------------------|
| 500  | 1       |                |                     |
| 1000 | 1       |                |                     |
| 1500 | 1       |                |                     |
| 2000 | 1       |                |                     |
| 2500 | 1       |                |                     |
| 3000 | 1       |                |                     |
| 3500 | 1       |                |                     |

### Plot

*Fill me in*

### Discussion

*Fill me in*

## Stretch 2

### Design Experience

I think that the provided algorithm could be real in certain contexts where the weights actually are normally distributed. However, this implies a sense of randomness to the weights in actual business contexts that I don't think is always correct. If we talking about cities, I'm not sure that the distances from cities is necessarily going to be normally distributed because it just depends, but it still might be a useful heuristic for testing the algorithm.

Another way that you could generate a graph is by having each successive weight be greater than the first.

The kind of graph generation algorithm that I will develop will be based on the distances between cities. I'll get the average number of roads that go out of a particular cities and the average distance distribution to the closest city. I'll pull the edges and weights from a distribution that contains these factors (number of edges in a single node and for each edge pull a random weight from a given distribution from the real world).

I will implement this using the random.choices module from the standard library and importing my own list of the most likely weights for roads and number of roads going to or out of a single city.

### Provided Graph Generation Algorithm Explanation

*Fill me in*

### Selected Graph Generation Algorithm Explanation

*Fill me in*

#### Screenshots of Working Graph Generation Algorithm

![img](small.png)

![img](medium.png)

![img](large.png)

## Project Review

*Fill me in*

