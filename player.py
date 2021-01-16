import pygame
from projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 480

    def update_animation(self):
        self.animate()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
            self.game.score -= 10
            if self.game.score <= 0:
                self.game.score = 0
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x + 20, self.rect.y + 40, self.health, 5]
        back_bar_position = [self.rect.x + 20, self.rect.y + 40, self.max_health, 5]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animations()

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
            self.load_animation("assets/run", [7,7,7])

    def move_left(self):
        self.rect.x -= self.velocity

