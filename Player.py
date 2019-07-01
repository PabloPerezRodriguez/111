from fabulous.color import bold, magenta, fg256

class Player:
  def __init__(self, name):
    self.name = name
    self.printable_name = bold(magenta(self.name))

    self.score = 0

  def ask_to_re_roll(self, must_re_roll, _, __):
    if must_re_roll:
      while True:
        res = input(f'{bold(fg256("orangered", "Do you want to roll?"))} (y) ')
        if res == 'y':
          return True  
    else:
      while True:
        res = input(f'{bold(fg256("orangered", "Do you want to roll?"))} (y/n) ')
        if res == 'y':
          return True
        elif res == 'n':
          return False
    
  def round_end(self):
    pass
      
  def round_start(self):
    pass