from validation import Validation

row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]
col_letter = ['a','b','c','d','e','f','g','h','i','j','k','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
N = 8


class Chess:  
  def __init__(self, position):
    self.position = position  
    self.validation = Validation(self.position, col_letter, N)

  def find_knight_possibilities_in_two_tours(self):
    self.validation.validate_params()
    self.init_position_variables()
    possibilities = self.find_knight_possibilities(self.position_x, self.position_y)
    final_result = self.init_fina_result_valriables(possibilities)         
    return self.find_knight_possibilities_second_turn(possibilities, final_result)        

  def init_position_variables(self):      
    self.position_y = int(self.position[-1]) - 1
    self.position_x = int(col_letter.index(self.position[0]))

  def init_fina_result_valriables(self, possibilities):   
    final_result = {}
    final_result['firstTurn'] = possibilities[2]
    final_result['secondTurn'] = {}
    return final_result

  def find_knight_possibilities_second_turn(self, possibilities, final_result):
    i = 0    
    for j in possibilities[0]:
        current_possibilities = self.find_knight_possibilities(j, possibilities[1][i])
        final_result['secondTurn'][col_letter[possibilities[1][i]] + str(j + 1)] =  current_possibilities[2]
        i = i +1
    return final_result     

  def find_knight_possibilities(self, x, y):
    self.init_arrays()   
    for k in range(N):
        possible_valid_position_x = x + row[k]
        possible_valid_position_y = y + col[k] 
        self.append_valid_move_when_is_valid(possible_valid_position_x, possible_valid_position_y)
    return [self.array_of_x, self.array_of_y, self.possible_moves]

  def init_arrays(self):    
      self.array_of_x = []; self.array_of_y = []; self.possible_moves = []

  def append_valid_move_when_is_valid(self, x, y):
    if self.validation.is_valid_move(x, y):
        self.array_of_x.append(x)
        self.array_of_y.append(y)
        self.possible_moves.append(col_letter[y] + str(x + 1))                