## Förenklad version av python-crossing:
1. En fast spelbana som en lista, utan slump och rörliga bilar:
- finns i board.py

2. En funktion för att flytta spelaren:
- finns i player.py

3. Funktion som kollar om spelaren står på en bil ruta:
- finns i collision.py

## Avancerad version av python-crossing:

1. Poäng system

2. Bilar som förflyttar sig på spelbanan

3. Slumpade rader

4. Ökande svårighet

## Funktioner och vokabulär:

- draw_board från board.py
- move_player från player.py
- check_collision från collision.py

## Fel/problem som behöver fixas:

- Spelarens ikon är inte centrerad när spelet körs, om man lägger till ett mellanslag efter ikonen blir startraden bara längre än de andra
FIXAT, bytta ut alla tecken i banan mot emojis så att de var lika breda

- eftersom vi använder input för rörelse krävs det att man klickar enter varje gång när man vill gå, så vi borde använda biblioteket "readchar" för att göra det snabbare