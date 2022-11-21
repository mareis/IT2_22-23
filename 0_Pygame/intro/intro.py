import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk = [ 
            pygame.image.load('img/player/player_walk_1.png').convert_alpha(),
            pygame.image.load('img/player/player_walk_2.png').convert_alpha()
        ]
        self.player_index = 0;
        self.player_jump = pygame.image.load('img/player/jump.png').convert_alpha()

        self.image =  self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.v = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.v = -8
            self.jump_sound.play() 

    def apply_gravity(self):
        self.v += g
        self.rect.y += self.v
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump

        else:
           self.player_index += 0.1
           if self.player_index >= len(self.player_walk):self.player_index = 0
           self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()  
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            self.frames = [
                pygame.image.load('img/fly/fly1.png').convert_alpha(),
                pygame.image.load('img/fly/fly2.png').convert_alpha()
            ]
            y_pos = 210
        
        else:
            self.frames = [
                pygame.image.load('img/snail/snail1.png').convert_alpha(),
                pygame.image.load('img/snail/snail2.png').convert_alpha() 
            ]
            y_pos = 300


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

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
             
def collision():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        return False

    return True


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

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


sky_surf = pygame.image.load('img/Sky.png').convert()
ground_surf = pygame.image.load('img/ground.png').convert()


player_stand = pygame.image.load('img/player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (width/2, height/2))

game_name_surf = test_font.render('Snail Run', False, (111,196,169)) 
game_name_surf = pygame.transform.rotozoom(game_name_surf, 0, 2)
game_name_rect = game_name_surf.get_rect(center = (width/2, 70))

game_message_surf = test_font.render('Press space to run', False, (111,196,169)) 
game_message_rect = game_message_surf.get_rect(center = (width/2, height-70))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) 

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500) 

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200) 



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
    
                start_time = pygame.time.get_ticks() 

             
    if game_active:
        screen.blit(sky_surf, (0, 0)) 
        screen.blit(ground_surf, (0, 300))  
        
        score = display_score()
        
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()


        # Collision
        game_active = collision()

 
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        #obstacle_rect_list.clear()

        #player_rect.bottom = 300
        player_v = 0

        game_score_surf = test_font.render(f'Youre score: {score}', False, (111,196,169)) 
        game_score_rect = game_score_surf.get_rect(center = (width/2, height-70))

        screen.blit(game_name_surf, game_name_rect)

        if score == 0: screen.blit(game_message_surf, game_message_rect)
        else: screen.blit(game_score_surf, game_score_rect)

          
    pygame.display .update()
    clock.tick(fps)
