from board import draw_board                                                            # hämtar funktionen draw_board från filen board.py

board = [
    {"type": "grass", "direction": 0,  "tiles": [".", ".", ".", ".", ".", ".", "."]},   # rad 0: gräs, ingen riktning, bara gräsrutor
    {"type": "road",  "direction": 1,  "tiles": ["-", "B", "B", "-", "-", "-", "-"]},   # rad 1: väg, bilar åt höger, en bil i kolumn 1–2           
    {"type": "road",  "direction": -1, "tiles": ["-", "-", "-", "-", "B", "-", "-"]},   # rad 2: väg, bilar åt vänster, en bil i kolumn 4
    {"type": "grass", "direction": 0,  "tiles": [".", ".", ".", ".", ".", ".", "."]},   # rad 3: gräs, säker rad mitt i banan
    {"type": "road",  "direction": 1,  "tiles": ["B", "-", "-", "-", "-", "B", "-"]},   # rad 4: väg, bilar åt höger, bilar i kolumn 0 och 5
    {"type": "grass", "direction": 0,  "tiles": [".", ".", ".", ".", ".", ".", "."]},   # rad 5: gräs, startraden där spelaren står
]

player = (5, 3)                                                                         # tupel för spelarens position: rad 5 (nederst), kolumn 3 (mitten)

draw_board(board, player)                                                               # anropar funktionen