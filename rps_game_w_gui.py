# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:07:13 2020

@author: Keith
"""
# todo: add best of option; will need score tracking 
########################
import random
from enum import Enum
import tkinter as tk

class Choice(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

# user input function
def user_choice():
    choice = 1

    while choice == 1:
        user = input('Rock (0), Paper (1), or Scissors (2): ')
        if user == str(Choice.Rock.value):
            print('Your Choice: Rock')
            choice+=1
        elif user == str(Choice.Paper.value):
            print('Your Choice: Paper')
            choice+=1
        elif user == str(Choice.Scissors.value):             
            print('Your Choice: Scissors')
            choice+=1
        else:
            print('Please select a valid input')
      
    return int(user)

# computer input function    
def comp_choice():
    comp = random.randint(0, 2)
    
    if comp == Choice.Rock.value:
            print('My Choice: Rock')

    elif comp == Choice.Paper.value:
            print('My Choice: Paper')
    elif comp == Choice.Scissors.value:             
            print('My Choice: Scissors')
            
    return (comp)

# rps game function            
def rps():
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Rock Paper Scissors")
    play = input('Do you wish to challenge me? (Y/N): ')
    while True:
        if play == 'Y' or play == 'y':   
            while play == 'Y' or play == 'y':
                user = user_choice()
                comp = comp_choice()
                if user == Choice.Rock.value:
                    if comp == Choice.Rock.value:
                        print('Tie')
                    elif comp == Choice.Paper.value:
                        print('You Lose!')
                    else:
                        print('You Win!')
                if user == Choice.Paper.value:
                    if comp == Choice.Paper.value:
                        print('Tie')
                    elif comp == Choice.Scissors.value:
                        print('You Lose!')
                    else:
                        print('You Win!')
                if user == Choice.Scissors.value:
                    if comp == Choice.Scissors.value:
                        print('Tie')
                    elif comp == Choice.Rock.value:
                        print('You Lose!')
                    else:
                        print('You Win!')
                      
                play = input('Do you wish to challenge me again? (Y/N): ')
        elif play == 'N' or play == 'n':
             print('Thank you for playing!')
             break
        else:
             print('Only Y or N please')
             play = input('Do you wish to challenge me? (Y/N): ')

    window.mainloop()
