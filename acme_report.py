#!/usr/bin/env python

import random
from acme import *


def generate_products(prod = 30):       
    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    randName = random.choice(adjective) + ' ' + random.choice(noun)
    price, weight = random.randint(5,100), random.randint(5,100)
    flam = random.uniform(0,2.5)
    products = []
    for _ in range(prod):
        products.append(Product(randName, price, weight, flam))
    return products

def inventory_report(prods):
    def Average(lst):
        return reduce(lambda a, b: a + b, lst) / len(lst) 
    prices = []
    weights = []
    flams = []
    for item in prods:
        prices.append(item.price)
        weights.append(item.weight)
        flams.append(item.flammability)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", len(prods))
    print("Average price: ", Average(prices))
    print("Average weight: ", Average(weights))
    print("Average flammability: ", Average(flams))

if __name__ == '__main__':
    inventory_report(generate_products())