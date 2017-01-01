import random

class Abbott(object):   # <--- the 'object' specifier here lets the python interpreter know that this class refers to
                        # an object in the code that can be instantiated or destroyed via calls to it

    def __init__(self, health): # <--- don't worry about this for now, each class needs an __init__ function because it's
                        # how the interpreter knows that this class is an object. most languages (like Java) hide this
                        # from you, so you may not see it again.
        self.loader = "Abbott loaded" # <--- this is useful for debugging, to see if the object was actually loaded
        self.health = 100 # <--- we initialize Abbott to full health

    def spawn(self):    # <--- inside each class, you can have what are called 'methods' (really just python functions)
                        # that operate on each instance of the object.

        pygame.image.load('Abbott.png') # <--- ABBOTT LIVES
    
    def attack(self):   # <--- this one deals damage (to the player's dingo) every time it's called

        Player.takeDamage() # <--- damages the player

    def takeDamage(self):

        Abbott.health -= random.randint(5, 20) # <--- what this does is subtract a pseudo-random amount of health from
                                               # Abbott, makes things more interesting and less predictable

    def killYour(self): # <--- this one handles despawning the dead Abbott boss after his health drops to 0

        pygame.image.unload('Abbott.png') # <--- I actually have no idea how to unload a pygame sprite, so look that up

class Player(object):   # <--- a player object is created just the same as an Abbott object

    def __init__(self, health):
        self.loader = "Player loaded"
        self.health = 100

    def spawn(self):

        pygame.image.load('Dingo.png') # <--- or whatever you called your dingo sprite

    def attack(self):

        Abbott.takeDamage() # <--- Abbott takes damage from the attack

    def takeDamage(self):

        Player.health -= random.randint(5, 20)

    def killYour(self):

        pygame.image.unload('Dingo.png')

