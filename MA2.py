"""
Solutions to module 2 - A calculator
Student: Nils Wikström
Mail: nils.wikstrom@outlook.com
Reviewed by: Johan Mårtensson   
Reviewed date: 2022-04-21
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

from ast import expr
import math
from statistics import mean
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def fac(n):
    if n.is_integer() and n > 0:
        if n==0:
            return 1
        else:
            return n*fac(n-1)
    else:
        raise EvaluationError('Please use a strictly positive integer')

def fib(n):
    if n.is_integer() and n > 0: 
        if n==0:
            return 0
        elif n==1:
            return 1
        else :
            return fib(n-1) + fib(n-2)
    else:
        raise EvaluationError('Please use a strictly positive integer')

def loge(x):
    if x.is_integer() and x>0:
        return math.log(x)
    else:
        raise EvaluationError('Please use a strictly positive integer')




def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok,variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError('Expected variable after "="')
        wtok.next()
        if wtok.get_current() == '' or wtok.get_current() == '=' or wtok.get_current() == ')':
            pass
        else:
            raise SyntaxError('Please only assign variable after =')
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    if wtok.get_current() == '-': #Realized that this might not be necessary if a recursive argument is used in factor but went with it anyway :)
        wtok.next()
        result = -term(wtok,variables)
    else:
        result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    if wtok.get_current() == '**' or wtok.get_current() == '//':
        raise SyntaxError('Please do not put multiple operators in a row')
    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            temp = factor(wtok,variables)
            if int(temp) == 0:
                raise EvaluationError("Division by zero")
            else:
                result = result / temp
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {'exp': math.exp, 'sin':math.sin, 'cos':math.cos, 'log':loge, 'fac':fac, 'fib':fib, 'tanh':math.tanh}
    function_n = {'sum': sum, 'max':max, 'min':min, 'mean':mean}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        elif wtok.get_current() in function_1:
            funk = wtok.get_current()
            wtok.next()
            if wtok.get_current() != '(':
                raise SyntaxError('Expected "("')
            else:
                val = factor(wtok,variables)
                result = function_1[funk](val)
        
        elif wtok.get_current() in function_n:
            funk = wtok.get_current()
            wtok.next()
            result = function_n[funk](arglist(wtok,variables))
        else:
            raise EvaluationError('Unassigned variable or unknown function')
    
    elif wtok.get_current() == '-':
            wtok.next()
            if wtok.is_number():
                result = -float(wtok.get_current())
            else:
                raise SyntaxError('Too many operators in a row')
    
    elif wtok.get_current() == '+':
        wtok.next()
        if wtok.get_current() == '-': 
            result = float(wtok.get_current())
        else:
            raise SyntaxError('Too many operators in a row')
    else:
        raise SyntaxError(
            "Expected number, name or '('")  
    return result

def arglist(wtok,variables):
    result = []
    if wtok.get_current() == '(':
        while wtok.get_current() != ')':
            wtok.next()
            result.append(assignment(wtok, variables))

    return result


         
def main():
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    while True:
        line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
            
            except EvaluationError as ee:
                print("***Evaluation error: ", ee)
 

if __name__ == "__main__":
    main()
