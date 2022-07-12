import pygame
import random
from Settings import board
import time
pygame.init()

WIDTH, HEIGHT = 400,400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minesweeper Alex Addition')
screen.fill((0, 0, 0))
board1 = board(10, 12, 7, screen)
board1.draw()
Loser = ['Good Job, You Lost!', 'You do know that you dont click the bombs...right...?', 'Loser', 'Defeat', 'You have died...']





while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    

    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        pos = pygame.mouse.get_pos()
        for t in range(len(board1.board)):
          for g in range(len(board1.board[t])):
            if board1.board[t][g].rect.collidepoint(pos) and board1.board[t][g].flag == False and board1.board[t][g].hide == False:
              print(t, g)
              if board1.board[t][g].bomb == True:
                board1.board[t][g].hide = True
                board1.draw()
                pygame.display.flip()
                time.sleep(1)
                pygame.quit()
                print(Loser[random.randint(0, 4)])
              else:
                board1.pick(t, g)
                board1.draw()
                #print(pos)
              
               
                
                
          
      if event.button == 3:
        pos = pygame.mouse.get_pos()
        for t in board1.board:
          for g in t:
            if g.rect.collidepoint(pos):
              g.flag ^= True
              print(g.flag)
              board1.draw()
              #print(pos)

    
              
    


  pygame.display.flip()
