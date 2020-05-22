# Description

- The A* search algorithm considers the estimated cost at each node and goes
for the cheapest one.  
- This cost `f` is calculated off of two factors `f = g + h` where `g` is the cost so far from the source node and `h` is the heuristic cost of the  current node 
from the goal node.  
- I have used Euclidean distance as a metric for calculating the heuristic distance.  

## Data Structure

- **Priority Queue**: This pops off the element with the highest priority first, which in our case would be the node with the cheapest cost.
The time complexity for `get()` and `put()` is O(logn). 
