# Name:          Date:
import time
from collections import deque


def generate_adjacents(current, words_set):
    ''' words_set is a set which has all words.
    By comparing current and words in the words_set,
    generate adjacents set of current and return it'''
    adj_set = set()
    
    for c in range(len(current)):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if (new_word := current[:c] + letter + current[c+1:]) in words_set:
                adj_set.add(new_word)
    
    return adj_set

def check_adj(words_set):
    # This check method is written for words_6_longer.txt
    adj = generate_adjacents('listen', words_set)
    target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
    return (adj == target)

def build_path(front_seen, back_seen, meeting_point):
    path = []

    curr = meeting_point
    while curr is not None:
        path.append(curr)
        curr = front_seen[curr]
    path.reverse() # make backwards - we work from meeting to starting

    curr = back_seen[meeting_point]
    while curr is not None:
        path.append(curr)
        curr = back_seen[curr]

    return path

def bi_bfs(start, goal, words_set):
    '''The idea of bi-directional search is to run two simultaneous searches--
    one forward from the initial state and the other backward from the goal--
    hoping that the two searches meet in the middle. 
    '''
    # use a queue
    front_q = deque()
    back_q = deque()

    front_q.append(start)
    back_q.append(goal)

    front_seen = {start: None}
    back_seen = {goal: None}

    while front_q and back_q:
        if len(front_q) <= len(back_q):
            curr = front_q.popleft()

            for adj in generate_adjacents(curr, words_set):
                if adj in front_seen:
                    continue

                front_seen[adj] = curr # set parent
                front_q.append(adj)

                if adj in back_seen:
                    return build_path(front_seen, back_seen, adj) 
        else:
            curr = back_q.popleft()

            for adj in generate_adjacents(curr, words_set):
                if adj in back_seen:
                    continue

                back_seen[adj] = curr # set parent
                back_q.append(adj)

                if adj in front_seen:
                    return build_path(front_seen, back_seen, adj) 
    return None

def main():
    filename = input("Type the word file: ")
    words_set = set()
    file = open(filename, "r")
    for word in file.readlines():
        words_set.add(word.rstrip('\n'))
    #print ("Check generate_adjacents():", check_adj(words_set))
    initial = input("Type the starting word: ")
    goal = input("Type the goal word: ")
    cur_time = time.time()
    path = (bi_bfs(initial, goal, words_set))
    if path != None:
        print (path)
        print ("The number of steps: ", len(path))
        print ("Duration: ", time.time() - cur_time)
    else:
        print ("There's no path")
 
if __name__ == '__main__':
    main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''


