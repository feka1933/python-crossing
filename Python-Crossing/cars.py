def move_cars(board):
    """Move every car one step in its row's direction. Cars that leave one side come back on the other."""
    for row in board:                                           # går igenom varje rad i banan
        tiles = row["tiles"]                                    # hämtar radens lista med rutor
        if row["direction"] == 1:                               # bilarna kör åt höger
            row["tiles"] = [tiles[-1]] + tiles[:-1]             # sista rutan flyttas först, allt annat ett steg åt höger
        elif row["direction"] == -1:                            # bilarna kör åt vänster
            row["tiles"] = tiles[1:] + [tiles[0]]               # första rutan flyttas sist, allt annat ett steg åt vänster
                                                                # gräsrader har riktning 0 och lämnas orörda