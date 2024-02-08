import random
import string

class BoggleBoard:
  
  def __init__(self,board=[]):
    ##4x4 grid, empty at first
    self.board = [["_", "_", "_", "_"],
                  ["_", "_", "_", "_"],
                  ["_", "_", "_", "_"],
                  ["_", "_", "_", "_"]]
    
    #dice list
    self.dice = [['A','A','E','E','G','N'], ['E','L','R','T','T','Y'], ['A','O','O','T','T','W'], ['A','B','B','J','O','O'],
                ['E','H','R','T','V','W'], ['C','I','M','O','T','U'], ['D','I','S','T','T','Y'], ['E','I','O','S','S','T'],
                ['D','E','L','R','V','Y'], ['A','C','H','O','P','S'], ['H','I','M','N','Q','U'], ['H','I','M','N','Q','U'],
                ['E','E','G','H','N','W'], ['A','F','F','K','P','S'], ['H','L','N','N','R','Z'], ['D','E','I','L','R','X']]
    
    def __str__(self):
      return f"this is the board:{self.board}"
  
    def __repr__(self):
      return f"this_ is the board: {self.board}"



  # When a new 'BoggleBoard' is initialized the output should look like this:
  def new_board(self):
    for row in self.board:
      print(row)
  
  def letter(self):
    random_dice=random.choice(self.dice)
    random_letter=random.choice(random_dice)
    return random_letter
  
##shake --> fill each cell w/ random UPPERCASE letter
  def shake(self):
    # random.choice{}

    for row in self.board:
      for char in range(len(row)):
        # random_char = random.choice(string.ascii_uppercase)
        # row[char] = row[char].replace('_', random_char)
          row[char] = row[char].replace('_', self.letter())
          if row[char]== "Q":
            row[char] = "Qu"
              
    #print board game now that it has been shaken         
    for row in self.board:
      print(row)

board1 = BoggleBoard()

print(board1.shake())