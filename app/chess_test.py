import unittest
from chess import Chess

class Test(unittest.TestCase):
    def test_a1_position(self):
        self.assertEqual(Chess('a1').find_knight_possibilities_in_two_tours(), 
        {'firstTurn': ['b3', 'c2'], 'secondTurn': {'b3': ['c5', 'd4', 'd2', 'c1', 'a1', 'a5'], 'c2': ['d4', 'e3', 'e1', 'a1', 'a3', 'b4']}})

    def test_d4_position(self):
        self.assertEqual(Chess('d4').find_knight_possibilities_in_two_tours(), 
        {'firstTurn': ['e6', 'f5', 'f3', 'e2', 'c2', 'b3', 'b5', 'c6'], 'secondTurn': {'e6': ['f8', 'g7', 'g5', 'f4', 'd4', 'c5', 'c7', 'd8'], 
        'f5': ['g7', 'h6', 'h4', 'g3', 'e3', 'd4', 'd6', 'e7'], 'f3': ['g5', 'h4', 'h2', 'g1', 'e1', 'd2', 'd4', 'e5'], 'e2': ['f4', 'g3', 'g1', 'c1', 'c3', 'd4'], 
        'c2': ['d4', 'e3', 'e1', 'a1', 'a3', 'b4'], 'b3': ['c5', 'd4', 'd2', 'c1', 'a1', 'a5'], 'b5': ['c7', 'd6', 'd4', 'c3', 'a3', 'a7'], 
        'c6': ['d8', 'e7', 'e5', 'd4', 'b4', 'a5', 'a7', 'b8']}})

    def test_non_digit_try_should_exist(self):
        with self.assertRaises(ValueError) as cm:
            Chess('').find_knight_possibilities_in_two_tours()

    def test_only_one_digit_try_should_exist(self):
        with self.assertRaises(ValueError) as cm:
            Chess('a').find_knight_possibilities_in_two_tours()      

    def test_first_digit_invalid(self):
        with self.assertRaises(ValueError) as cm:
            Chess('#1').find_knight_possibilities_in_two_tours()

    def test_second_digit_invalid(self):
        with self.assertRaises(ValueError) as cm:
            Chess('a9').find_knight_possibilities_in_two_tours()                                   
if __name__ == '__main__':
    unittest.main()
