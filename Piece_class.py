
#Defining class for pieces.
class Piece:

    def __init__(self, ptype, color, file, rank, moved):
        self.ptype=ptype
        self.color=color
        self.rank=rank
        self.file=file
        self.moved=moved
        
def getFile(inputPiece):
    return inputPiece.file

def getRank(inputPiece):
    return inputPiece.rank

def getColor(inputPiece):
    return inputPiece.color

def getPtype(inputPiece):
    return inputpiece.ptype

def moved(inputPiece):
    return inputpiece.moved

