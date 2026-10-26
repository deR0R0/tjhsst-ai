# Name: Robert Zhao
# Date: 10/23/26

def check_complete(assignment:str, csp_table):
   return assignment.find(".") == -1
   
def select_unassigned_var(assignment, variables, csp_table):
   return assignment.find(".") # just return the first one...

def isValid(value, var_index, assignment, variables, csp_table):
   """
   .........
   .........
   .........
   .........
   .........
   .........
   .........
   .........
   .........
   """
   # vertical check
   bot_amount = (80 - var_index) // 9
   top_amount = var_index // 9
   for x in range(bot_amount):
      if value == assignment[var_index+((x+1)*9)]:
         return False

   for x in range(top_amount):
      if value == assignment[var_index-((x+1)*9)]:
         return False
   # horizontal checa
   row = (var_index // 9) * 9
   for x in range(9):
      if row + x != var_index and assignment[row+x] == value:
         return False
   # box check
   row = ((var_index // 9) // 3 ) * 3
   col = ((var_index % 9) // 3 ) * 3
   for c in range(3):
      for r in range(3):
         index = (row + r) * 9 + (col + c)
         if index != var_index and value == assignment[index]:
            return False
   return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return list("123456789")

def update_variables(value, var_index, assignment, variables, csp_table):
   return {}

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment, csp_table):
      return assignment
   var = select_unassigned_var(assignment, variables, csp_table)
   for value in ordered_domain(var, assignment, variables, csp_table):
      if isValid(value, var, assignment, variables, csp_table):
         new_assignment = assignment[:var] + value + assignment[var+1:]
         result = recursive_backtracking(new_assignment, variables, csp_table)
         if result is not None:
            return result
   return None

def display(solution):
   final = ""
   for i, char in enumerate(solution):
      if i % 3 == 0 and i != 0:
         final += "  "
      if i % 9 == 0 and i != 0:
         final += "\n"
      if i % 27 == 0 and i != 0:
         final += "\n"
      final += char + " "
   return final

def sudoku_csp():
   return [[]]

def initial_variables(puzzle, csp_table):
   vars = {}
   for i, char in enumerate(puzzle):
      if char == ".":
         vars[i] = []
         for option in "123456789":
            if isValid(option, i, puzzle, vars, csp_table):
               vars[i].append(option)
      else:
         vars[i] = [char]
   return vars
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()

