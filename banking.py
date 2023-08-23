# -*- coding: utf-8 -*-
"""
Goblins Magical Loan System
A sophisticated system for approving loans to wizards starting businesses.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: David Corcoran
"""
__version__ = 4

'''
The Goblin Loan System allows a user to insert their name into the program.
In return, the user will receive a number representing their loan rating.
The higher the rating, the bigger the loan a user can take out.
'''

#(1) main: Calls the other functions and controls data flow
def main():
    print_introduction()
    name = input_name()
    user_rating = calculate_rating(name)
    print_rating(user_rating)
    loan_amount = input_loan_amount()
    print_loan_availability(user_rating, loan_amount)
    print_conclusion()
    '''
    Main function that calls all the other functions and provides
    an interactive loan processing experience.
        
    Args:
        None
    Returns:
        None
    '''

#(2) print_introduction: Print a welcome message
def print_introduction():
    '''
    Args: None
    Prints: An introduction and welcome message
    '''
    print("* 1) Introduction ********************************\nWelcome to the Goblins Magical Loan System!\nPlease answer the following questions truthfully,\nand we will process your loan request.\nImposters will be fed to the dragons.")


#(3) input_name: Get the user's name
def input_name():
    '''
    Args:None
    Input: User inputs their full name
    Returns: Name that the user inputted
    Prints: A welcome message specific to the user
    '''
    name = input("* 2) Name ****************************************\nPlease enter your full, legal name.\nMagical verification will verify your identity.\nWrite your name and press enter: ")
    print("Welcome, " + str(name) + "!")
    return name


#(4) calculate_rating: Get the user's rating (by Grindlehook)
# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
# Do NOT change the following function definition
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is a little delicate, and will break after being called once.
    
    NOTE (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.
    
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
# Do NOT change the preceding function definition
    
#(5) print_rating: Print the user's rating
def print_rating(rating):
    '''
    Args: rating (int)
    Prints: rating (string)
    '''
    print("* 3) Rating **************************************\nYour user rating has been calculated.\nYour rating is: " + str(rating) + "/10 points")


#(6) input_loan_amount: Get the user's desired loan amount
def input_loan_amount():
    '''
    Args: None
    Input: User inputs their requested loan
    Returns: Loan amount as an integer
    '''
    loan_amount = input("* 4) Loan ****************************************\nLoans are made based on your customer rating.\nHowever, you can request a loan of any size.\nHow many galleons do you want?\nWrite your loan amount: ")
    return int(loan_amount)

    
#(7) print_loan_availability: Print whether the loan is available
def print_loan_availability(user_rating, loan_amount):
    '''
    Args: rating (int), loan_amount (int)
    Returns: True if loan is available, False if loan is unavailable
    '''
    def test_loan(user_rating, loan_amount):
        if ((user_rating ** 2) * 100) >= loan_amount:
            return True
        else:
            return False
    if test_loan(user_rating, loan_amount) == True:
        print("* 5) Available? **********************************\nYour loan request has been evaluated.\nLoan available: True")
    else:
        print("* 5) Available? **********************************\nYour loan request has been evaluated.\nLoan available: False")


#(8) test_loan: Determines if the loan is available
def test_loan(user_rating, loan_amount):
    '''
    Args: rating (int), loan_amount (int)
    Returns: True if loan_amount <= (user_rating ** 2) * 100, False if loan_amount is greater
    '''
    if ((user_rating ** 2) * 100) >= loan_amount:
        return True
    else:
        return False
        
        
#(9) print_conclusion: Prints a thank-you message.
def print_conclusion():
    '''
    Args: None
    Prints: A thank you message to the user
    '''
    print("* 6) Conclusion **********************************\nThanks for using Goblins Magical Loan System!\nBest of luck with your new small business.\nWe hope you'll use Goblins for all your future\nbanking needs. Remember: Fortius Quo Fidelius!\n**************************************************")


# Call main function only if this file is being run directly
#   as opposed to being run by `test_my_solution.py`
if __name__=='__main__':
    main()