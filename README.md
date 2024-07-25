The A* algorithm uses an evaluation function 
𝑓(𝑛)=𝑔(𝑛)+ℎ′(𝑛) f(n)=g(n)+h'(n)},   h'(n) represents the heuristic value of the node to be evaluated from the current, n, to the end, and g(n), 
the actual cost of the path taken to reach that node, n, from the initial node. A* maintains two auxiliary data structures, which we can call open, implemented as a priority queue 
(ordered by The Value 𝑓(𝑛)of each node), and closed, where the information of the nodes that have already been visited is stored.
At each step of the algorithm, the node that is first open expands, and in case it is not a target node, it calculates the 𝑓(𝑛){displaystyle f(n)} of all its children, inserts them into open,
and passes the evaluated node to closed.
The algorithm is a combination of first-in-width and first-in-depth searches: while It is a route calculator that implements the A* algorithm where it looks for the most efficient
path between two points using heuristics and costs also uses Manhattan distance with the priority queue
