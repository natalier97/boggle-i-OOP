import random
import string

class BoggleBoard:
  
  def __init__(self,board=[]):
    ##4x4 grid, empty at first
    self.board = [["_", "_", "_", "_"],
                  ["_", "_", "_", "_"],
                  ["_", "_", "_", "_"],
                  ["_", "_", "_", "_"]]
    
    def __str__(self):
      return f"this is the board:{self.board}"
  
    def __repr__(self):
      return f"this is the board: {self.board}"

# When a new 'BoggleBoard' is initialized the output should look like this:

  
  def new_board(self):
    for row in self.board:
      print(row)

##shake --> fill each cell w/ random UPPERCASE letter
  def shake(self):
    # random.choice{}
    row_number = 0

    for row in self.board:
    #   row_number += 1
    #   print(row_number)
      for char in range(len(row)):
        random_char = random.choice(string.ascii_uppercase)
        row[char] = row[char].replace('_', random_char)
        # self.board[row_number][0] = "A"

    print(self.board)



board1 = BoggleBoard()

print(board1.shake())