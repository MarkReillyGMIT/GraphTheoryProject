#Mark Reilly
#Classes used in thompsons construction

class State:
    # Every state has 0, 1, or 2 edges from it.
    edges = []

    #Label for the arrows, None means epsilon.
    label = None

    #Create a constructor for the class
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label


class Fragment:
    #Start State of NFA fragment
    start = None
    #Accept State of NFA fragent
    accept = None

    #Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    #Convert the input to a stack list.
    infix = list(infix)[::-1]

    #Operators Stack
    opers = []

    #Output lists.
    postfix = []

    #Operator precedence
    prec = {'*': 100, '|': 80, '.': 60, ')': 40, '(': 20}
    #Loop through one character at a time.
    while infix:
        #pop a character from the list
        c = infix.pop()
    #Decide what to do based on the character.
        if c == '(':
            #Push and open brcket to opers stack
            opers.append(c)
        elif c == ')':
            #Pop the operators stack until u find an opening bracket
            while opers[-1] != '(':
                postfix.append(opers.pop())
            #Get rid of the "("
            opers.pop()
        elif c in prec:
            #Push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            #Push c to the opers stack.
            opers.append(c)
        else:
            #Typically we just push the character to the output
            postfix.append(c)

    #Pop all cahracters to the output
    while opers:
        postfix.append(opers.pop())

    #Convert output list to string.
    return ''.join(postfix)


def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if c == '.':
            #Pop two fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            #point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            #Create new instance of fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
            #Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)

        elif c == '|':
            #Pop two fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            #Create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            #Point the old accept states at the new one 
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            #Create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
            #Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)
        elif c == '*':
            #Pop a single fragment of the stack
            frag = nfa_stack.pop()
            #Create new start and accept states
            accept = State()
            start = State(edges = [frag.start, accept])
            #Point the arrows 
            frag.accept.edges=[frag.start, accept]
            #Create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
            #Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)
        else:
            #Create new start and accept states
            accept = State()
            start = State(label=c, edges=[accept])
            #Create new instance of fragment to represent the new NFA
            newfrag = Fragment(start, accept)
            #Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)
           
    return nfa_stack.pop()

def match(regex, s):
    #This function will return true if and only if the regular expression 
    # regex (fully) matches the string s,it returns False otherwise

    #Compile the regular expression into an NFA.
    nfa = regex_compile(regex)
    #Ask the NFA if it mathces the String s.
    return  nfa 

print(match("a.b|b*","bbbbbbbbb"))
