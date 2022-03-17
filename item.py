import pygame
import os
from config import pieceSize, padding, theme


class Item():
    def __init__(self):
        self.path = "assets/"
        self.imageLoad = pygame.image.load(os.path.join(self.path,
                                                        theme, "piece/", "closed.png"))
        self.image = pygame.transform.scale(self.imageLoad, pieceSize)

    def getName(self):
        return type(self).__name__

    def draw(self, num, clicked, flagged, lost, row, col, surface):
        if not clicked:
            if flagged:
                self.imageLoad = pygame.image.load(os.path.join(
                    self.path, theme, "piece/", "flag.png"))
            else:
                self.imageLoad = pygame.image.load(os.path.join(self.path,
                                                                theme, "piece/", "closed.png"))
        if clicked:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", type(self).__name__.lower() + ".png"))

        self.image = pygame.transform.scale(self.imageLoad, pieceSize)
        surface.blit(
            self.image, (col * pieceSize[0], row * pieceSize[1] + (pieceSize[1] + padding * 2)))

    def action(self):
        itemAction = pygame.event.Event(
            pygame.USEREVENT+0, value=type(self).__name__.upper())
        pygame.event.post(itemAction)


class Mine(Item):
    def __init__(self):
        super().__init__()

    def draw(self, num, clicked, flagged, lost, row, col, surface):
        super().draw(num, clicked, flagged, lost, row, col, surface)

        if clicked:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", type(self).__name__.lower() + "_red.png"))
        if (not clicked and not flagged and lost):
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", type(self).__name__.lower() + ".png"))

        self.image = pygame.transform.scale(self.imageLoad, pieceSize)
        surface.blit(self.image, (col *
                                  pieceSize[0], row * pieceSize[1] + (pieceSize[1] + padding * 2)))


class Coin(Item):
    def __init__(self):
        super().__init__()


class Life(Item):
    def __init__(self):
        super().__init__()


class Empty(Item):
    def __init__(self):
        super().__init__()

    def draw(self, num, clicked, flagged, lost, row, col, surface):
        if not clicked:
            if flagged:
                self.imageLoad = pygame.image.load(os.path.join(
                    self.path, theme, "piece/", "flag.png"))
            if flagged and lost:
                self.imageLoad = pygame.image.load(os.path.join(
                    self.path, theme, "piece/", "flag_red.png"))
            if not flagged:
                self.imageLoad = pygame.image.load(os.path.join(self.path,
                                                                theme, "piece/", "closed.png"))
        if clicked:
            self.imageLoad = pygame.image.load(os.path.join(
                self.path, theme, "piece/", str(num) + ".png"))

        self.image = pygame.transform.scale(self.imageLoad, pieceSize)
        surface.blit(self.image, (col *
                                  pieceSize[0], row * pieceSize[1] + (pieceSize[1] + padding * 2)))

    def action(self):
        pass
