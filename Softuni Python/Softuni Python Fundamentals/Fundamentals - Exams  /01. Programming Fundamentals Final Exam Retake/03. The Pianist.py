class Piece:
    """
    This class holds information about a piece.
    Each peace should have a name, composer and a key.
    """
    def __init__(self, piece: str, composer: str, key: str):
        self.piece = piece
        self.composer = composer
        self.key = key
    
    def __repr__(self):
        """
        We just Print information about the piece
        """
        return f"{self.piece} -> Composer: {self.composer}, Key: {self.key}"

class Pieces:
    """
    This class serves a purpose as a collection
    """
    def __init__(self):
        self.pieces = {}
    
    def __repr__(self):
        pieces_list = []
        for _, piece_data in self.pieces.items():
            pieces_list.append(str(piece_data))
        return "\n".join(pieces_list)
    
    def add(self, piece: str, composer: str, key: str, is_quite = False):
        if piece in self.pieces:
            if not is_quite:
                print(f"{piece} is already in the collection!")
            return
        self.pieces[piece] = Piece(piece=piece, composer=composer, key=key)
        if not is_quite:
            print(f"{piece} by {composer} in {key} added to the collection!")
    
    def remove(self, piece: str):
        if piece not in self.pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            return
        self.pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    
    def change_key(self, piece: str, key: str):
        if piece not in self.pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            return
        self.pieces[piece].key = key
        print(f"Changed the key of {piece} to {key}!")



separator = "|"
pieces = Pieces()

number_of_pieces = int(input())

for _ in range(number_of_pieces):
    piece_data = input()
    piece, composer, key = piece_data.split(separator)

    pieces.add(piece=piece, composer=composer, key=key, is_quite=True)

while True:
    command_line = input()
    if command_line == "Stop":
        print(pieces)
        break

    commands = command_line.split(separator)

    match commands[0]:
        case "Add":
            piece, composer, key = commands[1:]
            pieces.add(piece=piece, composer=composer, key=key)

        case "Remove":
            piece = commands[1]
            pieces.remove(piece=piece)
        
        case "ChangeKey":
            piece, key = commands[1:]
            pieces.change_key(piece=piece, key=key)
        

