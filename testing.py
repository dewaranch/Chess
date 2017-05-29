
#Defining class for pieces.
class Piece:

    def __init__(self, ptype, color, file, rank):
        self.ptype=ptype
        self.color=color
        self.rank=rank
        self.file=file

#defining pieces and setting up initial board
wp1=Piece('Pawn','White','a','2')
wp2=Piece('Pawn','White','b','2')
wp3=Piece('Pawn','White','c','2')
wp4=Piece('Pawn','White','d','2')
wp5=Piece('Pawn','White','e','2')
wp6=Piece('Pawn','White','f','2')
wp7=Piece('Pawn','White','g','2')
wp8=Piece('Pawn','White','h','2')

wr1=Piece('Rook','White','a','1')
wr2=Piece('Rook','White','h','1')

wn1=Piece('Night','White','b','1')
wn2=Piece('Night','White','g','1')

wb1=Piece('Bishop','White','c','1')
wb2=Piece('Bishop','White','f','1')

wq=Piece('Queen','White','d','1')
wk=Piece('King','White','e','1')

bp1=Piece('Pawn','Black','a','7')
bp2=Piece('Pawn','Black','b','7')
bp3=Piece('Pawn','Black','c','7')
bp4=Piece('Pawn','Black','d','7')
bp5=Piece('Pawn','Black','e','7')
bp6=Piece('Pawn','Black','f','7')
bp7=Piece('Pawn','Black','g','7')
bp8=Piece('Pawn','Black','h','7')

br1=Piece('Rook','Black','a','8')
br2=Piece('Rook','Black','h','8')

bn1=Piece('Night','Black','b','8')
bn2=Piece('Night','Black','g','8')

bb1=Piece('Bishop','Black','c','8')
bb2=Piece('Bishop','Black','f','8')

bq=Piece('Queen','Black','d','8')
bk=Piece('King','Black','e','8')

Pieces=[wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wr1, wr2, wn1, wn2, wb1, wb2, wq, wk,
        bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, br1, br2, bn1, bn2, bb1, bb2, bq, bk]

def getFile(inputPiece):
    return inputPiece.file

def WhiteMove():
    pselect=input('White player, enter the file and rank of the piece you want to move.')
    move=input('enter the file and rank of where you want to move it.')
def BlackMove():
    pselect=input('Black player, enter the file and rank of the piece you want to move.')
    move=input('enter the file and rank of where you want to move it.')

def legalPawn(initial,movedto):
    


