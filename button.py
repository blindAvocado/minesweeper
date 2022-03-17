import pygame
import os
from config import padding, pieceSize, theme


class Button():
    def __init__(self, surface):
        self.surface = surface
        self.path = "assets/"
        self.pressed = False

    def draw(self, surface, lost, won):
        pass

    def action(self, board):
        pass

    def update(self, surface, lost, won, board):
        self.draw(surface, lost, won)
        self.action(board)


class Restart(Button):
    def __init__(self, surface):
        super().__init__(surface)
        self.imageLoad = pygame.image.load(os.path.join(
            self.path, theme, "piece/", "main-btn-default.png"))
        self.image = pygame.transform.scale(self.imageLoad, pieceSize)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pygame.display.get_surface(
        ).get_width() // 2 - self.image.get_width() // 2, padding)

    def draw(self, surface, lost, won):
        if self.pressed:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", "main-btn-default-pressed.png"))
        else:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", "main-btn-default.png"))
        if lost:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", "main-btn-lost.png"))
        if won:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", "main-btn-won.png"))

        self.image = pygame.transform.scale(self.imageLoad, pieceSize)
        surface.blit(
            self.image, (pygame.display.get_surface().get_width() // 2 - self.image.get_width() // 2, padding))

    def action(self, board):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    # board.setBoard()
                    buttonAction = pygame.event.Event(
                        pygame.USEREVENT+1, value="RESET")
                    pygame.event.post(buttonAction)
                    self.pressed = False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
