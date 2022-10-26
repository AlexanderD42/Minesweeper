import pygame
import random
import time

class tile: 
  bombs = 0
  def __init__(self, y, x):
    self.rect = pygame.Rect(x*board.screen.get_width()/board.column, y*board.screen.get_height()/board.row, board.screen.get_width()/board.column, board.screen.get_height()/board.row)
    self.bomb = False
    self.number = 0
    self.flag = False
    self.hide = False
    self.tile = pygame.image.load('CoveredTile.png')
    self.tile = pygame.transform.scale(self.tile, (self.rect.right-self.rect.left, self.rect.bottom-self.rect.top))
    self.tileRect = self.tile.get_rect()
    self.tileRect.topleft = self.rect.topleft
    self.bombIMG = pygame.image.load('Bomb.png')
    self.bombIMG = pygame.transform.scale(self.bombIMG, (self.rect.right-self.rect.left, self.rect.bottom-self.rect.top))
    self.bombRect = self.bombIMG.get_rect()
    self.bombRect.topleft = self.rect.topleft
    self.flagIMG = pygame.image.load('Flag.png')
    self.flagIMG = pygame.transform.scale(self.flagIMG, (self.rect.right-self.rect.left, self.rect.bottom-self.rect.top))
    self.flagRect = self.flagIMG.get_rect()
    self.flagRect.topleft = self.rect.topleft
    self.font = pygame.font.SysFont('timesnewroman', 30)
    

  def draw(self):
    if self.hide == True:
      pygame.draw.rect(board.screen, (255, 255, 255), self.rect)
    if self.bomb:
      board.screen.blit(self.bombIMG,  self.bombRect)

    else:
      if self.number > 0:
        textRect = self.rect
        textRect.x += 15
        board.screen.blit(self.font.render (str(self.number), True, (0, 0, 0)), textRect)
        self.rect.x -= 15
        
    if self.hide == False:

      board.screen.blit(self.tile,  self.tileRect)

    if self.flag:
      board.screen.blit(self.flagIMG,  self.flagRect)


    


class board:
  
  def __init__(self, column, row, bombs, screen):
    board.column = column
    board.row = row
    self.bombs = bombs
    board.screen = screen
    self.Count = (board.row*board.column)-self.bombs
    
 
          
     
  
    self.board = []
    for i in range(row):
      self.board.append([])
      for j in range(column):
        
        self.board[i].append(tile(i, j))
        
    bombsPlaced = bombs

    while bombsPlaced > 0:
      #print(bombsPlaced)
      # Adds all bombs and updates the numbers
      for h in range(row):
        for k in range(column):
          if bombsPlaced > 0:

            if random.randint(0, 35) == 1 and self.board[h][k].bomb == False:
              
              self.board[h][k].bomb = True
              self.UpdateNumbers(h, k)
              
              tile.bombs += 1
              bombsPlaced -= 1
              
    
    print(tile.bombs)
  #def bombs(self, row, column, bombs):
       # self.board = []
    #if row >= 0 and column >=0 and row < self.row and column < self.column:
      
    
  def UpdateNumbers(self, row, column):
        
    if row >= 0 and column >=0 and row < self.row and column < self.column:
          
      value = self.board[row][column].bomb
      
    else:

      return


    if value:
      self.UpdateNumbers(row-1, column)
      self.UpdateNumbers(row+1, column)
      self.UpdateNumbers(row, column-1)
      self.UpdateNumbers(row, column+1)
      self.UpdateNumbers(row-1, column-1)
      self.UpdateNumbers(row-1, column+1)
      self.UpdateNumbers(row+1, column+1)
      self.UpdateNumbers(row+1, column-1)
      print('bomb updated')

    else:
      self.board[row][column].number += 1
      return 1
          
      
        



  def draw(self):
    for h in self.board:
        for k in h:
          k.draw()

  def pick(self, row, column):  
    #print(row, column)
    
    if row >= 0 and column >=0 and row < self.row and column < self.column:
      value = self.board[row][column].number
      
    else:
      return

    if value > 0 and not self.board[row][column].hide:
      #print(self.Count)
      self.board[row][column].hide = True
      self.Count -=1
      if self.Count == 0:
        print('you have won')
        pygame.quit()
      return 1
   
    elif value == 0 and not self.board[row][column].hide:
      self.board[row][column].hide = True
      self.draw()
      pygame.display.update()
      self.Count -=1
      self.pick(row-1, column-1)
      self.pick(row-1, column)
      self.pick(row+1, column+1)
      self.pick(row, column-1)
      self.pick(row, column+1)
      self.pick(row+1, column-1)
      self.pick(row+1, column)
      self.pick(row+1, column+1)
     






      

