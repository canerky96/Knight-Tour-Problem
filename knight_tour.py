from collections import deque
import time
import operator
from math import pow,sqrt

class Nodes: #Node class to hold visited places

    def __init__(self,x,y):

        self.parent = []
        self.x = x
        self.y = y

    def createCopy(self,n): # hard copy method

        temp=Nodes(n[0],n[1])
        temp.x=n[0]
        temp.y=n[1]
        for item in self.parent:
            temp.parent.append(item)

        return temp


def isInside(x,y,n): # a method to detect, location is in board or not
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False

def new_action(Node,n,explorer_set): # returning the action numbers for current nodes

    new_moves = []
    moves = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)] #where the knight can go

    for i in moves:
        new_x = Node.x + i[0]
        new_y = Node.y + i[1]

        if isInside(new_x,new_y,n) and ((new_x,new_y) not in explorer_set): #if x,y is inside tha board and not visited yet
            new_moves.append((new_x,new_y)) #append the new action list

    return new_moves

def isGoalState(Node,n): #Action is goal state or not

    if len(Node.parent) == n*n: #n*n is equal to dept. Also is equal to path length
        return True
    else:
        return False

def sorter(list):#a sort method for h2 heuristic
    newlist = sorted(list, key=operator.itemgetter(0, 1), reverse=True)
    return newlist

def nearest(x,y,n): # method is returning the lowest-valued square nearest to any of the four corners of the board

    list = []
    d1 = sqrt(pow(x,2) + pow(y,2))
    d2 = sqrt(pow(x,2) + pow(n-1-y,2))
    d3 = sqrt(pow(n-1-x,2) + pow(y,2))
    d4 = sqrt(pow(n-1-x,2) + pow(n-1-y,2))

    list.append(d1)
    list.append(d2)
    list.append(d3)
    list.append(d4)

    return min(list)

def h2(Node,n,explored_set):#returning the option number of next moves from current node

    move_numbers = []

    for action in new_action(Node,n,explored_set):

        child = Node.createCopy(action)
        child.parent.append(action)
        move_numbers.append((len(new_action(child,n,child.parent)), nearest(action[0],action[1],n),(child.x,child.y)))
        del child

    return move_numbers

def bfs(n,limit):
    node = Nodes(0, 0) #initial state
    node.parent.append((0, 0))
    frontier = deque() #frontier with deque struct. DEQUE => queue with infinite memmory space support. Default "list" structure support 2gb space
    frontier.append(node)#adding node to frontier
    expended_node_counter = 1
    if isGoalState(node, n) == True: #checking for goal state
        return "Found in first step.", node.parent, 0,expended_node_counter
    start = time.time() #starting time
    elapsed = 0
    while 1:
        try:
            if len(frontier) == 0: # no solution found
                return "No solution exists.", None, elapsed,expended_node_counter

            Node = frontier.popleft() #FIFO
            expended_node_counter = expended_node_counter + 1
            for action in new_action(Node, n, Node.parent): #brancing current node

                child = Node.createCopy(action)
                child.parent.append(action)


                if isGoalState(child, n): #checking goal state
                    return "A solution found.", child.parent, elapsed,expended_node_counter

                frontier.append(child) #adding node to frontier

                elapsed = time.time() - start
                if elapsed > limit:
                    return "Timeout.", child.parent, elapsed,expended_node_counter #time limit control

        except MemoryError: #catching memmory overflow
            print("Exception format: Memory Error")
            return "Out of Memory",child.parent,elapsed,expended_node_counter

def dfs(n,limit):
    # From different to Breadth First Search,
    # in DFS we are popping from end of queue "LIFO"
    node = Nodes(0,0)
    node.parent.append((0,0))
    frontier = deque()
    frontier.append(node)
    expended_node_counter = 1

    if isGoalState(node,n) == True:
        return "Found in first step.",node.parent,0,expended_node_counter
    start = time.time()
    elapsed = 0
    while 1:
        try:
            if len(frontier)==0:
                return "No solution exists.",None,elapsed,expended_node_counter

            Node = frontier.pop()
            expended_node_counter = expended_node_counter + 1
            for action in new_action(Node,n,Node.parent):

                child=Node.createCopy(action)
                child.parent.append(action)


                if isGoalState(child, n):
                    return "A solution found.", child.parent, elapsed,expended_node_counter

                frontier.append(child)

                elapsed = time.time() - start
                if elapsed > limit:
                    return "Timeout.", child.parent, elapsed,expended_node_counter

        except MemoryError:
            print("Exception format: Memory Error")
            return "Out of Memory",child.parent,elapsed,expended_node_counter

def dfs_heuristic(n,limit):

    node = Nodes(0,0) #initial state
    node.parent.append((0,0))
    frontier = deque()
    frontier.append(node)
    expended_node_counter = 1
    if isGoalState(node,n) == True: #checking for goal state
        return "Found in first step.",node.parent,0,expended_node_counter

    start = time.time() #start timer
    elapsed = 0

    while 1:
        try:
            if len(frontier) == 0: # no solution found
                return "No",None,elapsed,expended_node_counter

            Node = frontier.pop() #popping node from frontier
            expended_node_counter = expended_node_counter + 1 #counter for expanded node

            #h2 is returning the action number of next move and distance from nearest corner
            #after getting results we are sorting by descending order
            #and adding the frontier. Because the nature of DFS, we are popping the correct node from end frontier

            for action in sorter(h2(Node,n,Node.parent)):

                child = Node.createCopy(action[2])
                child.parent.append(action[2])

            if isGoalState(child, n):
                return "A solution found.",child.parent,elapsed,expended_node_counter

            frontier.append(child)

            elapsed = time.time() - start
            if elapsed > limit:
                return "Timeout.", child.parent, elapsed,expended_node_counter
        except MemoryError:
            print("Exception format: Memory Error")
            return "Out of Memory",child.parent,elapsed,expended_node_counter

def main():

    while 1:
        print("a. Breadth First Search")
        print("b. Depth First Search")
        print("c. Depth First Search with Node Selection Heuristic")
        print("d. Exit")
        choice = input('Enter your choice: ')

        if choice == 'd': # if user enters 'd', finish program
            return

        n = int(input('Enter board size: '))
        limit = int(input('Enter time limit(minutes): '))
        if choice == 'a':
            print("\nSearching solution...\n")
            result, list, elapsed, expanded_nodes = bfs(n, limit*60)

        elif choice == 'b':
            print("\nSearching solution...\n")
            result, list, elapsed, expanded_nodes= dfs(n, limit*60)
        else:
            print("\nSearching solution...\n")
            result, list, elapsed ,expanded_nodes= dfs_heuristic(n, limit * 60)

        mElapsed = float(elapsed) / 60  # unit of minutes
        sElapsed = elapsed  # unit of seconds
        print("Return Status: ", result)
        print("Solution Path: ", list)
        print("Expanded nodes: ",expanded_nodes)
        print(("Execution Time: %.2f" % mElapsed), "minutes (", ("%.2f" % sElapsed), "second )\n\n")

main()