def draw_board(board, player):
    """Prints the board with the player shown as 👤"""
    for row_number in range(len(board)):                        # går igenom varje radnummer
        row = board[row_number]                                 # hämtar raden från board ordlistan
        line = ""                                               # skapar en tom sträng som så småningom ska fyllas på
        for column_number in range(len(row["tiles"])):          # går igenom varje kolumnnummer i radens lista med rutor
            if (row_number, column_number) == player:           # kollar om rutans position är samma som spelarens
                line += "👤"                                    # i så fall ritas spelaren
            else:                                               # om inte spelaren står här
                line += row["tiles"][column_number] + " "       # ritas rutan ut med dens egna tecken och ett mellanslag
        print(line)                                             # skriver ut den fullständiga raden

# Kör hela programmet i main.py  