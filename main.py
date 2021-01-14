import pygame
import math
from game import Game


pygame.init()
clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("La fuite du sorcier")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/Background.png')
background = pygame.transform.scale(background, (2435, 1027))
bg_x = 0
bg_width = background.get_width()

my_font = pygame.font.SysFont("Times New Roman", 18)


banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 50))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = math.ceil(screen.get_height() / 3)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (200, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


game = Game()
running = True


def redraw_window():
    screen.blit(background, (bg_x, -300))  # draws our first bg image
    screen.blit(background, (bg_width, -300))  # draws the seconf bg image
    score_display = my_font.render('Score: ' + str(game.score), True, (255, 255, 255))
    screen.blit(score_display, (0, 0))


while running:
    clock.tick(FPS)
    bg_x -= 1.4
    bg_width -= 1.4
    if bg_x < background.get_width() * -1:
        bg_x = background.get_width()
    if bg_width < background.get_width() * -1:
        bg_width = background.get_width()
    redraw_window()

    if game.is_playing:
        game.launch_game(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
