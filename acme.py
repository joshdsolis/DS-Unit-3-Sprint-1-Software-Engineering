#!/usr/bin/env python
"""
Python module for Acme Corp's Products
"""
import random

class Product:
    """Class for Acme's Product"""

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, 
    identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        ratio = self.price/float(self.weight)
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        final = self.flammability * self.weight
        if final < 10:
            return "...fizzle"
        elif final >= 10 and final < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):

    def __init__(self, name, price = 10, weight = 10, flammability = 0.5, 
    identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return "...it's a glove"
    
    def punch(self):
        if self.weight < 5:
            return "That tickles"
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"