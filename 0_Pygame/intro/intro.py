import pygame
from sys import exit

size = width, height = (800, 400)
fps = 60

player_v = 0
g = 0.3

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = True


sky_surf = pygame.image.load('img/Sky.png').convert()
ground_surf = pygame.image.load('img/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64)) 
score_rect = score_surf.get_rect(center = (width/2, 50))

snail_surf = pygame.image.load('img/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800, 300))
 
player_surf = pygame.image.load('img/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300 and game_active:
                player_v = -8

            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                snail_rect.left = 800
                player_rect.bottom = 300
  
    if game_active:

        screen.blit(sky_surf, (0, 0)) 
        screen.blit(ground_surf, (0, 300)) 

        pygame.draw.rect(screen, '#c0e8ec', score_rect, 40)
        pygame.draw.rect(screen, '#c0e8ec', score_rect)

        player_rect.y += player_v
        player_v += g

        if player_rect.bottom > 300: player_rect.bottom = 300

        screen.blit(score_surf, score_rect)  
        
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)

        snail_rect.x -= 4 
        if snail_rect.right <= 0: snail_rect.left = 800

        if player_rect.colliderect(snail_rect):
            game_active = False

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print("Mus")
 
    else:
        screen.fill('Red')
         
    
    pygame.display .update()
    clock.tick(fps)
