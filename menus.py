# Optional stuff. Options menu. Save options
import json
from os.path import exists
from PyInquirer import prompt

def is_num(str):
  try:
    int(str)
    return True
  except ValueError:
    return False

options_ = {}

def options(s):
  return options_[s]

def load_options():
  global options_
  if exists('options.json'):
    with open('options.json') as f:
      options_ = json.load(f)
  else:
    reset_default_options()

def reset_default_options():
  global options_
  options_ = {
    "winning_number": 111,
    "round_ending_number": 1,
    "mandatory_re_roll": False,
    "no_re_roll": False
  }
  save_options()

def save_options():
  json.dump(options_, open('options.json', 'w'))

def options_menu():
  while True:
    selected_option = prompt(
      questions = [{
        'type': 'list',
        'qmark': '🛠 ',
        'message': 'Customize the game!',
        'name': 'options',
        'choices': [ 
          {
            'name': f'Winning number ({options("winning_number")})',
            'value': 0
          },
          {
            'name': f'Round-ending number ({options("round_ending_number")})',
            'value': 1,
          },
          {
            'name': f'Mandatory re-roll ({options("mandatory_re_roll") if options("mandatory_re_roll") else "Not Active"})',
            'value': 2,
          },
          {
            'name': f'No re-roll ({options("no_re_roll") if options("no_re_roll") else "Not Active"})',
            'value': 3
          },
          {
            'name': 'Done',
            'value': -1,
          }
        ]
      }
    ])['options']
    
    if selected_option == -1:
      break
    elif selected_option == 0:
      winning_number_selection_menu()
    elif selected_option == 1:
      round_ending_number_selection_menu()
    elif selected_option == 2:
      mandatory_re_roll_selection_menu()
    elif selected_option == 3:
      no_re_roll_selection_menu()
  
  save_options()

# Options sub menus
def winning_number_selection_menu():
  winning_number = prompt({
    'type': 'input',
    'name': 'winning_number',
    'message': "Write the winning number you'd like:",
    'default': '111',
    'validate': lambda s: is_num(s) or 'Please enter a number'
  })['winning_number']
  options_['winning_number'] = int(winning_number)

def round_ending_number_selection_menu():
  round_ending_number = prompt({
    'type': 'input',
    'name': 'round_ending_number',
    'message': "Write the round-ending number you'd like:",
    'default': '1',
    'validate': lambda s: (is_num(s) and int(s) >= 1 and int(s) <= 6) or 'Please enter a valid number (1-6)'
  })['round_ending_number']
  options_['round_ending_number'] = int(round_ending_number)

def mandatory_re_roll_selection_menu():
  mandatory_re_roll = prompt({
    'type': 'confirm',
    'name': 'mandatory_re_roll',
    'message': "Would you like to activate mandatory re-roll?",
    'default': False
  })['mandatory_re_roll']
  options_['mandatory_re_roll'] = mandatory_re_roll

  if mandatory_re_roll:
    mandatory_re_roll_value = prompt({
      'type': 'input',
      'name': 'mandatory_re_roll_value',
      'message': "Which number would you like to be the mandatory re-roll number?",
      'default': '4',
      'validate': lambda s: (is_num(s) and int(s) >= 1 and int(s) <= 6) or 'Please enter a valid number (1-6)'
    })['mandatory_re_roll_value']
    options_['mandatory_re_roll'] = int(mandatory_re_roll_value)

def no_re_roll_selection_menu():
  no_re_roll = prompt({
    'type': 'confirm',
    'name': 'no_re_roll',
    'message': "Would you like to activate no re-roll?",
    'default': False
  })['no_re_roll']
  options_['no_re_roll'] = no_re_roll

  if no_re_roll:
    no_re_roll_value = prompt({
      'type': 'input',
      'name': 'no_re_roll_value',
      'message': "Which number would you like to be the no re-roll number?",
      'default': '2',
      'validate': lambda s: (is_num(s) and int(s) >= 1 and int(s) <= 6) or 'Please enter a valid number (1-6)'
    })['no_re_roll_value']
    options_['no_re_roll'] = int(no_re_roll_value)



def main_menu():
  res = prompt(
    questions = [{
      'type': 'list',
      'qmark': '🕹 ',
      'message': 'Main menu',
      'name': 'main_menu',
      'choices': [ 
        {
          'name': 'Start game',
          'value': 0
        },
        {
          'name': 'Customize the game',
          'value': 1
        },
        {
          'name': 'Quit',
          'value': -1
        }
      ]
    }
  ])['main_menu']
  return res
