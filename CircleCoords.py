'''
Sahil Sah
CS5001
Spring 2022
Final Project

This code creates a class to take in the coordinates of the
marbles the user interacts with so it can be
checked for click in a specific range and do an
action based on that
'''
# global variable for length of the marbles
MARBLE_RADIUS = 15

class HoldCircles:
    '''
    This class manages the coordinates of the input
    marbles to be checked for ranges so actions
    can occur.
    '''
    def __init__(self, x, y, color):
        '''
        Method -- init
                Creates the constructor of the class and takes in
                x/y coordinates and color as objects. 
        Parameters: x- the x coordinate of the marble
                    y- the y coordinate of marble
                    color - color of marble
        Return: none
        '''
        self.x = x
        self.y = y
        self.color = color

    def click_in_choices(self, x, y):
        '''
        Method -- click_in_choices
                -checks the range of the coordinates of the
                marbles
        Parameters: x- the x coordinate of the marble
                    y- the y coordinate of marble
                    
        Return: the width of the marble of the range
        of coordinates its in and if the click is
        within that range
        '''

        x1 = self.x + MARBLE_RADIUS
        x2 = self.x - MARBLE_RADIUS
        y1 = self.y + MARBLE_RADIUS + MARBLE_RADIUS
        y2 = self.y - MARBLE_RADIUS + MARBLE_RADIUS
        click_width =  x > x2 and x < x1

        click_height = y > y2 and y < y1
        return click_width and click_height
