import  os, random, keyboard, time

clear = lambda: os.system('cls')

keys = ['w','s','esc']

pressed = []

score = 0

barrier = []

coins = []

class Player:
   char = 8
   x_pos= 0
   y_pos= 0

x = Player.x_pos
y = Player.y_pos

class Board:
   def position(dict,x,y):
      count = 0
      clear()
      del dict
      dict = [['_','_','_','_','_','_'],['_','_','_','_','_','_'],['_','_','_','_','_','_'],['_','_','_','_','_','_'],['Score is: %s' %(score)]]
      dict[x][y] = Player.char
      for Barrier in barrier:
         if Barrier.y < 0:
            barrier.remove(Barrier)
         else:
            dict[Barrier.x][Barrier.y] = Barrier.char
      for Coin in coins:
         if Coin.y < 0:
            coins.remove(Coin)
         else:
            dict[Coin.x][Coin.y] = Coin.char
      while count <= 4:
         print(*dict[count], sep=' ')
         count += 1

class press:
    def __init__(self, key):
        self.key = keyboard.add_hotkey(key, lambda: [pressed.append(key), print(key)]) 

for key in keys:
   press(key)

class Barrier:
      def __init__(self):
         self.x = random.randint(0,3)
         self.y = 5
         self.char = 1
      
class Coin:
      def __init__(self):
         self.x = random.randint(0,3)
         self.y = 5
         self.char = 0
   
class Collision:
      def check(score,x,y):
         for Barrier in barrier:
            for Coin in coins:

               c = Coin.x, Coin.y
               b = Barrier.x, Barrier.y
               p = x, y
               if c == b:
                  barrier.remove(Barrier)
               elif b == p:
                  print("Game Over!")
                  exit()
               elif c == p:
                  scored = True
                  return scored
while True:                 
   class Barrier:
      def __init__(self):
         self.x = random.randint(0,3)
         self.y = 5
         self.char = 1
      
   class Coin:
      def __init__(self):
         self.x = random.randint(0,3)
         self.y = 5
         self.char = 0
   
   while len(barrier) <= 2:
      barrier.append(Barrier())
      
   while len(coins) <= 0:
      coins.append(Coin())

   Board.position(dict,x,y)
   
   s = Collision.check(score,x,y) 
   
   if s == True:
      score += 1
   

   for Barrier in barrier:
      Barrier.y -= 1

   for Coin in coins:
      Coin.y -= 1
   
   if 'w' in pressed:
      x -= 1
      if x >= 4 or x < 0:
         x = 0
      pressed.clear()
      
   if 's' in pressed:
      x += 1
      if x >= 4 or x < 0:
         x = 0
      pressed.clear()
      
   if 'esc' in pressed:
      break
   
   Board.position(dict,x,y)
   time.sleep(0.8)
