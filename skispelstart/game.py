# Laad Pygame Zero.
import pgzrun

# Laad de functie 'randrange' uit de module 'random'
# Hiermee kan je een willekeurig getal tussen twee bepaalde waardes kiezen.
from random import randrange

# Breedte en hoogte van het speelveld.
WIDTH  = 400
HEIGHT = 800

# Maak Rob, de skiënde robot, en zet hem op de juiste plek.
# Rob is een zogenaamde acteur, iets in het spel dat kan bewegen.
rob     = Actor('robot_links')
rob.pos = 200, 200

# Maak de slalom vlaggen, zet ze willekeurig aan de bodem van het speelveld.
slalom = Actor('slalom_baan')
slalom.x = randrange(80, WIDTH - 80)
slalom.y = HEIGHT - 20

# De snelheid waarmee Rob naar links of rechts beweegt, deze komt later nog van pas.
rob.vx  = 0.0

# De punten die Rob heeft verdient. Wij zetten hem hier op 0 aan het start van het spel.
rob.punten = 0

# Deze functie tekent het speelscherm.
# Deze functie wordt heeeel vaak aangeroepen door PyGame Zero,
# zodat het net lijkt alsof de acteurs (Rob en de slalom vlaggen) vloeiend bewegen!
def draw():
    pass

# Deze functie veranderd de acteurs in het spel als dat nodig is,
# bijvoorbeeld wanneer je een toets op je toetsenbord drukt.
def update(dt):    
    pass

# Start het spel!
pgzrun.go()