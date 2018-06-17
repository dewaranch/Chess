#Setting up the pieces.
import Piece_class as pc
Piece=pc.Piece
gf=pc.getFile
gr=pc.getRank
gc=pc.getColor
gp=pc.getPtype
gm=pc.moved

#defining pieces and setting up initial board
wp1=Piece('Pawn','White','a','2',0)
wp2=Piece('Pawn','White','b','2',0)
wp3=Piece('Pawn','White','c','2',0)
wp4=Piece('Pawn','White','d','2',0)
wp5=Piece('Pawn','White','e','2',0)
wp6=Piece('Pawn','White','f','2',0)
wp7=Piece('Pawn','White','g','2',0)
wp8=Piece('Pawn','White','h','2',0)

wr1=Piece('Rook','White','a','1',0)
wr2=Piece('Rook','White','h','1',0)

wn1=Piece('Night','White','b','1',0)
wn2=Piece('Night','White','g','1',0)

wb1=Piece('Bishop','White','c','1',0)
wb2=Piece('Bishop','White','f','1',0)

wq=Piece('Queen','White','d','1',0)
wk=Piece('King','White','e','1',0)

bp1=Piece('Pawn','Black','a','7',0)
bp2=Piece('Pawn','Black','b','7',0)
bp3=Piece('Pawn','Black','c','7',0)
bp4=Piece('Pawn','Black','d','7',0)
bp5=Piece('Pawn','Black','e','7',0)
bp6=Piece('Pawn','Black','f','7',0)
bp7=Piece('Pawn','Black','g','7',0)
bp8=Piece('Pawn','Black','h','7',0)

br1=Piece('Rook','Black','a','8',0)
br2=Piece('Rook','Black','h','8',0)

bn1=Piece('Night','Black','b','8',0)
bn2=Piece('Night','Black','g','8',0)

bb1=Piece('Bishop','Black','c','8',0)
bb2=Piece('Bishop','Black','f','8',0)

bq=Piece('Queen','Black','d','8',0)
bk=Piece('King','Black','e','8',0)

WhitePieces=[wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wn1,wn2,wb1,wb2,wq,wk]
BlackPieces=[bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bn1,bn2,bb1,bb2,bq,bk]
AllPieces=WhitePieces+BlackPieces
print(len(WhitePieces))
print(len(BlackPieces))
print(len(AllPieces))




