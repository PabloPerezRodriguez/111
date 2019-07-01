from Player import Player
import random
from menus import options
from fabulous.color import bold, magenta, fg256
from time import sleep


def dumb_strat(last_roll, current_score, strategy_data):
  # Always rolls again until he rolls a one (or hits the winning number) - quite a dumb strategy
  return last_roll != 1 and current_score < options('winning_number')

def the_coward(last_roll, current_score, strategy_data):
  # Never rolls again - the coward - crawling his way to victory
  return last_roll is None

def same_roller(last_roll, current_score, data):
  # Always rolls 2 (3, 4, 5 - whatever) times
  if not 'roll_amt' in data:
    data['roll_amt'] = random.randint(1, 10) # In theory this would be 1-infinity but 10 seems like a large amount of throws already
  if not 'current_rolls' in data:
    data['current_rolls'] = 0
  
  if data['first_roll_of_round']:
    # New round
    data['current_rolls'] = 0
  
  ret = data['current_rolls'] < data['roll_amt']
  data['current_rolls'] += 1
  
  return ret

def random_roller(last_roll, current_score, data):
  # Rolls <random number>(determined before the actual roll) times - different for each round
  if not 'current_rolls' in data:
    data['current_rolls'] = 0
  
  if data['first_roll_of_round']:
    # New round
    data['current_rolls'] = 0
    data['roll_amt'] = random.randint(1, 10)

  ret = data['current_rolls'] < data['roll_amt']
  data['current_rolls'] += 1
  
  return ret
  print(data['current_rolls'], data['roll_amt'])

def cautious_roller1(last_roll, current_score, data):
  # Rolls again with a probability of 33% - rather cautious (takes a roll, then a random number decides whether to
  # roll again or not - if the random number(in the range 0.0 inclusive to 1.0 exclusive) is less than or equal to
  # 0.33, the computer rolls again.
  
  if data['first_roll_of_round']:
    # New round
    return True # Take a roll
  else:
    return random.random() <= 0.33

def cautious_roller2(last_roll, current_score, data):
  # Rolls again with a probability of 50% - see the explanation above (cautious_roller1)
  
  if data['first_roll_of_round']:
    # New round
    return True # Take a roll
  else:
    return random.random() <= 0.50

def cautious_roller3(last_roll, current_score, data):
  # Rolls again with a probability of 66% - see the explanation above (cautious_roller1)
  
  if data['first_roll_of_round']:
    # New round
    return True # Take a roll
  else:
    return random.random() <= 0.66

STRATEGIES = [dumb_strat, the_coward, same_roller, random_roller, cautious_roller1, cautious_roller2, cautious_roller3]

class ComputerPlayer(Player):
  def __init__(self, name):
    super().__init__(name)
    self.strategy = random.choice(STRATEGIES)
    self.strategy_data = {}
  
  def ask_to_re_roll(self, must_re_roll, last_roll, current_score):
    #qm = ?
    reroll_qm = None
    if must_re_roll:
      print(f'{bold(fg256("orangered", "Do you want to roll?"))} (y) ', end="", flush=True)
      self.strategy(last_roll, current_score, self.strategy_data)
      reroll_qm = True
    else:
      ai_result = self.strategy(last_roll, current_score, self.strategy_data)
      print(f'{bold(fg256("orangered", "Do you want to roll?"))} (y/n) ', end="", flush=True)
      reroll_qm = ai_result

    self.strategy_data['first_roll_of_round'] = False
    
    sleep(1)
    print("y" if reroll_qm else "n")
    return reroll_qm

  def round_start(self):
    self.strategy_data['first_roll_of_round'] = True
