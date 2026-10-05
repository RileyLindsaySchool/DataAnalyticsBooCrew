import random
import time
from google.colab import output
import matplotlib.pyplot as plt
from PIL import Image

  
#create a function that will allow the user to exit the game whenever they want
def earlyExit():
    print("Too bad.  Game over. "+playerName+" is a scared wimp. Goodbye!")
    input("Hit enter to continue\n")

#create a function that starts the game
def start():
  print("Welcome to the Haunted House.  A text-based game created in BDA 3003")
  global playerName
  im = Image.open('/content/haunted house image.png')
  plt.axis('off')
  plt.imshow(im)
  plt.axis('off')
  plt.imshow(im)
  plt.show()
  time.sleep(1)
  print("\n")
  playerName=input("What is your name? \n")
  global hasKey
  hasKey = "n"
  porch()  

def porch():
  output.clear()
  print("""Late one night, you are driving down a dirt road in a deserted area.
  Suddenly, your car breaks down. You try several times unsuccessfully to restart you car.
  You have no cellphone service.  A storm is approaching.
  You see a house in the distance and run there to take shelter.
  You find yourself on the front porch of a rather scary house.
  It has broken windows and an overall sinister feel.""")
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(250, 490, playerName, fontsize=10, color='red')
  plt.show() 
  enterHouse()

def enterHouse():
  b=input("Do you want to enter the house "+playerName+"? (Enter yes or no)\n")
  if b=="yes":
    entryway()
  elif b=="no":
    earlyExit()
  else:
    print("Not a valid response.") 
    enterHouse()

def entryway():
  output.clear()
  print("""You are in the entry way of the house. There are cobwebs in the corner.
  Red rum is written on the wall in what appears to be blood.
  There is a passageway to the north and another to the east.""")
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(250, 420, playerName, fontsize=10, color='red')
  plt.show() 
  whichDirection1()
  
def whichDirection1():
  c=input(playerName+", do you want to go north, east, or quit""? (Type north, east, or quit)\n")
  if c=="north":
    kitchen()
  elif c=="east":
    livingroom()
  elif c=="quit":
    earlyExit()
  else:
    print("Not a valid response.") 
    whichDirection1()


def kitchen():
  output.clear()
  print("""   You are in the kitchen.  All the surfaces are covered with pots, pans, food pieces, and pools of blood. 
  You think you hear something up the stairs that go to the west side of the room.
  It's a scraping noise, like something being dragged along the floor.
  On the counter there are three boxes of cereal, a clean bowl, and a clean spoon.""")
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(250, 250, playerName, fontsize=10, color='red')
  plt.show() 
  whichDirection2()
  
def whichDirection2():
  c=input(playerName+", do you want to go south, east, eat some cereal, or quit""? (Type south, east, cereal, or quit)\n")
  if c=="south":
    entryway()
  elif c=="east":
    diningroom()
  elif c=="cereal":
    cereal()
  elif c=="quit":
    earlyExit()
  else:
    print("Not a valid response.") 
    whichDirection2()


def cereal():
  output.clear()
  print("""  There is Count Chocula, Franken Berry, and Boo Berry. """)
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(250, 250, playerName, fontsize=10, color='red')
  plt.show() 
  whichCereal()


def whichCereal():
  c=input(playerName+", do you want to eat Count Chocula, Franken Berry, Boo Berry, or have you changed your mind""? (Type count, franken, boo, or nevermind)\n")
  if c=="count":
    print(playerName+" enjoyed some Count Chocula cereal.")
  elif c=="franken":
    print("A highly venomous spider comes out of the cereal box and bites "+playerName+".  "+playerName+" is dead. Game over.")
    input("Hit Enter to continue\n")
  elif c=="boo":
    global hasKey
    if hasKey == "n":
      print("There was a key inside the cereal box. "+playerName+" takes it.")
      hasKey = "y"
    else:
      print(playerName+" enjoyed some Boo Berry cereal.")
    input("Hit Enter to continue\n")
    kitchen()
  elif c=="nevermind":
    kitchen()
  else:
    print("Not a valid response.") 
    whichCereal()  


def diningroom():
  output.clear()
  print("""   You are in the dining room.  There is the fresh remains of dinner on a table. 
  You don't know what it is and your not sure you want to know.
  You hear what sounds like a distant scream.  """)
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(600, 200, playerName, fontsize=10, color='red')
  plt.show() 
  whichDirection3()


def whichDirection3():
  c=input(playerName+", do you want to go south, west, or quit""? (Type south, west, or quit)\n")
  if c=="south":
    livingroom()
  elif c=="west":
    kitchen()
  elif c=="quit":
    earlyExit()
  else:
    print("Not a valid response.") 
    whichDirection3()


def livingroom():
  output.clear() 
  print("""   You are in the living room.  The photos on the wall seem to be staring at you. 
  You feel a cold breeze and light in the room seems to change.
  There something wrapped in a blanket in the corner, about the size of a person.  """)
  im = Image.open('/content/hh floor plan.bmp')
  plt.axis('off')
  plt.imshow(im) 
  plt.text(500, 400, playerName, fontsize=10, color='red')
  plt.show() 
  R = random.choice([1,2,3,4,5,6,7,8,9,10])
  if R<7:
     whichDirection4()
  elif R>7:
     
     print("Something attacks from out of the shadows.  "+playerName+" is dead. Game over.")
     input("Hit Enter to Continue")
  elif R==7:
     
     print("You see something you didn't see at first: a bag in the corner.  \n A note on the bag: says "+playerName+" take this money leave and never tell anyone about this house or come back. \n You open the bag and find thousands of hundred dollar bills. \n You quickly leave the house walk 20 miles through the rain and escape with the money.")
     input("Hit Enter to Continue")

def whichDirection4():
  c=input(playerName+", do you want to go north, west, or quit""? (Type north, west, or quit)\n")
  if c=="north":
    diningroom()
  elif c=="west":
    entryway()
  elif c=="quit":
    earlyExit()
  else:
    print("Not a valid response.") 
    whichDirection4()


start()