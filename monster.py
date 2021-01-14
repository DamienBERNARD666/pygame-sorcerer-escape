import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("wizard")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load('assets/wizard.png')
        self.image = pygame.transform.scale(self.image, (128, 140))
        self.rect = self.image.get_rect()
        self.rect.x =  1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)
        self.start_animations()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.score += 100
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 2)

    def update_animations(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        bar_color = (111,210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
