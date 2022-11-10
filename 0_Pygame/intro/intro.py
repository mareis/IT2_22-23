from turtle import st
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'{current_time//1000:10}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

    return current_time//1000 

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for rect in obstacle_list:
            rect.x -= 5 

            if rect.bottom == 300: screen.blit(snail_surf, rect)
            else: screen.blit(fly_surf, rect)


        if obstacle_list[0].x < -  100:
            obstacle_list.pop(0)
            #print(obstacle_list[0].x)

             
    return obstacle_list
             
def collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player.colliderect(obstacle): return False

    return True

def player_animation():
    #global player_index  
    if player_rect.bottom < 300:
        return player_jump

    else:
        global player_index
        player_index += 0.1
        print(int(player_index))

        if player_index >= 2: player_index = 0
        return player_walk[int(player_index)]



size = width, height = (800, 400)
fps = 60 

player_v = 0
g = 0.3

score = 0 

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False
start_time = 0

sky_surf = pygame.image.load('img/Sky.png').convert()
ground_surf = pygame.image.load('img/ground.png').convert()

#score_surf = test_font.render('My game', False, (64,64,64)) 
#score_rect = score_surf.get_rect(center = (width/2, 50))


# Obsticales
snail_surf = pygame.image.load('img/snail/snail1.png').convert_alpha() 
fly_surf = pygame.image.load('img/fly/fly1.png').convert_alpha()

obstacle_rect_list = []



player_walk = [ 
    pygame.image.load('img/player/player_walk_1.png').convert_alpha(),
    pygame.image.load('img/player/player_walk_2.png').convert_alpha()
]
player_index = 0;
player_jump = pygame.image.load('img/player/jump.png').convert_alpha()


player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300)) 

#

player_stand = pygame.image.load('img/player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (width/2, height/2))

game_name_surf = test_font.render('Snail Run', False, (111,196,169)) 
game_name_surf = pygame.transform.rotozoom(game_name_surf, 0, 2)
game_name_rect = game_name_surf.get_rect(center = (width/2, 70))

game_message_surf = test_font.render('Press space to run', False, (111,196,169)) 
game_message_rect = game_message_surf.get_rect(center = (width/2, height-70))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_v = -8

            if event.type == obstacle_timer:
                if randint(0,2):obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900, 1100), 300)))
                else: obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900, 1100), 210)))


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                player_rect.bottom = 300
                start_time = pygame.time.get_ticks() 

            
  
    if game_active:
        screen.blit(sky_surf, (0, 0)) 
        screen.blit(ground_surf, (0, 300))  
        
        score = display_score()

        player_rect.y += player_v
        player_v += g

        if player_rect.bottom > 300: player_rect.bottom = 300

        player_surf = player_animation()
        screen.blit(player_surf, player_rect)

        
        # Obstacle movement 
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
         
        # Clollision
        game_active = collisions(player_rect, obstacle_rect_list)

        #screen.blit(snail_surf, snail_rect)
        #snail_rect.x -= 4 



        #if snail_rect.right <= 0: snail_rect.left = 800

        #if player_rect.colliderect(snail_rect):
            #game_active = False

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print("Mus")
 
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()

        player_rect.bottom = 300
        player_v = 0

        game_score_surf = test_font.render(f'Youre score: {score}', False, (111,196,169)) 
        game_score_rect = game_score_surf.get_rect(center = (width/2, height-70))

        screen.blit(game_name_surf, game_name_rect)

        if score == 0: screen.blit(game_message_surf, game_message_rect)
        else: screen.blit(game_score_surf, game_score_rect)

         
    
    pygame.display .update()
    clock.tick(fps)
