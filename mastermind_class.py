'''
Sahil Sah
CS5001
Spring 2022
Final Project: Mastermind

File that includes the two game logic and generating
answer function as well as the Mastermind class
that draws the board and allows user to run through the game
'''


import turtle
import random
import datetime
import time
from Point import Point
from turtle import Screen, Turtle
from GifCoords import Gifs
from CircleCoords import HoldCircles

# set global variables that are consistent for list of colors and marble radius
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'black']
MARBLE_RADIUS = 15

def generate_answer():
    '''
    Function: generates a random list of 4 colors that will
    be the answer for each mastermind game
    Parameters: none
    Return: the 4 color list that will be the answer
    '''
    answer = random.sample(COLORS, 4)
    return answer

def game_logic(answer, player_guess):
    '''
    Function: game logic that counts the cows and bulls
    where bulls are if the player guess is the corect
    color and in the correct position and the cows if
    the color is right but in the wrong position
    Parameters: the list of the answer code generated from
    generate_answer and the players color guesses to be matched
    with the answer
    Return: number of bulls and cows to be counted
    '''
    bull = 0
    cow = 0
    if len(answer) != 4 or len(player_guess) != 4:
        raise Exception('The answer list or guess list is too short')
    for i in range(4):
        if answer[i] == player_guess[i]:
            bull += 1
        elif player_guess[i] in answer:
            cow += 1
    return bull, cow
        

class MasterMind:
    '''
    This class creates the blueprint for playing Mastermind
    using Turtle drawing while using the game logic from
    the functions to generate answer and game_logic. It allows
    for the game board to be drawn and game to be played
    through click coordinate data and images.
    '''
    
    def __init__(self, position, color, size = MARBLE_RADIUS):
        '''
        Method -- init
                Creates the constructor of the class Mastermind for
                the game to be played through
                
        Parameters: positions - the current positions of where
        specific things are drawn
                    color - colors of obects
                    size - size of objects, set to default
                    to marble_radius for circles
        Return: none
        '''
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)
        # generates answer for each game
        self.answer = generate_answer()
        self.choice_starting_position = Point(-300,-300)
        # holds coords of play area that will be clicked on
        self.input_row_coords = []
        self.starting_position = Point(-300, 200)
        # holds coords of placed gifs
        self.gifs_coords = []
        # counter for current row
        self.current_row = 0
        # holds list of coords for the area the player chooses from
        self.choice_box = []
        # holds correct answers of each row to be checked
        self.accuracy_of_guess = []
        # score counter
        self.track_score = 0
        # string of player name
        self.player = ''


    def new_pen(self):
        '''
        Method -- new_pen
                  for the turtle pen to be used as
                  an instance
        Parameters: none
        Return: initilized turtle
        '''
        
        return turtle.Turtle()

    def make_screen(self):
        '''
        Method -- make_screen
                  initializes tutrle screen and sets to
                  900 by 800 screen size for game
        Parameters: none
        Return: none
        '''
        
        screen = turtle.Screen()
        screen.setup(900,800)

    def get_user_info(self):
        '''
        Method -- get_user_info
                  lets player input username into pop-up
                  text box
        Parameters: none
        Return: none
        '''
        self.player = turtle.textinput('MasterMind', 'Your name:')
        self.write_leaderboard()

    def set_positions(self, x, y):
        '''
        Method -- set_positions
                  holds positions of x and y for needed actions
        Parameters: x / y - sets position of x and y needed
        throughout the game
        Return: none
        '''        
        self.position.x = x
        self.position.y = y

    def draw_mastermind(self, x, y):
        '''
        Method -- draw_mastermind
                draws the word Mastermind in large letters at the
                top of the screen
        Parameters: x/y - position to start drawing at
        Return: none
        '''
        turtle.speed(0)
        turtle.pensize(10)
        turtle.penup()
        turtle.goto(x ,y)
        turtle.pendown()
        turtle.color('red')
        turtle.write('MasterMind', font=('Arial', 40, 'bold'))

    def draw_square(self, x, y, width, length, color='black'):
        '''
        Method -- draw_square
                method to call to draw square based on needed dimensions 
        Parameters: x / y - goes to x/y positions to start drawing
                    width - width of needed squre
                    length - length of needed square
                    color - needed color of square, defaults to black
        Return: none
        '''       
        turtle.speed(0)
        turtle.pensize(5)
        turtle.penup()
        turtle.sety(y)
        turtle.setx(x)
        turtle.pendown()
        turtle.color(color)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)

    def draw_circle(self, color = 'white', size = MARBLE_RADIUS):
        '''
        Method -- draw_circle
                draws circle in turtle with needed colors and sizes 
        Parameters: color - color of the circles (defaults to white)
                    size - the diameter of the marble (defaults to
                    global variable of 15)
        Return: none
        '''        
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        self.pen.circle(size)
        self.pen.end_fill()

    def draw_clear_circles(self, size):
        '''
        Method -- draw_clear_circles
                draws empty circles of the size needed 
        Parameters: size - the size of needed circle 
        Return: none
        '''        
        self.draw_circle(size = size)

    def draw_choices(self):
        '''
        Method -- draw_choices
                  draws the  filled color circles in the play box for the
                  player to choose the colors from
        Parameters: none
        Return: none
        '''
        self.position = self.choice_starting_position
        for index in COLORS:
            self.input_row_coords.append(HoldCircles(x = self.position.x,
                                                     y = self.position.y,
                                                     color = index))
            self.draw_circle(color = index, size = MARBLE_RADIUS)
            self.position.x += 40
    
    def draw_four_guess_circles(self):
        '''
        Method -- draw_four_guess_circles
                  draws the 4 small empty circles that will check 
                  the color the user selects from the play box
        Parameters: none
        Return: guess - list of appeneded circle data
        '''
        start_point_x = self.position.x
        start_point_y = self.position.y
        self.position.y += 15
        guess = []

        def draw_bull_cow_circles(guess):
            '''
            Method -- draw_bull_cow_circles
                      draws 2 sets of 2 small circles for each row
                      to check the 4 guess circles for the colors
                      the user chooses
            Parameters: guess - empty list that gets circle data
            appeneded into
            Return: guess
            '''
            for i in range(2):
                guess.append(HoldCircles(x = self.position.x,
                                         y = self.position.y,
                                         color = 'white'))
                self.draw_clear_circles(size = 3)
                self.position.y -= 10
            return guess
        guess = draw_bull_cow_circles(guess)
        self.position.y += 20
        self.position.x += 10
        guess = draw_bull_cow_circles(guess)
        return guess
                                     
                                     
    def draw_each_row_four(self):
        '''
        Method -- draw_each_row_four
                  draws 4 large empty circles in rows for
                  the player to choose selected color to be
                  colored into then checked
        Parameters: none
        Return: the current row and cow_bull checker
        '''       
        row = []
        for i in range(4):
            row.append(HoldCircles(x = self.position.x,
                                   y = self.position.y,
                                   color = 'white'))
            self.draw_clear_circles(MARBLE_RADIUS)
            self.position.x += 60
        cow_bull = self.draw_four_guess_circles()
        for each in row:
            return row, cow_bull
                

    def draw_ten_rows_of_all_circles(self):
        '''
        Method -- draw_ten_rows_of_all_circles
                  draws all of the need circles on the game
                  board down in 10 rows
        Parameters: none
        Return: none
        '''
        self.position = self.starting_position
        
        for i in range(10):
            row, cow_bull = self.draw_each_row_four()
            self.choice_box.append(row)
            self.accuracy_of_guess.append(cow_bull)
            self.position.x -= 250
            self.position.y -= 40

    def stamp_gifs(self, image, width, height, x, y):
        '''
        Method -- stamp_gifs
                  stamps the needed gifs for the game at specific
                  coordinates with set dimensions
        Parameters: x1/x2- the x coordinates of the image
                    y1/y2- the y coordinates of marble
                    width/hieght- x and y ranges of the image
        Return: the stamped image
        '''
        screen = Screen()
        screen.register_shape(image)
        t = Turtle(shape = image)
        t.penup()
        t.goto(x, y)
        t.stamp()
        t.penup()

        x1 = x - width/2
        y1 = y + height/2

        x2 = x1 + width
        y2 = y1 - height

        image = Gifs(x1=x1, y1=y1, x2=x2, y2=y2, width=width,
                     height=height, image=image)
        self.gifs_coords.append(image)
        return t.stamp()

    def quit(self):
        # stamps quit gif on board
        return self.stamp_gifs('quit.gif', 100, 56, 200, -325)

    def exit_game(self):
        # method to exit out of game if certain circumstances are reached
        self.score = 11
        self.hold_scores()
        self.quit_msg()
        # delays exiting out of turtle
        time.sleep(5)
        turtle.bye()
        

    def end_game(self, bulls):
        '''
        Method -- end_game
                  checks conditions for the player to exit from
                  the game and stamp lose or winner gifs
        Parameters: bulls - if bulls reaches the count of 4 it means
        the player has won the game and the winner gif is posted
        Return: loser or winner image depending on if game is won
        or lost by user
        '''
        self.hold_scores()
        if bulls == 4:
            return self.stamp_gifs('winner.gif', 1000, 1000, 0, 0)
        else:
            self.score = 11
            return self.stamp_gifs('Lose.gif', 1000, 1000, 0, 0)

    def leaderboard_error(self):
        # stamps leaderboard error gif if error occurs
        return self.stamp_gifs('leaderboard_error.gif', 1000, 1000, 0, 0)

    def quit_msg(self):
        # stamps quit message when user leaves game
        return self.stamp_gifs('quitmsg.gif', 1000, 1000, 0, 0)

    def file_error(self):
        # stamps file error gif if error occurs
        return self.stamp_gifs('file_error.gif', 1000, 1000, 0, 0)

    def checkbox(self):
        # stamps checkbox image for user to check answer if clicked
        return self.stamp_gifs('checkbutton.gif', 60, 60, -300, -350)

    def reset_button(self):
        # stamps x button image for user to reset guess if clicked
        return self.stamp_gifs('xbutton.gif', 60, 60,  -230, -350)

    def stamp_all_gifs(self):
        # stamps all needed images for gameboard
        self.quit()
        self.checkbox()
        self.reset_button()


    def get_user_guess_clicks(self, x, y):
        '''
        Method -- get_user_guess_clicks
                  takes click of user selections of marbles and
                  gets the color and places that color in order
                  of click within the guess circles. also pulls in
                  method to handle clicks on different gifs
        Parameters: x - x coordinate of user click
                    y - y coordinate of user click
        Return: none
        '''
        for choice_circle in self.input_row_coords:
            if choice_circle.click_in_choices(x, y):
                if choice_circle.color == 'white':
                    break
                current_row = self.choice_box[self.current_row]
                for i in range(len(current_row)):
                    if current_row[i].color == 'white':
                        self.position.x = current_row[i].x
                        self.position.y = current_row[i].y
                        self.draw_circle(choice_circle.color)
                        self.choice_box[self.current_row][i].color = \
                        choice_circle.color
                        self.position.x = choice_circle.x
                        self.position.y = choice_circle.y
                        choice_circle.color = 'white'
                        self.draw_circle()
                        break
                    else:
                        continue

        self.get_button_clicks(x, y)

    def reset_choices(self):
        '''
        Method -- reset_choices
                  resets the input circles the user clicks on
                  to white if the user selects the x button
        Parameters: none
        Return: none
        '''
        for i in range(len(self.input_row_coords)):
            if self.input_row_coords[i].color == 'white':
                self.input_row_coords[i].color = COLORS[i]
                self.set_positions(self.input_row_coords[i].x,
                                   self.input_row_coords[i].y)
                self.draw_circle(COLORS[i])

    def reset_current_row(self):
        '''
        Method -- reset_current_row
                  resets colors to white if
                  the current row the player is on
                  if the user clicks the x button
        Parameters: none
        Return: none
        '''

        for i in self.choice_box[self.current_row]:
            if i.color != 'white':
                i.color = 'white'
                self.set_positions(i.x, i.y)
                self.draw_circle(i.color)

    def reset_both_rows(self):
        '''
        Method -- reset_both_rows
                  takes both methods that reset current row
                  player is on and the choices the player
                  chooses from and resets both at the same time
                  when player clicks x button
        Parameters: none
        Return: none
        '''
        self.reset_choices()
        self.reset_current_row()

    def check_user_answer(self):
        '''
        Method -- check_user_answer
                  Takes the colors that the user selected and checks
                  it against the generated answer. If color is in the answer
                  adds count to cow and makes check circle red
                  but if color is also in correct
                  position it adds count to bulls and makes check
                  circle black
        Parameters: none
        Return: none
        '''
        user_guesses = [circle.color \
                        for circle in self.choice_box[self.current_row]]
        
        bulls, cows = game_logic(self.answer, user_guesses)
        count = 0
        for bull in range(bulls):
            current_guess = self.accuracy_of_guess[self.current_row]
            circle = current_guess[count]
            self.position.x = circle.x
            self.position.y = circle.y
            self.draw_circle('black', 3)
            count += 1
        for cow in range(cows):
            current_guess = self.accuracy_of_guess[self.current_row]
            circle = current_guess[count]
            self.position.x = circle.x
            self.position.y = circle.y
            self.draw_circle('red', 3)
            count += 1
        self.current_row += 1
        self.row_pointer(self.current_row)
        # print(self.answer)
        self.track_score = self.current_row
        self.reset_choices()
        if bulls == 4 or self.current_row > 9:
            self.end_game(bulls)

    def set_row(self, row):
        # sets row to the current play line to be used for pointer
        self.current_row = row

    def row_pointer(self, row):
        '''
        Method -- row_pointer
                  After game board is created, takes turtle
                  pointer and places it on each line
                  that the player is currently on
        Parameters: row - the current row the player is on
        Return: none
        '''
        if row > 9:
            return
        
        turtle.shape('classic')
        turtle.color('red')
        turtle.penup()
        turtle.showturtle()
        turtle.setpos(-325, 220 - row * 45)
        turtle.shapesize(2, 2, 2)


    def log_errors(self, error):
        '''
        Method -- log_errors
                  Method to log errors that occurs from the game
                  and writes into a new file
        Parameters: error - takes in the error the game outputs
        if there is any and writes it into a file with the current
        date and time to log the error
        Return: none
        '''
        try:
            with open('error_logging.txt', mode = 'a+') as file:
                date_time = datetime.datetime.now()
                file.write(str(date_time) + ':' + str(error) + '\n')
        # handles if file error/file not found
        except IOError as error:
            print(error)
            
    def hold_scores(self):
        '''
        Method -- hold_scores
                  takes user name and score receieved
                  in game and writes into txt file to hold
                  and written onto game board
        Parameters: none
        Return: none
        '''
        try:
            with open('leaderboard.txt', mode = 'a') as file:
                file.write((str(self.current_row + 1)) + ':' + \
                           self.player.strip().capitalize() + '\n')
                
        # logs and handles file error if leaderboard file isnt found 
        except IOError as error:
            self.log_errors(error)
            self.leaderboard_error()
            print(error)

    def write_header(self):
        '''
        Method -- write_header
                  writes the word Leaderboard as the header
                  for the right game box where scores are written
        Parameters: none
        Return: none
        '''
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(225,200)
        turtle.pencolor('yellow')
        turtle.pendown()
        turtle.write('Leaderboard', font = ('Arial', 25, 'normal'),
                     align = 'center')

    def write_leaderboard(self):
        '''
        Method -- write_leaderboard
                reads the held scores in the leaderboard files
                and writes the name and score into the leaderboard
                section of the game board while sorting scores
        Parameters: none
        Return: none
        '''
        try:
            with open('leaderboard.txt', mode = 'r') as file:
                names = [line.strip().split(':') for line in file]
                names.sort()
                turtle.hideturtle()
                turtle.speed(0)
                turtle.penup()
                turtle.goto(225,150)
                turtle.pencolor('blue')

                for name in names:
                    name = ':'.join(name)
                    turtle.write(name, font=('Arial', 15, 'normal'),
                                 align='Right')
                    turtle.right(90)
                    turtle.forward(50)
                    turtle.left(90)
        # handles and logs if there is error with file 
        except IOError as error:
            self.log_errors(error)
            print(error)


    def get_button_clicks(self, x, y):
        '''
        Method -- get_button_clicks
                Method for using clicks of the user to do actions
                in the game based on area of click
        Parameters: x- the x coordinate of the click
                    y- the y coordinate of the click
                    
        Return: none
        '''
        for image in self.gifs_coords:
            if image.click_in_gif(x, y):
                if image.image == 'checkbutton.gif':
                    self.check_user_answer()
                elif image.image == 'xbutton.gif':
                    self.reset_both_rows()
                elif image.image == 'quit.gif':
                    self.exit_game()

    def draw_gameboard(self):
        '''
        Method -- draw_gameboard
                  draws the entire game board including circles, squares
                  and headers out to make main shorter
        Parameters: none
        Return: none
        '''
        screen = turtle.Screen()
        screen.bgpic('wood.gif')
        self.make_screen()
        self.get_user_info()
        self.draw_mastermind(-125, 300)
        self.draw_square(-350, 250, 350, 500, color = "black")
        self.draw_square(50, 250, 350, 500, color = "blue")
        self.draw_square(-350, -257, 750, 130, color = "black")
        self.stamp_all_gifs()
        self.draw_choices()
        self.write_header()
        self.draw_ten_rows_of_all_circles()
        self.row_pointer(self.current_row)
