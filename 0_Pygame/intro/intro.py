import pygame
from sys import exit

size = width, height = (800, 400)
fps = 60

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('img/Sky.png').convert()
ground_surf = pygame.image.load('img/ground.png').convert()

score_surf = test_font.render('My game', False, 'black') 
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
 
    screen.blit(sky_surf, (0, 0)) 
    screen.blit(ground_surf, (0, 300)) 
    screen.blit(score_surf, score_rect)
    
    
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    snail_rect.x -= 4 
    if snail_rect.right <= 0: snail_rect.left = 800

    if player_rect.colliderect(snail_rect):
        print("Kol")

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print("Mus")
 
    
    pygame.display .update()
    clock.tick(fps)
