import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x =  1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.velocity = random.randint(2, 4)
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


class Wizard(Monster):

    def __init__(self, game):
        super().__init__(game, "wizard", (130, 130))


class Wraith(Monster):

    def __init__(self, game):
        super().__init__(game, "wraith", (300, 300), 190)
        self.health = 250
        self.max_health = 250
        self.attack = 10

