import sys, pygame
import time
import random
import copy
scale = 10
pygame.init()
apple_pos = pygame.Rect(200,200,scale,scale)
apple_pos.right = (random.randint(1,59) * scale)
apple_pos.top = (random.randint(1,59) * scale)
speed = 1/15
size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0
player_color = pygame.Color(255, 255, 255)
player = [pygame.Rect(20,20,scale,scale), pygame.Rect(15,20,scale,scale),pygame.Rect(10,20,scale,scale),pygame.Rect(5,20,scale,scale), pygame.Rect(-5,20,scale,scale),pygame.Rect(-10,20,scale,scale)]
direction = 'd'
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
def waitframe():
    a = time.time()
    b = a
    while b-a < 1/30: b = time.time()
    

def draw_player(player):
    for node in player:
        pygame.draw.rect(screen, (255, 255, 255), node)

def move_player(player, direction):
    
    for i in range(len(player) -1,0,-1):
        
        player[i].right = player[i-1].right
        player[i].top = player[i-1].top
        if player[i].right > 600: sys.exit()
        if player[i].right < 0: sys.exit()
        if player[i].top > 590: sys.exit()
        if player[i].top < 0: sys.exit()   
    if direction == 'd': player[0].right +=scale
    if direction == 'a': player[0].right -=scale
    if direction == 's': player[0].top +=scale
    if direction == 'w': player[0].top -=scale
    check_death(player)

def handle_input(direction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and direction !='a':
                direction = 'd'
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction !='d':
                direction = 'a'
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN)and direction !='w':
                direction = 's'
            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and direction !='s':
                direction = 'w'
    return direction
def apple(player, apple_pos, direction):
   
    for node in player:
        if apple_pos.colliderect(node):            
            apple_pos.right = (random.randint(1,59) *scale)
            apple_pos.top = (random.randint(1,59) * scale)

            player.append(copy.copy(player[-1]))
            player.append(copy.copy(player[-1]))
            player.append(copy.copy(player[-1]))
    pygame.draw.rect(screen, (255, 0, 0), apple_pos)
    return player, apple_pos

def check_death(player):
    for i  in range (1,len(player)):
        if player[i].colliderect(player[0]): sys.exit()
        if player[0].colliderect(player[i]): sys.exit()

while 1:
    
    screen.fill(black)
    direction = handle_input(direction)
    move_player(player, direction)
    check_death(player)
    waitframe()

    
    player, apple_pos = apple(player, apple_pos,direction)
    waitframe()
    draw_player(player)    
    pygame.display.flip()
    check_death(player)
  