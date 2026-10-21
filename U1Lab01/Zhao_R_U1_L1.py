import random, time
from collections import deque

def getInitialState():
    x = "_12345678"
    l = list(x)
    random.shuffle(l)
    y = ''.join(l)
    return y


'''precondition: i<j
swap characters at position i and j and return the new state'''
def swap(s: str, i: int, j: int) -> str:
    if i > j:
        i, j = j, i

    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]


'''
Generate a list which hold all children of the
current state and return the list.
Translation: i think this should list the
possible moves from the current position.

Example:

123 -> has 4 possible moves.
4_5
678

_23 -> 2 possible moves.
456
781
'''
def generate_children(state: str) -> list[str]:
    """
    steps:
    1. find the current pos of the _ - through .index method
    2. based on the index, we can figure out where the _ is
    on the map. so using < or >, we can determine the possible positions.

    first column: 0, 3, 6
    middle: 1, 4, 7
    end: 2, 5, 8
    """
    possibleStates = []
    
    emptyIndex = state.index('_')
    
    if emptyIndex not in [0,3,6]: possibleStates.append(swap(state, emptyIndex, emptyIndex - 1))
    if emptyIndex not in [2,5,8]: possibleStates.append(swap(state, emptyIndex, emptyIndex + 1))
    if emptyIndex not in [0,1,2]: possibleStates.append(swap(state, emptyIndex, emptyIndex - 3))
    if emptyIndex not in [6,7,8]: possibleStates.append(swap(state, emptyIndex, emptyIndex + 3))

    return possibleStates


def display_path(n, explored): #key: current, value: parent
    l = [] 
    while explored[n] != "s": #"s" is initial's parent
        l.append(n)
        n = explored[n]
    print ()
    l = l[::-1]
    for i in l:
        print (i[0:3], end = " ")
        print ()
    for j in l:
        print (j[3:6], end = " ")
        print()
    for k in l:
        print (k[6:9], end = " ")
    return len(l)


'''Find the shortest path to the goal state "_12345678" and
returns explored and an empty string or "No solution".
You can make other helper methods, but you must use dictionary for
explored.'''
def BFS(initial_state, goal = "_12345678"):
    explored = {initial_state: "s"}
    q = deque()
    q.append((initial_state, 's'))

    while len(q) > 0:
        current, parent = q.popleft()
        
        if current == goal:
            return explored, ""
        for position in generate_children(current):
            if position not in explored:
                explored[position] = current
                q.append((position, current))
    
    return explored, "No solution"


'''Find the path to the goal state "_12345678" and
returns explored and an empty string or "No solution".
You can make other helper methods, but you must use dictionary for
explored.'''
def DFS(initial_state, goal = "_12345678"):
    explored = {initial_state: "s"}
    s = deque()
    s.append((initial_state, 's'))

    while len(s) > 0:
        current, _ = s.pop()

        if current == goal:
            return explored, ""
        for position in generate_children(current):
            if position not in explored:
                explored[position] = current
                s.append((position, current))


    return explored, "No solution"


def main():
    initial = getInitialState()
    goal = "_12345678"
    # Fun of 8 puzzle
    #initial = "1234567_8"
    #initial = "14725836_"
    #initial = "12345678_"
    #initial = "84765231_"
    start = time.time()
    print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    bfs_result = BFS(initial)
    print ("\n\nThe number of nodes explored:", len(bfs_result[0]))
    if bfs_result[1] != "No solution":
        print ("\nThe shortest path length is :", display_path(goal, bfs_result[0]))
    print ("BFS duration:", time.time() - start)
#    start = time.time()
#    print ("\n\nDFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
#    dfs_result = DFS(initial)
#    print ("\n\nThe number of nodes explored:", len(dfs_result[0]))
#    if dfs_result[1] != "No solution":
#        print ("\nThe path length is :", display_path(goal, dfs_result[0]))
#    print ("DFS duration:", time.time() - start)
#

if __name__ == '__main__':
    main()