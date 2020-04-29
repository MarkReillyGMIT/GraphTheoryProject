# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

import thompsonConstruction, MainMenu, getopt, sys, Result
"""
Prompts user for input of Regex and String, returns if the Regex matches the string or not.
"""
#Reference: https://www.geeksforgeeks.org/command-line-arguments-in-python/
# Remove 1st argument from the 
# list of command line arguments 
argumentList = sys.argv[1:] 
  
# Options 
options = "hmor:"
  
# Long options 
long_options = ["Help", "My_file", "Output =", "Run"] 
  
try: 
    # Parsing argument 
    arguments, values = getopt.getopt(argumentList, options, long_options) 
      
    # checking each argument 
    for currentArgument, currentValue in arguments: 
  
        if currentArgument in ("-h", "--Help"):
            # Prints Main Menu .
            print("|====================================|")
            print("|               Help                 |")
            print("| Enter main.py --Run to Run program |")
            print("| Enter a regex expression           |")
            print("| Enter a string                     |")
            print("|====================================|")
              
        elif currentArgument in ("-m", "--My_file"): 
            print ("Displaying file_name:", sys.argv[0]) 
              
        elif currentArgument in ("-o", "--Output"): 
            print (("Enabling special output mode (% s)") % (currentValue)) 
        elif currentArgument in ("-r", "--Run"):
            # Prints Main Menu .
            MainMenu.mainMenu()
            Result.displayOutput()              
except getopt.error as err: 
    # output error, and return with an error code 
    print (str(err)) 
