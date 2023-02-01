import random
from math import pi
from dataclasses import dataclass

class StringFoo:
   def __init__(self, message):
       self.message = message
   def set_string(self, msg):
       self.message = msg
   def print_string(self):
       print(self.message)

class Rectangle:
   def __init__(self, largeur, longueur):
       self.largeur = largeur
       self.longueur = longueur
   def calcul_aire(self):
       return self.longueur * self.largeur
   def afficher_info(self):
       print(f"{self.longueur}{self.largeur}{self.calcul_aire()}")
print(Rectangle(2, 3).calcul_aire())

class Cercle:
   def __init__(self, rayon):
       self.rayon = rayon
   def calcul_aire(self):
       return self.rayon * 2 * pi
   def calcul_circonference(self):
       return self.rayon * 2 * pi
print(Cercle(10).calcul_circonference())
print(Cercle(10).calcul_aire())

@dataclass
class Personnage:
   puissance: int = random.randint(1, 20)
   agiliter: int = random.randint(1, 20)
   IQ: int = random.randint(1, 20)
   Genetics: int = random.randint(1, 20)
   Magie: int = random.randint(1, 20)


