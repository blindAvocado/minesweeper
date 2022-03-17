import pygame
from board import Board
from counter import TimeCounter, MineCounter
from button import Restart
from config import padding, pieceSize, screenSize


class Game():
    def __init__(self, boardSize, bombCount):
        self.boardSize = boardSize
        self.bombCount = bombCount
        self.board = Board(self.boardSize, self.bombCount)
        self.screen = pygame.display.set_mode(screenSize)
        self.playerLives = 1
        self.coins = 0
        self.lost = False
        self.won = False

    def run(self):
        self.screen.fill((192, 192, 192))

        pygame.init()
        self.clock = pygame.time.Clock()

        self.timeCounter = TimeCounter()
        self.mineCounter = MineCounter()

        self.restartBtn = Restart(self.screen)

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    self.rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(self.position, self.rightClick)
                if event.type == pygame.USEREVENT+0:
                    print(event.value)
                    if event.value == "MINE":
                        # print(self.playerLives)
                        self.playerLives -= 1
                        # print(self.playerLives)
                        self.checkLost()
                    if event.value == "COIN":
                        # self.coins += 1
                        pass
                    if event.value == "LIFE":
                        # self.playerLives += 1
                        pass
                if event.type == pygame.USEREVENT+1:
                    if event.value == "RESET":
                        self.playerLives = 1
                        self.lost = False
                        self.won = False
                        self.board.__init__(self.boardSize, self.bombCount)

            self.ticks = pygame.time.get_ticks()
            self.drawPieces()
            self.restartBtn.update(
                self.screen, self.lost, self.won, self.board)

            if (self.board.getWon()):
                self.won = True
                self.lost = False

            if (not self.lost and not self.won):
                self.timeCounter.drawDigits(
                    self.screen, self.ticks, self.board.getStartTime())
                self.mineCounter.drawDigits(
                    self.screen, self.board.getUserBombs())

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

    def handleClick(self, position, rightClick):
        if not self.won:
            self.index = (position[1] - (pieceSize[1] + padding * 2)
                          ) // pieceSize[1], position[0] // pieceSize[0]
            if not ((self.index[0] or self.index[1]) < 0):
                self.piece = self.board.getPiece(self.index)
                self.board.handleClick(self.piece, rightClick, self.lost)

    def drawPieces(self):
        for row in range(self.boardSize[0]):
            for col in range(self.boardSize[1]):
                self.piece = self.board.getPiece((row, col))
                self.piece.draw(self.screen, self.lost)

    def checkLost(self):
        if self.playerLives < 1:
            self.lost = True
            self.won = False
