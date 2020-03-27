# Author: Mark Reilly
# Graph Theory Project Thompsons Construction

from State_Fragment import State, Fragment
from shunt import shunt

def compile(infix):
    """Return NFA fragment representing the infix regular expression. """
    #Convert infix to postfix.
    postfix = shunt(infix)
    ##Make postfix a stack of characters
    postfix = list(postfix)[::-1]
    
    #A stack for NFA fragments
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
            #The new start state is frag2's.
            start = frag2.start
            #The new accept state is frag1's.
            accept = frag1.accept
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
        elif c == '*':
            #Pop a single fragment of the stack
            frag = nfa_stack.pop()
            #Create new start and accept states
            accept = State()
            start = State(edges = [frag.start, accept])
            #Point the arrows 
            frag.accept.edges=[frag.start, accept]
        elif c == '?':
            #Pop a single fragment of the stack
            frag = nfa_stack.pop()
            #Create new start and accept states
            accept = State()
            start = State(edges = [frag.start, accept])
            #Point old accept state to new accept state
            frag.accept.edges =(accept, accept)
        elif c == '+':
            #Pop a single fragment of the stack
            frag = nfa_stack.pop()
            #Create new start and accept states
            accept = State()
            start = State(edges=[frag.start])
            #Point the arrows 
            frag.accept.edges=[frag.start, accept]
        else:
            #Create new start and accept states
            accept = State()
            start = State(label=c, edges=[accept])

        #Create new instance of fragment to represent the new NFA
        newfrag = Fragment(start, accept)
        
        #Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)
           
    return nfa_stack.pop()
