#un round est compose des plusiers maths exemple : 1 round : 4 maths donc 8 joueurs

class Round:
    def __init__(self, name, round_number, start_time="",end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches = []
        self.start_time = start_time
        self.end_time = end_time
        
    def add_matche(self, matche):
        self.matches.append(matche)
        
#Comment se fait la connexion entre le round, le tournoi et le match ?????
#un torneo contiene varios rounds (4 default) y un round contiene varios partidos y 
# los partidos tienen jugadores 
"""- añadir jugadores a los torneos
    - añadir rondas a los torneos
    - añadir partidos a las rondas
    - mejorar la interfaz de la consola para que los mensajes y 
    las entradas sean más claros (añadir líneas blancas, espacios, :)"""

