def check_collision(board, player):
    """Returns True if the player is standing on a car '🚗' otherwise False."""
    row = player[0]                                             # tar spelarens radnummer
    col = player[1]                                             # tar spelarens kolumnnummer
    tile = board[row]["tiles"][col]                             # hämtar tecknet i rutan där spelaren står
    return tile == "🚗"                                          # jämförelsen blir True om rutan är en bil '🚗', annars False