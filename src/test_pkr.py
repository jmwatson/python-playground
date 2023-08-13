import unittest
from pkr import *

class TestPKRHandEvaluation(unittest.TestCase):

    def test_ace_low_rank(self):
        self.assertEqual(ace_low_rank('A'), 0)
        self.assertEqual(ace_low_rank('2'), 1)
        self.assertEqual(ace_low_rank('9'), 8)

    def test_rank(self):
        self.assertEqual(rank('A'), 9)
        self.assertEqual(rank('2'), 1)
        self.assertEqual(rank('9'), 8)

    def test_is_straight(self):
        self.assertTrue(is_straight(['2H', '3H', '4H']))
        self.assertTrue(is_straight(['AH', '2C', '3S']))
        self.assertFalse(is_straight(['AH', '9S', '8C']))

    def test_is_flush(self):
        self.assertTrue(is_flush(['2H', '5H', '9H']))
        self.assertFalse(is_flush(['AH', '2C', '3S']))

    def test_hand_rank(self):
        self.assertEqual(hand_rank(['2H', '3H', '4H']), 503)  # Straight Flush
        self.assertEqual(hand_rank(['3H', '4D', '5H']), 204)  # Straight
        self.assertEqual(hand_rank(['2H', '5H', '9H']), 308)  # Flush
        self.assertEqual(hand_rank(['2H', '2C', '4H']), 101)  # Pair
        self.assertEqual(hand_rank(['AH', '2C', '3S']), 202)  # Straight with Ace
        self.assertEqual(hand_rank(['7H', '7C', '7D']), 406)  # Three of a kind
        self.assertEqual(hand_rank(['2H', '3C', '5D']), 4)    # High card

    def test_compare_hands(self):
        self.assertEqual(compare(['AH', '2C', '3S'], ['2H', '3H', '4H']), -1)  # Hand 2 wins
        self.assertEqual(compare(['7H', '7C', '9D'], ['7S', '7D', '9C']), 0)   # Tie
        self.assertEqual(compare(['9H', '7C', '8C'], ['3D', '2S', '4S']), 1)   # Hand 1 wins

    # wanted some extra coverage over pairs since there are some edge cases
    def test_compare_hands_pairs(self):
        self.assertEqual(compare(['7H', '7C', '9D'], ['7S', '7D', '8C']), 1)   # Hand 1 wins
        self.assertEqual(compare(['7H', '7C', '9D'], ['6S', '6D', '9C']), 1)   # Hand 1 wins
        self.assertEqual(compare(['7H', '7C', '9D'], ['8S', '8D', '2C']), -1)  # Hand 2 wins
        self.assertEqual(compare(['3H', '3C', '4C'], ['4S', '4D', '3D']), -1)  # Hand 2 wins

if __name__ == '__main__':
    unittest.main()
