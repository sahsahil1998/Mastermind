'''
Sahil Sah
CS5001
Spring 2022
Final Project

This code creates a class to take in the coordinates of the
image gifs the user interacts with so it can be
checked for click in a specific range and do an
action based on that
'''

class Gifs:
    '''
    This class manages the coordinates of the gifs
    to be checked for ranges so actions
    can occur.
    '''
    def __init__(self, x1, y1, x2, y2, width, height, image):
        '''
        Method -- init
                Creates the constructor of the class and takes in
                x/y coordinates to get widths and heights
                of where the image is and the image. 
        Parameters: x1/x2- the x coordinates of the image
                    y1/y2- the y coordinates of marble
                    width/hieght- x and y ranges of the image
        Return: none
        '''
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.height = height
        self.image = image

    def click_in_gif(self, x, y):
        '''
        Method -- click_in_gif
                -checks the range of the coordinates of the
                gif
        Parameters: x- the x coordinate of the gif
                    y- the y coordinate of gif
                    
        Return: the width and height of the images for the range
        of coordinates its in and if the click is
        within that range
        '''
        
        object_width =  x > self.x1 and x < self.x2
        object_height = y > self.y2 and y < self.y1

        return object_width and object_height

