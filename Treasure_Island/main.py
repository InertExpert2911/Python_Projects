print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")

response = input("Your mission, should you choose to find the treasure. Type 'Yes' or 'No' : ") 

if response.lower() == "yes":
  left_or_right = input("You enter the dungeon and the path is splitting into two. Type 'Left' or 'Right' : ")

  if left_or_right.lower() == "left":
    swim_goback = input("You see a pool of water. You wanna 'Swim' or 'Go Back'? : ")

    if swim_goback == "swim": 
      axe = input("You get to the other side safely and you see an axe. Would you like to pick it up? : ")

      if axe.lower() == "yes":
        kill = input("You move forward and you see a monstor !! 'Kill' or 'Escape'? : ")

        if kill.lower() == "kill":
          print("You kill the monstor and just ahead the path you see a chest of gold coins. You found the treasure !!!")
        else:
          print("The monstor kills you and you are dead. GAME OVER!!!!!")
    
      else:
        print("You move on. You see a monstor and the monstor kills you. Game Over!!!")

    else:
      print("On your way back, you were attacked by an animal and you are dead. GAME OVER !!!")

  else:
    print("You fall into a hole. Game Over !!!!")

else: 
  print(''' 
     _            _   _     
    | |          | | | |    
  __| | ___  __ _| |_| |__  
 / _` |/ _ \/ _` | __| '_ \ 
| (_| |  __/ (_| | |_| | | |
 \__,_|\___|\__,_|\__|_| |_|
 ''')

 # https://replit.com/@TharunReddy5/TreasureIsland#main.py