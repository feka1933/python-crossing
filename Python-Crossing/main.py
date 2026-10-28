from board import draw_board                                    # hämtar funktionen draw_board från filen board.py
from player import move_player                                  # hämtar funktionen move_player från filen player.py
from collision import check_collision                           # hämtar funktionen check_collision från filen collision.py
from cars import move_cars
from score import add_point, show_score, show_final_score        #hämtar poängfunktionerna från filen score.py
import readchar

board = [
    {"type": "grass", "direction": 0,  "tiles": ["🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩"]},   # rad 0: gräs, ingen riktning, bara gräsrutor
    {"type": "road",  "direction": 1,  "tiles": ["⬛", "🚗", "🚗", "⬛", "⬛", "⬛", "⬛"]},   # rad 1: väg, bilar åt höger, en bil i kolumn 1–2
    {"type": "road",  "direction": -1, "tiles": ["⬛", "⬛", "⬛", "⬛", "🚗", "⬛", "⬛"]},   # rad 2: väg, bilar åt vänster, en bil i kolumn 4
    {"type": "grass", "direction": 0,  "tiles": ["🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩"]},   # rad 3: gräs, säker rad mitt i banan
    {"type": "road",  "direction": 1,  "tiles": ["🚗", "⬛", "⬛", "⬛", "⬛", "🚗", "⬛"]},   # rad 4: väg, bilar åt höger, bilar i kolumn 0 och 5
    {"type": "grass", "direction": 0,  "tiles": ["🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩"]},   # rad 5: gräs, startraden där spelaren står
]

player = (5, 3)                                                                         # tupel för spelarens position: rad 5 (nederst), kolumn 3 (mitten)
score = 0                                                                               #spelarens aktuella poäng

game_over = False

while not game_over:
    print("\n" * 30)                                            # skriver ut tomma rader så att det gamla brädet åker ur synfältet
    draw_board(board, player)                                   # ritar brädet med spelaren på sin nuvarande position
    show_score(score)                                           # NY: visar den aktuella poängen direkt under brädet
    print("w = upp   s = ner   a = vänster   d = höger   q = avsluta")   # påminner om vilka tangenter som gäller
    choice = readchar.readkey().lower()                         # läser in spelarens tangent med readchar och gör om stora bokstäver til små

    if choice == "q":                                           # om spelaren skrev q ...
        break                                                   # ... hoppar vi ur loopen och programmet tar slut

    player = move_player(player, choice, board)                 # flyttar spelaren (ogiltiga drag = stå kvar)
    game_over = check_collision(board, player)                  # krockade spelaren in i en bil?

    if not game_over:                                           # om spelaren klarade sitt drag ...
        # NY: poängen delas ut först efter krockkollen ovan, så att ett hopp
        # NY: rakt in i en bil inte ger något poäng – bara hopp som klaras räknas
        if choice == "w":                                       #om spelaren hoppar ett steg...
            score = add_point(score)                            # ...såfall läggs poäng till
        move_cars(board)                                        # ... flyttar alla bilar ett steg
        game_over = check_collision(board, player)              # krockade en bil in i spelaren?

if game_over:
    print("\n" * 30)
    draw_board(board, player)
    print("GAME OVER! Du blev påkörd.")

show_final_score(score)                                         # visar slutpoängen, oavsett om spelaren dog eller tryckte q
print("Spel avslutat")                                          # skrivs ut när spelet har avslutats