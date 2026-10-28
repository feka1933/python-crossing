#poängsystem för python-crossing.
#ett hopp fram ger ett poäng



def add_point(score): #ökar poäng med ett och retunerar nya poängen
    return score + 1


def show_score(score): #skriver ut den aktuella poängen 
    print(f"Poäng: {score}")


def show_final_score(score): #skriver ut slutpoängen när spelet är slut
    print(f"Slutpoäng: {score}")