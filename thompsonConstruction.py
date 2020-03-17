# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

""" Shunting Yard Algorithm converts infix regular expression to postfix """

def shunt(infix):
    specials ={'?': 70, '+': 60, '*' : 50, '.' : 40, '|' : 30}

    postfix = ""
    stack = ""

    # Loop through the string one character at a time
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack [-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in specials: 
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c

        else:
            postfix = postfix + c

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]

    return postfix
