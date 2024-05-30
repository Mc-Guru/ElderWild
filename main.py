import pygame
import subprocess
import sys
from pygame.locals import *


class ElderWild:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('ElderWild')
        self.background_image = pygame.image.load('./src/bg.png').convert()
        self.background_image = self.scale_image(self.background_image, (self.screen_width, self.screen_height))

    def draw_text(self, text, color, surface, x, y):
        font = pygame.font.Font(None, 46)
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def scale_image(self, image, size):
        rect = image.get_rect()
        ratio = min(size[0] / rect.width, size[1] / rect.height)
        width = int(rect.width * ratio)
        height = int(rect.height * ratio)
        return pygame.transform.scale(image, (width, height))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.screen.blit(self.background_image, ((self.screen_width - self.background_image.get_width()) // 2,
                                                      (self.screen_height - self.background_image.get_height()) // 2))

            self.draw_text('Mise à jour terminée', (255, 255, 255), self.screen, self.screen_width // 2, self.screen_height // 2)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = ElderWild()
    game.run()
