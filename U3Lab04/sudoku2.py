# Name: 
# Date: 
import os, time

def check_complete(assignment:str, q_table):
   return assignment.find(".") == -1

def find_unfilled(assignment:str, neighbors, q_table):
   # do mrv
   possible_values = [i for i in range(len(assignment)) if assignment[i] == "."]
   unfilled = {}
   for value in possible_values:
      unfilled[value] = len(get_possible_values(value, assignment, neighbors, q_table))

   # find which variable has the least number of unfilled neighbors
   return min(unfilled, key=unfilled.get)

def get_possible_values(var_index, assignment, neighbors, q_table):
   # this is faster than the commented. this is straight horseshit. should probably call this once outside the loop rather than having it run mutliple million times per second.
   #possible_values = set("123456789")
   #for neighbor in neighbors[var_index]:
   #   if assignment[neighbor] != ".":
   #      possible_values.discard(assignment[neighbor])
   return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def initialize_ds(puzzle, neighbors):
   return {}, puzzle, {str(i): puzzle.count(str(i)) for i in range(1, 10)}

def solve(puzzle): 
   # q_table is quantity table {'1': number of value '1' occurred, ...}
   neighbors = sudoku_neighbors(sudoku_csp())
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  
   return recursive_backtracking(puzzle, variables, neighbors, q_table)

def recursive_backtracking(assignment, variables, neighbors, q_table):
   if check_complete(assignment, q_table):
      return assignment
   var = find_unfilled(assignment, neighbors, q_table)
   for value in get_possible_values(var, assignment, neighbors, q_table):
      new_assignment = assignment[:var] + value + assignment[var+1:]
      result = recursive_backtracking(new_assignment, variables, neighbors, q_table)
      if result is not None:
         return result
   return None

def sudoku_neighbors(csp_table):
   # build a dictionary of neighbors for each variable
   neighbors = {}
   for x in range(81):
      neighbors[x] = set()
   # add the row neighbors
   for row in csp_table[:9]:
      for x in row:
         neighbors[x].update(set(row) - {x})
   # add the column neighbors
   for col in csp_table[9:18]:
      for x in col:
         neighbors[x].update(set(col) - {x})
   # add the sub-block neighbors
   for sub_block in csp_table[18:27]:
      for x in sub_block:
         neighbors[x].update(set(sub_block) - {x})
   return neighbors
   
def sudoku_csp(n=9):
   csp_table = [[k for k in range(i*n, (i+1)*n)] for i in range(n)] # rows
   csp_table += [[k for k in range(i,n*n,n)] for i in range(n)] # cols
   temp = [0, 1, 2, 9, 10, 11, 18, 19, 20]
   csp_table += [[i+k for k in temp] for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]] # sub_blocks
   return csp_table

def checksum(solution):
   return sum([ord(c) for c in solution]) - 48*81 # One easy way to check a valid solution

# Make sure comment out main() before submission!
def main():
   filename = input("file name: ")
   if not os.path.isfile(filename):
      filename = "puzzles.txt"
   start_time = time.time()
   for line, puzzle in enumerate(open(filename).readlines()):
      #if line == 50: break  # check point: goal is less than 0.5 sec
      line, puzzle = line+1, puzzle.rstrip()
      print ("Line {}: {}".format(line, puzzle)) 
      solution = solve(puzzle)
      if solution == None:print ("No solution found."); break
      print ("{}({}, {})".format(" "*(len(str(line))+1), checksum(solution), solution))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
