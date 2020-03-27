# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

import thompsonConstruction, MainMenu

# Print program header.
MainMenu.mainMenu()

# User input for regex and string.
userRegex = input("Enter Regular Expression: ")
userString = input("Enter string: ")

# Calls match from regex script on users regex and string.
result = (thompsonConstruction.match(userRegex, userString))
if result:
    print("\nThe regular expression " + userRegex + " matches the string " + userString)
else:
    print("\nThe regular expression" + userRegex + " does not match the string " + userString)
