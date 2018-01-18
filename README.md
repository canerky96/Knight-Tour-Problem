# Knight Tour Problem
**Reference for Heuristic**: Paris L, Heuristic Strategies for the Knight Tour Problem, http://ai2-s2-pdfs.s3.amazonaws.com/ebdf/b585eaea47f52ab774759da2c39fb6d0d8e6.pdf
## Problem Formulation
  **States**: Any sequence of 0 to NxN visited squares.  
  **Initial State**: A knight in 0,0 point(bottom left) on the board.  
  **Actions**: Perform a knight move from current square to next unvisited square.  
  **Goal Test**: All NxN square are visited by knight. 
  
  **Path Cost**: No path cost.

## Algorithms
 * **Breadth First Search**
 
 BFS algorithm is more advantageous in problems whose solution is in unknown place of graph
or lower depth of graph. BFS algorithm increases the number of nodes in frontier dramatically in each
depth. We know that our solution is in maximum depth. Algorithm reaches the maximum depth after
expanded all nodes in previous depths. Our memory cannot store frontier even small chessboards after
a certain time since the frontier exceeds size of memory. You will see in test result. Briefly, BFS is not
proper for our problem because of its space complexity (O(b^d)).

 * **Depth First Search**
 
 DFS is advantageous for our problem since it traverse graph vertically. Even in high
chessboards, it reaches maximum depth easily. Also frontier stores small number of nodes(O(b*m)).
We know that the solution is in maximum depth but we don’t know which path goes to
maximum(NxN) depth. Some nodes may carry us a path that is not a solution. Algorithm will traverse
the graph until it will find the solution. The issue with DFS is time complexity(O(b^d)). Namely, we
will certainly find a solution with DFS without deal with memory space but it may take very very long
time.
 
 * **Depth First Search with Node Selection**
 
 When we look at DFS, it is very efficient algorithm about memory with linear space. But we
need to traverse all graph to find solution. If we eliminate some nodes before expanded them, we can
reach a solution in shorter time.
We read the paper and understood all heuristics. There are two case that causes a fault. First one
is inaccessible square. If there is a square which cannot be visited, it is an inaccessible node. This can
be seen by selecting any node and looking at the unvisited nodes that is can be visited by knight moves.
Second case is dead-end. In any step, if there is no square that can be visited by current square, this is
dead-end situation.
There are two heuristics which tries to prevent these two situation. First one is hla which looks
current square’s neighbors’(squares that can be visited by current square) options and chooses square
with most options. This heuristic prevents dead-end but cannot prevent inaccessible square situation.
Other heuristic is hlb. Unlike the hla, hlb chooses the square with least options. It prevents inaccessible
square situation and prevents dead-end indirectly(intentionally). After some test programs have made, it
is shown that hlb is more heuristic than hla. However, hlb is not a perfect heuristic. It fails on some
particular size and very large boards.
After that, to improve hlb heuristic, a new improved heuristic h2 is proposed. In any case of tie
for hlb, when there are more than one squares that have the least options, it will be chosen the lowestvalued
square nearest to any of four corners of board. Although, hlb fails in some board sizes and large
boards, h2 finds a solution successfully.
