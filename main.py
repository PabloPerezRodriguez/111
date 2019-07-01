from fabulous.color import *
from player_selection import player_creation_loop
from menus import main_menu, options_menu, load_options, options
# from fabulous import fg256, bg256

import random
from time import sleep

def welcome():
  print(f'Welcome to {bold(red("111"))}, a {bold(yellow("python"))} implementation of a dice game')
  info_url = 'https://www.reddit.com/r/ProgrammingPrompts/comments/2mwokc/easybase_task_to_difficult_challengedice_game_111/'

  print(f'For instructions see {bold(underline(yellow(info_url)))}')

# Functions

def roll_die():
  return random.randint(1, 6)

# Game
def game(players):
  round_number = 1

  # Game loop
  while not any(player.score > options('winning_number') for player in players):
    print(bold(red(f'ROUND {(round_number)}')))
    sleep(2)

    # Player loop
    for p in players:
      print(f"It's {p.printable_name}'s turn")
      sleep(1)
      # Player round loop
      p.round_start()
      round_score = 0
      mandatory_re_roll = False
      last_roll = None
      while True:
        res = p.ask_to_re_roll(mandatory_re_roll, last_roll, round_score + p.score)
        mandatory_re_roll = False
        

        if res == True:
          player_roll = roll_die()
          print(f'You rolled a {bg256("orangered", player_roll)}')
          if player_roll == options('round_ending_number'):
            print(red('Because you rolled the score-voiding number, you lost all the points this round and your turn has ended'))
            round_score = 0
            break
          elif player_roll == options('mandatory_re_roll'):
            print(red('Because you rolled the mandatory re-roll number, you must re-roll'))
            mandatory_re_roll = True
          elif player_roll == options('no_re_roll'):
            print(red("Because you rolled the no re-roll number, you can't re-roll, so your turn has ended"))
            break
          else:
            round_score += player_roll
          last_roll = player_roll
        else:
          break
      
      p.score += round_score

      print(f"{p.printable_name} has finished their turn and they have a score of {bg256('orangered', p.score)}")
      p.round_end()

      if p.score >= options('winning_number'):
        break
    round_number += 1
  
  player_that_has_won = next(player for player in players if player.score > options('winning_number'))
  print(f'{player_that_has_won.printable_name} has won the game with a score of {bg256("orangered", p.score)}')

if __name__ == '__main__':
  welcome()
  load_options()
  while True:
    mm_selection = main_menu()
    if mm_selection == -1:
      break
    elif mm_selection == 0:
      players = player_creation_loop()
      game(players)
    elif mm_selection == 1:
      options_menu()


