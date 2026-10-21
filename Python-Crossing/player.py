def move_player(player, choice, board):
    """Moves the player one step in the chosen direction. Invalid keys, or moves that would leave the board, keep the player in place."""
    row = player[0]                                             # plockar ut spelarens nuvarande radnummer
    col = player[1]                                             # plockar ut spelarens nuvarande kolumnnummer

    if choice == "w":                                           # w = uppåt, och uppåt på skärmen är ett LÄGRE radnummer
        row = row - 1
    elif choice == "s":                                         # s = nedåt, alltså ett högre radnummer
        row = row + 1
    elif choice == "a":                                         # a = ett steg åt vänster, alltså ett lägre kolumnnummer
        col = col - 1
    elif choice == "d":                                         # d = ett steg åt höger, alltså ett högre kolumnnummer
        col = col + 1

    number_of_rows = len(board)                                 # hur många rader brädet har
    number_of_columns = len(board[0]["tiles"])                  # hur många kolumner brädet har (läser av den första raden)

    if row < 0 or row >= number_of_rows:                        # skulle spelaren hamna ovanför eller under brädet?
        return player                                           # i så fall: ogiltigt drag, returnera gamla positionen
    if col < 0 or col >= number_of_columns:                     # skulle spelaren hamna utanför brädet åt vänster eller höger?
        return player                                           # i så fall: ogiltigt drag, returnera gamla positionen

    return (row, col)                                           # den nya giltiga positionen, som en tupel precis som tidigare

