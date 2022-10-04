"""
Solutions to module 2 - A calculator
Student: David Lood
Mail: david.lood.3070@student.uu.se
Reviewed by: David Meadon
Reviewed date: 14/9
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""


import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

# Functions:




def func(f, x):
    return f (x)

def log(x):
    if x <= 0:
        raise EvaluationError('Illegal argument')
    else:
        return math.log(x)


def fib(n):
    if n<0 or n.is_integer() == False:
        raise EvaluationError('Illegal argument')
    else:
        a, b = 0, 1
        for i in range(0, int(n)):
            a, b = b, a + b
        return a

def fac(n):
    if n<0 or n.is_integer() == False:
        raise EvaluationError('Illegal argument')
    else:
        result = 1
        for i in range(1, int(n)+1):
            result *= i
        return result

def mean(lst):
    return sum(lst)/len(lst)

function_l = {'sin': math.sin,
                  'cos': math.cos,
                  'exp': math.exp,
                  'log': log,
                  'fib': fib,
                  'fac': fac}

function_n = {'sum':sum,
              'max':max,
              'min':min,
              'mean':mean}

# Class:

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


# Syntax:

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end():
        pass
    else:
        raise SyntaxError('Expected end of line')
    return result




def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected variable after '='")
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/' or wtok.get_current() == '//':
        operation = wtok.get_current()
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        else:
            wtok.next()
            t_var = factor(wtok, variables)
            if t_var == 0:
                raise EvaluationError('Division by zero')
            else:
                if operation == '//':
                    result = result // t_var
                else:
                    result = result / t_var
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""



    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()


    elif wtok.get_current() in function_l:
        f = function_l[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == '(':
            result = func(f,factor(wtok, variables))  #Tokenizer unbalanced parantheses
        else:
            raise SyntaxError("Expected '('")


    elif wtok.get_current() in function_n:
        wtok.next()
        result = function_n[wtok.get_previous()](arglist(wtok, variables))



    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f"Undefined variable: '{wtok.get_current()}'")


    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1 * factor(wtok, variables)
    else:
        raise SyntaxError(
            "Expected number,word, '(' or '-'")
    return result



def arglist(wtok,variables):
   result = []
   if wtok.get_current() == '(':
       wtok.next()
       result.append(assignment(wtok, variables))
       while wtok.get_current() == ',' :
           wtok.next()
           result.append(assignment(wtok, variables))
       if wtok.get_current() == ')':
           wtok.next()
           return result
       else:
           raise SyntaxError("Expected ')' or ','")
   else:
       raise SyntaxError("Expected '('")

# main

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()


        elif wtok.get_current() == 'vars':
            for i in variables:
                print(f"{i}     : {variables[i]}")


        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except EvaluationError as EE:
                print("*** EvaluationError: ", EE)


            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()

