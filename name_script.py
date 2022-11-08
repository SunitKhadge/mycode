#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - Hello , < Name> ! Happy <day of the week>!"""

def main():

    # collect string input from the user
    user_name = input("Please enter your name: ")
    
    user_input_dayofweek = input("Please enter day of the week: ")
    ## the line below creates a single string that is passed to print()
    
    # print() can be given a series of objects separated by a comma
    # print("Hello, " , user_name ,"! Happy ", user_input_dayofweek, " !")
    
    print(f"Hello, {user_name}! Happy {user_input_dayofweek}!")

main()
