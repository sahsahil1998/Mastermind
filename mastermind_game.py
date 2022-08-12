'''
Sahil Sah
CS5001
Spring 2022
Final Project: Mastermind

Main file that runs the game through the three class
imported through the mastermind_class file
'''

import turtle
from Point import Point
from turtle import Screen, Turtle
from mastermind_class import MasterMind

    

def main():
    # initialize screen and create driver for class
    screen = turtle.Screen()
    game_driver = MasterMind(Point(-300,200), 'red')
    game_driver.draw_gameboard()
    # handle the clicks of the user on screen
    screen.onclick(game_driver.get_user_guess_clicks)
    
    
if __name__ == "__main__":
    main()
    
