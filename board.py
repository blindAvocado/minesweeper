import pygame
import random
from item import Coin, Life, Mine, Empty
from piece import Piece


class Board():
    def __init__(self, size, bombCount):
        self.numClicked = 0
        self.size = size
        self.bombCount = bombCount
        self.bombUserCount = bombCount
        self.startTime = 0

        self.setBoard()

    def setBoard(self):
        self.board = []

        for row in range(self.size[0]):
            self.board.append([])
            for col in range(self.size[1]):
                self.board[row].append(0)

        self.setMines()
        self.setNeighbors()
        self.setBonuses()
        self.setNeighbors()

        for row in self.board:
            print(row)

    # Расстановка мин
    def setMines(self):
        self.bombs = 0

        print("BOMB COUNT: ", self.bombCount)

        # заполнение поля минами
        while self.bombs < self.bombCount:
            x = random.randrange(0, self.size[0])
            y = random.randrange(0, self.size[1])
            if (self.board[x][y] == 0) and (self.bombs < self.bombCount):
                print(x, y)
                self.board[x][y] = Piece(Mine(), x, y)
                self.bombs += 1

        print("BOMBS PLACED: ", self.bombs)

        # заполнение оставшегося поля пустыми клетками
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if self.board[row][col] == 0:
                    self.board[row][col] = Piece(Empty(), row, col)

    # Расстановка соседей
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    # Расстановка бонусов
    def setBonuses(self):
        self.coins = 0
        self.lives = 0
        self.coinCount = (self.size[0] * self.size[1]) // 50
        self.lifeCount = (self.size[0] * self.size[1]) // 100
        print("COINS: ", self.coinCount)
        print("LIVES: ", self.lifeCount)

        # расстановка монет
        while self.coins < self.coinCount:
            x = random.randrange(0, self.size[0])
            y = random.randrange(0, self.size[1])
            piece = self.getPiece((x, y))
            if (self.coins < self.coinCount) and (not piece.getHasNum()) and (piece.getItem().getName().lower() == "empty"):
                self.board[x][y] = Piece(Coin(), x, y)
                self.coins += 1

        # расстановка жизней
        while self.lives < self.lifeCount:
            x = random.randrange(0, self.size[0])
            y = random.randrange(0, self.size[1])
            piece = self.getPiece((x, y))
            if (self.lives < self.lifeCount) and (not piece.getHasNum()) and (piece.getItem().getName().lower() == "empty"):
                self.board[x][y] = Piece(Life(), x, y)
                self.lives += 1

    # Вернуть список соседей
    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    # Вернуть объект Piece по указнному индексу
    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    # Вернуть статус победы
    def getWon(self):
        if ((self.size[0] * self.size[1]) - self.bombCount == self.numClicked):
            return True
        else:
            return False

    def getUserBombs(self):
        return self.bombUserCount

    def getStartTime(self):
        return self.startTime

    def handleClick(self, piece, flag, lost):

        if not lost:
            if (flag and not piece.getClicked()):
                if (piece.getFlagged()):
                    self.bombUserCount += 1
                else:
                    self.bombUserCount -= 1
                piece.toggleFlag()
                return

            if not piece.getClicked() and not piece.getFlagged():
                piece.click()
                self.numClicked += 1
                piece.getItem().action()
                if piece.getItem().getName().lower() == "mine":
                    return

                if self.numClicked == 1:
                    self.startTime = pygame.time.get_ticks()

                if piece.getNumAround() != 0:
                    return

                for neighbor in piece.getNeighbors():
                    if (not neighbor.getItem().getName().lower() == "mine" and not neighbor.getClicked()):
                        if (not neighbor.getItem().getName().lower() == "empty" and neighbor.getClicked()):
                            pass
                        else:
                            self.handleClick(neighbor, False, lost)
                return
