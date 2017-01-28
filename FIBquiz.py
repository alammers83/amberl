# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# easy FIBs and answers


easy_fib = ["A", "___1___","is created with the def keyword. You specify the inputs a","___2___", 
            "takes by adding", "___3___", "separated by commas between the parentheses.", "___4___","s" ,"by default return", "___5___",
            "if you don't specify the value to return." ,"___6___" ,
            "can be standard data types such as string, number, dictionary,tuple, and", "___7___", "or can be more complicated such as objects and lambda functions."]
easy_answers = ["function", "function", "variables", "function", "none", "variables", "lists"]

# medium FIBs and answers.
medium_fib = ["Beyond a wholesome discipline, be gentle with",
              "___1___", ".You are a child of the universe no less than the"
              ,"___2___", "and stars.", "And whether or not it is clear to you" "," "no","___3___", "the", "___4___",
              "is unfolding as it should." , "___5___", "be at peace with", "___6___", "whatever you conceive",
              "___7___", "to be."]
medium_answers = ["yourself", "trees", "doubt", "universe", "Therefore", "God",
                  "Him"]


# hard FIBs and answers.
hard_fib = ["I love you without knowing how, or", "___1___", "or from where"
            "I love you", "___2___", "without problems or pride:"
            "I love you like this because I do not know any other way to", "___3___",
             "except in this" , "___4___" , "in which I am" , "___5___", "nor are", "___6___",
            "so close that your hand upon my", "___7___", "is mine. So close that your eyes close with my",
            "___8___"]
hard_answers = ["when", "directly", "love", "form", "not", "you", "chest", "dreams"]
                 


def load_fib_difficulty():
    # Asks the user for a difficulty level and outputs that level's data
   
    level = input("\nPlease select a difficulty level "
                      "(easy, medium, or hard): ")
    if level.lower() == "easy":
        return easy_fib, easy_answers, "easy"
    elif level.lower() == "medium":
        return medium_fib, medium_answers, "medium"
    elif level.lower() == "hard":
        return hard_fib, hard_answers, "hard"
    else:
        print ("Invalid difficulty level")
        return load_fib_difficulty()


def remove_spaces_before_punc(fib_string):
    # Removes spaces before punctuation.
    
    fib_string = fib_string.replace(" .", ".")
    fib_string = fib_string.replace(" !", "!")
    return fib_string


def provide_link(level):
    # Provides a link for more information

    if level == "easy":
       return "https://www.udacity.com/"
    if level == "medium":
        return "https://en.wikipedia.org/wiki/Desiderata"
    if level == "hard":
        return "http://hellopoetry.com/pablo-neruda/"
           

def guess_check(blank_number, fib, answers, answer):
    """Asks the user for a guess. If correct, moves to the next blank.
    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect.
    """
    blank = "___" + str(blank_number) + "___"
    guess = input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        fib[fib.index(blank)] = answer
        print (remove_spaces_before_punc(" ".join(fib)) + "\n")
        blank_number += 1
        return blank_number
    else:
        print ("WRONG. Please try again.\n")
        return guess_check(blank_number, fib, answers, answer)


def play_game():
    """Plays a full game of fill-in-the-blanks.
    Displays the chosen empty fill-in-the-blank. Game ends with a printed
    congratulations statement.
    """
    fib, answers, level = load_fib_difficulty()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print (remove_spaces_before_punc(" ".join(fib)) + "\n")

    blank_number = 1
    for answer in answers:
        blank_number = guess_check(blank_number, fib, answers, answer)

    print ("Congratulations, you have filled in all of the blanks! Here is the"
           " link to the call:")
    print (provide_link(level) + "\n")

play_game()