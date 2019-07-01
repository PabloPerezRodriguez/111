from Player import Player
from computer_player import ComputerPlayer
from fabulous.color import bold, magenta, white, underline
import random

def create_player(player_number):
  while True:
    name = input(f'How is {bold(magenta(f"Player {player_number}"))} called? ')
    if name == '':
      print(f'The name {bold(white(underline("CANNOT")))} be empty')
    else:
      return Player(name)

def create_cpu(cpu_number):
  return ComputerPlayer(f'CPU {cpu_number}')

def player_creation_loop():
  n_humans_int = None
  n_AIs_int = None
  while True:
      while True:
        n = input('How many people are playing? ')
        try:
          n_humans_int = int(n)
          break
        except ValueError:
          print('Please enter an integer')
      
      while True:
        n = input('How many computer players do you want to play with? ')
        try:
          n_AIs_int = int(n)
          break
        except ValueError:
          print('Please enter an integer')
      if (n_humans_int + n_AIs_int) < 2:
        print('A minimum of 2 players are needed to play this game')
      else:
        break
  
  every_player = [create_player(i) for i in range(1, n_humans_int+1)] + [create_cpu(i) for i in range(1, n_AIs_int+1)]
  random.shuffle(every_player)
  return every_player
    