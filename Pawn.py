import Chessman
class Pawn(Chessman.Chessman):

    def __init__(self, board, ln, team):
        self.ln = ln
        self.board = board
        self.firstMove = True
        self.team = team
        self.availableMoves()
    def die(self):
        del self

    def availableMoves(self):
        self.am = []
        if self.firstMove:
            if self.ln[0] + str(int(self.ln[1]) + 2) in self.board.field.keys():
                if self.board.field[self.ln[0] + str(int(self.ln[1]) + 2)] == None:
                    self.am.append(self.ln[0] + str(int(self.ln[1]) + 2))
        if self.ln[0] + str(int(self.ln[1]) + 1) in self.board.field.keys():
            if self.board.field[self.ln[0] + str(int(self.ln[1]) + 1)] == None:
                self.am.append(self.ln[0] + str(int(self.ln[1]) + 1))
        if chr(ord(self.ln[0]) - 1) + str(int(self.ln[1]) + 1) in self.board.field.keys():
            if type(self.board.field[chr(ord(self.ln[0]) - 1) + str(int(self.ln[1]) + 1)]) == Chessman.Chessman:
                if self.board.field[chr(ord(self.ln[0]) - 1) + str(int(self.ln[1]) + 1)].team != self.team:
                    self.am.append(chr(ord(self.ln[0]) - 1) + str(int(self.ln[1]) + 1))
        if chr(ord(self.ln[0]) + 1) + str(int(self.ln[1]) + 1) in self.board.field.keys():
            if type(self.board.field[chr(ord(self.ln[0]) + 1) + str(int(self.ln[1]) + 1)]) == Chessman.Chessman:
                if self.board.field[chr(ord(self.ln[0]) + 1) + str(int(self.ln[1]) + 1)].team != self.team:
                    self.am.append(chr(ord(self.ln[0]) + 1) + str(int(self.ln[1]) + 1))
        
    def move(self, ln):

        if ln in self.am:
            if self.board.field[ln] == None:
                self.board.field[ln] = self
                self.board.field[self.ln] = None
                self.ln = ln

            else:
                self.board.field[ln].die()
                self.board.field[ln] = self
                self.board.field[self.ln] = None
                self.ln = ln
            self.availableMoves()
        else:
            print("ошибка")
    def print(self):
        if self.team == "white":
            return "P "
        else:
            return "p "
