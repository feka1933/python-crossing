from board import generate_row                                 # behövs för att skapa nya rader


def move_player(player, choice, board):
    """Flyttar spelaren ett steg. Världen rullar när spelaren går uppåt
    från mitten av brädet – då skapas en ny rad högst upp och den nedersta tas bort."""
    row = player[0]
    col = player[1]
    middle_row = len(board) // 2                                # mittenraden (t.ex. rad 3 vid 6 rader)

    if choice == "w":
        new_row = row - 1
        if new_row < middle_row and row <= middle_row:          # spelaren vill gå förbi mittraden uppåt?
            board.insert(0, generate_row(len(board[0]["tiles"])))   # lägg till ny rad högst upp
            board.pop()                                             # ta bort nedersta raden
            row = middle_row                                        # spelaren stannar på mittraden
            # ↑ men rutan de står på är nu den som förut låg raden ovanför
        else:
            row = new_row
    elif choice == "s":
        row = row + 1
    elif choice == "a":
        col = col - 1
    elif choice == "d":
        col = col + 1

    number_of_rows = len(board)
    number_of_columns = len(board[0]["tiles"])

    if row < 0 or row >= number_of_rows:
        return player
    if col < 0 or col >= number_of_columns:
        return player

    return (row, col)