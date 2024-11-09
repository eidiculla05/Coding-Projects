# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    '''
    This function is setting up two new attributes for an object created from the class. 
    '''
    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.courses=[] # Initalizing an empty list to store courses 

    '''
    This function returns the name of the instructor. 
    '''
    def get_name(self):
        #--- YOUR CODE STARTS HERE
        return self.name  
   
    '''
    This function will set the name of the instructor to a new name if the new name is a non-empty string.
    '''
    def set_name(self, new_name):
        #--- YOUR CODE STARTS HERE
        if new_name != "":
            self.name = new_name # Sets old name to new name

    '''
    This function returns the list of the courses taught by the instructor if it exists in the list
    '''
    def get_courses(self):
        #--- YOUR CODE STARTS HERE
        return self.courses 

    '''
    This function removes the course from the list of courses, if it exists in the list
    '''
    def remove_course(self, course):
        #--- YOUR CODE STARTS HERE
        if course in self.courses:
            self.courses.remove(course) # Removes course from list if in list 

    '''
    This function adds a course to the list if the course is not in the list.
    '''
    def add_course(self,course):
        #--- YOUR CODE STARTS HERE
        if course not in self.courses: 
            self.courses.append(course) # Adds course to list if not in course list 


# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """
    '''
    This function initializes the instance of the pantry class with an empty dictionary 
    '''
    def __init__(self):
        self.items = {}  
    
    '''
    This function returns a string for instances of the panty class with their stock
    '''
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return 'I am a Pantry object, my current stock is '+str(self.items)
    
    '''
    This function adds the quantity of the item and returns a string with the current stock of the item 
    '''
    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item not in self.items: # If the item is not in the pantry, we set the number of items to 0
            self.items[item]=0.0

        self.items[item]+=qty * 1.0
        return "Pantry Stock for "+str(item)+": "+ str(self.items[item])

    '''
    This function returns multiple strings based on the item in the pantry.
    If the item is not in the pantry, it returns a string that says it is not in the pantry.
    If the quantity is greater than the current stock, it returns a string that says we need to add more of that item to the shopping list.
    The last return statement alets you that you only have a certain amount of stock left for that specific item.
    '''
    def get_item(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item not in self.items:
            return "You don't have " +item 
        elif qty >= self.items[item]:
            self.items[item] = 0.0
            return "Add " + item + " to your shopping list!"
        else: 
            self.items[item] -= qty
            return "You have " +str(self.items[item])+" of "+str(item) +" left"
        
    '''
    This function moves the entire stock from other_pantry to the original pantry.
    Items that have zero stock left are not moved to the orignial pantry.
    '''
    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE
        if item in self.items and item in other_pantry.items:
            self.stock_pantry(item, other_pantry.items[item])
            other_pantry.items[item] = 0.0

                
                 


# -------- SECTION 3
class Player:
    """
        >>> p1 = Player('Susy')
        >>> print(p1)
        No game records for Susy
        >>> p1.update_loss()
        >>> p1
        *Game records for Susy*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
        >>> p1.update_win(5)
        >>> p1.update_win(2)
        >>> p1
        *Game records for Susy*
        Total games: 3
        Games won: 2
        Games lost: 1
        Best game: 2 attempts
    """

    '''
    This function initializes an object with several attributes about the players performance. 
    '''
    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.games_played = 0
        self.games_wins = 0
        self.games_loss = 0
        self.leastNumberofAttempts = None 

    
    '''
    This function the amount of wins a player has by 1 and updates the players best game based on the amount of attempts they have had. 
    '''
    def update_win(self, att):
        #--- YOUR CODE STARTS HERE
        self.games_wins += 1 # Adds 1 to amount of wins
        if self.leastNumberofAttempts==None or att < self.leastNumberofAttempts:
            self.leastNumberofAttempts=att # Sets least number of attempts equal to their attempt to keep track of their best game
        self.games_played += 1

    '''
    This function increases the amount of games lost by a player by 1 and updates the amount of games played by 1.
    '''
    def update_loss(self):
        #--- YOUR CODE STARTS HERE
        self.games_loss += 1 # Adds 1 to the amount of losses for a given player
        self.games_played += 1 # Adds 1 to the amount of games player for a given player

        
    
    '''
    This function returns many strings.
    When no games have been played, the function returns that there are no game records for the player.
    Otherwise, it returns the players stats which includes their total games, games own, games lost, and their best game. 
    '''
    def __str__(self):
        #--- YOUR CODE STARTS HERE
        if self.games_played == 0: # If player has not played any games, return "No game records for that person"
            return "No game records for "+self.name
        elif self.leastNumberofAttempts==None:
            return "*Game records for "+self.name+"*\n"+"Total games: "+str(self.games_played) +"\n"+"Games won: "+str(self.games_wins) +"\n" + "Games lost: "+str( self.games_loss) +"\n" + "Best game: "+str(self.leastNumberofAttempts)
        else:
            return "*Game records for "+self.name+"*\n"+"Total games: "+str(self.games_played) +"\n"+"Games won: "+str(self.games_wins) +"\n" + "Games lost: "+str( self.games_loss) +"\n" + "Best game: "+str(self.leastNumberofAttempts)+" attempts"

        
    __repr__=__str__

class Wordle:
    """
        >>> p1 = Player('Susy')
        >>> p2 = Player('Taylor')
        >>> w1 = Wordle(p1, 'water')
        >>> w2 = Wordle(p2, 'cloud')
        >>> w3 = Wordle(p1, 'jewel')
        >>> w1.play('camel')
        '_A_E_'
        >>> w1.play('ranes')
        'rA_E_'
        >>> w1.play('baner')
        '_A_ER'
        >>> w1.play('pacer')
        '_A_ER'
        >>> w1.play('water')
        'You won the game'
        >>> w1.play('rocks')
        'Game over'
        >>> w1.play('other')
        'Game over'
        >>> w3.play('beast')
        '_E___'
        >>> w3.play('peace')
        '_E__e'
        >>> w3.play('keeks')
        '_Ee__'
        >>> w3.play('jewel')
        'You won the game'
        >>> w2.play('classes')
        'Guess must be 5 letters long'
        >>> w2.play('cs132')
        'Guess must be all letters'
        >>> w2.play('audio')
        '_ud_o'
        >>> w2.play('kudos')
        '_udo_'
        >>> w2.play('would')
        '_oulD'
        >>> w2.play('bound')
        'The word was cloud'
        >>> w2.play('cloud')
        'Game over'
        >>> p1
        *Game records for Susy*
        Total games: 2
        Games won: 2
        Games lost: 0
        Best game: 4 attempts
        >>> p2
        *Game records for Taylor*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
    """

    '''
    This function initializes an object with several attributes to keep track of the game. 
    '''
    def __init__(self, player, word):
        #--- YOUR CODE STARTS HERE
        self.player = player
        self.word = word 
        self.gameover = False 
        Wordle.att=6 # Maximums number of attempts allowd for the game
        self.attempts=0 # Initialized 0 has the current number of attempts for the player

    
    '''
    This function revises all characters in the users guess and returns strings based on their inputs.
    Then iterates through the users input and checks each character to see if they are in the right place or not and joins the characters back into a string and returns the string.
    '''
    def process_guess(self, guess):
        #--- YOUR CODE STARTS HERE
        if len(guess) != 5: # If users input is not 5 characters long
            return "Guess must be 5 letters long"
        elif not guess.isalpha(): # If users unput was not all letters
            return "Guess must be all letters"
        else:
            guess=guess.lower()
            self.word=self.word.lower()
            guess=list(guess)
            for i in range(0,len(guess)): # Iterates through each charcter in the users input
                if guess[i] in self.word: # Checks if the guessed letter is in the target word
                    if guess[i]==self.word[i]:
                        guess[i]=guess[i].upper() # If the letter in the guess is in the right place, provide that letter as uppercase
                    else:
                        guess[i]=guess[i].lower() # If the letter in the guess is not in the right place, provide that letter as lowercase
                else: 
                    guess[i]="_" # If the letter in the guess isn't in the word at all, provide "_"
        guess="".join(guess) # Joins the list of characters back into a string and returns it
        return guess


    '''
    Invokes process_guess(self, name)
    This function handles each attempt of the game and updates the stats for the player and gives the player feedback such as returning "Game Over" when the users attemps exceeds 6 attempts.
    '''
    def play(self, guess):
        #--- YOUR CODE STARTS HERE
            self.attempts+=1
            guess=self.process_guess(guess)
            
            if guess != self.word.upper() and self.attempts==Wordle.att: # If the users guess' were not the correct word and the amount of attempts they used equals 6, it returns the correct word
                self.player.update_loss()
                return "The word was "+str(self.word)
            elif self.attempts>Wordle.att: # If the users attempts exceeds 6, it returns game over
                return "Game over"
            elif guess==self.word.upper():
                self.player.update_win(self.attempts)
                self.attempts=Wordle.att
                return "You won the game" # Reutns You won the game if users guess matches the corect word
            else:
                return guess
            
           
            
            
    

# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''

    '''
    Initializes the class with two points, point 1 and point 2
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2
        

    #--- YOUR CODE STARTS HERE
    '''
    This function declares a variable called distance_formula where the distance formula is stored in this variable and returns this variable.
    It will also round the potential outputs of the formula to 3 decimal places. 
    '''
    @property
    def getDistance(self):
        distance_formula = math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2) # Setting distance formula equal to formula 
        distance_formula= round(distance_formula, 3) # Rounds to 3 decimal places 
        return distance_formula 
        
       
    
    #--- YOUR CODE STARTS HERE
    '''
    This function retuns the slop based on the slope equation.
    If the slope exists we round the slope to 3 decimal places.
    If the slope does not exist we return infinity has a float.
    '''
    @property
    def getSlope(self):
        slope=None
        if self.point2.x-self.point1.x!=0: # If X2 - X1 is 0, we get a undefined value, so we need to make sure it is not 0 
            slope = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

        if slope!=None: # If x2 - x1 does not equal 0
            return round(slope, 3) 
        else: # If x2 - X1 equals 0
            return float('Infinity') 
        
        


    #--- YOUR CODE CONTINUES HERE
    '''
    This function is used compute the interception b.
    If the slope equals 0, it will return y = b, because if the slope is 0 then m * x = 0.
    If the slope >0, the function will return y = mx + b
    '''
    def __str__(self):
        b = self.point1.y - (self.getSlope * self.point1.x)
        b=round(b, 3)

        if self.getSlope == float("Infinity"):
            return "Undefined"
        elif self.getSlope == 0: # If slope 0, there is no input for mx, so we are just left with b
            return 'y = ' + str(b)
        else:
            return 'y = ' + str(self.getSlope)+"x + " + str(b) # If slope does not equal 0, we have input for mx and b
        
    __repr__=__str__


    '''
    This function retuns a new line object where (x,y) attributes of every Point2D object are multipled by an integer. 
    Returns None if it is a non-integer value.
    '''
    def __mul__(self,integer):
        if isinstance(integer,int): # Makes sure its an integer
            return Line(Point2D(self.point1.x*integer,self.point1.y*integer),Point2D(self.point2.x*integer,self.point2.y*integer)) # Made a line object with two new point 2D objects which are multiplied by integers 
        else:
            return None # If not an integer, return none
        
    '''
    This function returns true if the point object lies on the line object. 
    Returns false if the point object does not lie on the line object.
    If the slope is undefined the function will return false.
    '''
    def __contains__(self,point):
        if self.getSlope==float('Infinity'): 
            return False 
        b = self.point1.y - (self.getSlope * self.point1.x) # Calculates value for b
        b=round(b, 3)
        if isinstance(point,Point2D):
            return math.isclose(self.getSlope*point.x+b,point.y) # Cannot use == so we use isclose() to determine if y = mx+b is true
        else:
            return False
        




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #Run tests per function - Uncomment the next line to run doctest by function. Replace Pantry with the name of the class you want to test
    doctest.run_docstring_examples(Point2D, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()