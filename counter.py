import pygame
import os
from config import pieceSize, padding


class Counter():
    def __init__(self):
        self.path = "assets/"
        self.counterImageLoad = pygame.image.load(os.path.join(
            self.path, "classic/", "counter.png"))
        self.counterImage = pygame.transform.scale(self.counterImageLoad, ((
            self.counterImageLoad.get_width() * pieceSize[0]) // self.counterImageLoad.get_height(), pieceSize[1]))

    def setDigitImage(self, digit):
        self.digit = digit
        self.digitImageLoad = pygame.image.load(
            os.path.join(self.path, "classic/", "counter" + digit + ".png"))
        self.digitImage = pygame.transform.scale(self.digitImageLoad, (self.digitImageLoad.get_width(
        ) * pieceSize[0] // self.digitImageLoad.get_height(), pieceSize[1] - 2))

        return self.digitImage


class TimeCounter(Counter):
    def convertInt(self, num):
        self.num = num

        if (self.num > 999):
            self.num = 999

        self.stringNum = str(num)

        if (num >= 0 and num <= 9):
            self.stringNum = "00" + self.stringNum
        elif (num >= 10 and num <= 99):
            self.stringNum = "0" + self.stringNum
        elif (num >= 100):
            pass

        return self.stringNum

    def drawDigits(self, surface, ticks, startTime):

        surface.blit(self.counterImage, (padding*2, padding))

        if (startTime == 0):
            ticks = 0

        self.seconds = int((ticks-startTime)/1000 % 60)
        self.digits = self.convertInt(self.seconds)

        for i in range(3):
            surface.blit(self.setDigitImage(
                self.digits[i]), (padding*2 + i * self.digitImage.get_width() + i*1, padding + 1))


class MineCounter(Counter):
    def convertInt(self, num):
        self.num = num

        if (self.num > 999):
            self.num = 999
        if (self.num < -99):
            self.num = -99

        self.stringNum = str(num)

        if (num >= 0 and num <= 9):
            self.stringNum = "00" + self.stringNum
        elif (num >= 10 and num <= 99):
            self.stringNum = "0" + self.stringNum
        elif (num < 0 and num >= -9):
            self.stringNum = list(self.stringNum)
            self.stringNum.append("")
            self.stringNum[2] = self.stringNum[1]
            self.stringNum[1] = "0"
        elif (num < -10 and num >= -99):
            pass

        return self.stringNum

    def drawDigits(self, surface, bombs):

        surface.blit(self.counterImage, (pygame.display.get_surface().get_size()[
            0]-padding*2-self.counterImage.get_width(), padding))

        self.digits = self.convertInt(bombs)

        for i in range(3):
            surface.blit(self.setDigitImage(self.digits[i]), (pygame.display.get_surface().get_size()[0]-padding*2-self.counterImage.get_width() + i *
                                                              self.digitImage.get_width() + i*1, padding + 1))
