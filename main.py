import Board
b = Board.Board()
print(b.field)
b.printt()
b.field["A2"].move("A4")
print("--------------------------------------")
b.printt()