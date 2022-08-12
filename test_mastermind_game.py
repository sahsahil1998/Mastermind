'''
Sahil Sah
CS5001 Spring 2022
Final Project
Testing Mastermind Functions

'''

import unittest
import random
from mastermind_class import generate_answer, game_logic

COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'black']


class TestGameLogic(unittest.TestCase):
    '''
    Class for testing functions used in Mastermind
    game for the game logic
    '''


    def test_generate_answer(self):
        '''
        Method: test_generate_answer
                Tests to make sure generated answers are in the COLORS
                list and if the lengths match up
        Parameters:none
        return: tests pass or failed
        '''
        answer = generate_answer()
        # checking to make sure generated colors in COLORS list
        for i in answer:
            if i not in COLORS:
                print('Color checking failed')
            else:
                print('Pass')
        guess = random.sample(COLORS, 4)
        # testing to make sure length is 4
        self.assertEqual(len(answer), len(guess))

    def test_game_logic(self):
        # tests counting of bulls and cows from a set guess
        # randomly generated answer
        answer = generate_answer()
        # set guess to be tested against
        guess = ['red', 'green', 'blue', 'black']
        
        test1_bulls_cows = game_logic(answer, guess)
        print('Test against random answer code: ', test1_bulls_cows)

        
        # setting an answer without randomness to count cows/bulls
        set_answer = ['purple', 'yellow', 'black', 'blue']
        # correct count for (bulls, cows) when comparing set_answer to guess
        correct_bulls_cows = (0, 2)
        # using game function to test output
        test2_bulls_cows = game_logic(set_answer, guess)
        print('Test against set answer code: ', test2_bulls_cows)
        self.assertEqual(test2_bulls_cows, correct_bulls_cows)
        

def main():

   unittest.main(verbosity = 3)

        
if __name__ == '__main__':
    unittest. main()
