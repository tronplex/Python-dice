import random

def dice_roll():
  sides = range(1,7)
  die01 = random.choice(sides)
  die02 = random.choice(sides)
  print("Die 1: " + str(die01))
  print("Die 2: " + str(die02))
  if die01 == die02:
    print("DOUBLES!")
    
dice_roll()
