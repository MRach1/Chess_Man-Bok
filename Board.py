import Pawn
import Chessman
class Board():

    def __init__(self):
        """
        a = []
        for i in range(8):
            a.append([0, 0, 0, 0, 0, 0, 0, 0])
        this.field = copy(a)
        """
        letters = "ABCDEFGH"
        numbers = "12345678"
        self.field = {x+y: None for x in letters for y in numbers}
        for i in self.field.keys():
            if "2" in i:
                self.field[i] = Pawn.Pawn(self, i, "white")
        for i in self.field.keys():
            if "7" in i:
                self.field[i] = Pawn.Pawn(self, i, "black")
        self.arr = list(self.field.values())

    def printt(self):
        self.arr = list(self.field.values())
        for i in range(8):
            for j in range(8):
                if type(self.arr[i*8 + j]) == Pawn.Pawn:
                    print(self.arr[i*8 + j].print(), end='')
                else:
                    print("@ ", end='')
            print("")

