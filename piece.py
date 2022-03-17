class Piece():
    def __init__(self, item, row, col):
        self.clicked = False
        self.flagged = False
        self.item = item
        self.row = row
        self.col = col
        self.numAround = 0

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def getHasNum(self):
        if self.numAround > 0:
            return True
        else:
            return False

    def getItem(self):
        return self.item

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if (piece.getItem().getName().lower() == 'mine'):
                self.numAround += 1

    def getNeighbors(self):
        return self.neighbors

    def getNumAround(self):
        return self.numAround

    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def draw(self, surface, lost):
        self.item.draw(self.numAround, self.clicked, self.flagged,
                       lost, self.row, self.col, surface)

    def __repr__(self):
        return f'{type(self.item).__name__}, ({self.row}, {self.col})'
