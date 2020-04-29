import thompsonConstruction

def displayOutput():
    # User input for regex and string.
    regexInput = input("Enter Regular Expression: ")
    userString = input("Enter string: ")

    result = (thompsonConstruction.match(regexInput, userString))
    if result:
        print("\nThe regular expression " + regexInput + " matches the string " + userString)
    else:
        print("\nThe regular expression " + regexInput + " does not match the string " + userString)