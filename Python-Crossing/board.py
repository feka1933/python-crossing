import random


def draw_board(board, player):
    """Prints the board with the player shown as 👤"""
    for row_number in range(len(board)):                        # går igenom varje radnummer
        row = board[row_number]                                 # hämtar raden från board ordlistan
        line = ""                                               # skapar en tom sträng som så småningom ska fyllas på
        for column_number in range(len(row["tiles"])):          # går igenom varje kolumnnummer i radens lista med rutor
            if (row_number, column_number) == player:           # kollar om rutans position är samma som spelarens
                line += "👤 "                                    # i så fall ritas spelaren med ett mellanslag efter
            else:                                               # om inte spelaren står här
                line += row["tiles"][column_number] + " "       # ritas rutan ut med dens egna tecken och ett mellanslag
        print(line)                                             # skriver ut den fullständiga raden

# Kör hela programmet i main.py  


def generate_row(number_of_columns=7):
    """Create a random row: 40% grass, otherwise a road with 1–2 cars."""
    if random.random() < 0.4:                                   # 40 % chans till säker gräsrad
        return {"type": "grass", "direction": 0,
                "tiles": ["🟩"] * number_of_columns}

    direction = random.choice([1, -1])                          # bilar åt höger eller vänster
    tiles = ["⬛"] * number_of_columns                          # börja med tom väg
    number_of_cars = random.randint(1, 2)                       # 1 eller 2 bilar
    for position in random.sample(range(number_of_columns), number_of_cars):
        tiles[position] = "🚗"                                  # placera ut bilarna på slumpade kolumner
    return {"type": "road", "direction": direction, "tiles": tiles}