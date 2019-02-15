#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_methods(self):
        prod = Product('Test Product', price = 20, weight = 10, flammability = 0.8)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...fizzle")

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(len(prods), 30)
    
    def test_legal_names(self):
        self.assertIn(generate_products(), random.choice(adjective) + ' ' + random.choice(noun))

if __name__ == '__main__':
    unittest.main()
