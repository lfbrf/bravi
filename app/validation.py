class Validation:  
  def __init__(self, position, col_letter, N):
    self.position = position  
    self.col_letter = col_letter
    self.N = N

  def validate_params(self):
    self.validate_params_charcters()
    self.validate_position_x()
    self.validate_position_y()

  def validate_params_charcters(self):
    if len(self.position) != 2:
      raise ValueError(f'Position of {self.position} is invalid')

  def validate_position_x(self):
    if self.position[0] not in self.col_letter[:self.N:]:
      raise ValueError(f'Position of {self.position} is invalid')

  def validate_position_y(self):
    if int(self.position[-1]) not in range(self.N):
      raise ValueError(f'Position of {self.position} is invalid')

  def is_valid_move(self, x, y):
    return not (x < 0 or y < 0 or x >= self.N or y >= self.N)            