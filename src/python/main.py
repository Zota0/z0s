import os
import listener as listen
from lexer import tokenize
from parser import parse
from eval import Evaluator

if __name__ == "__main__":

    print('\n')

    code = listen.body

    if code:

        tokens = tokenize(code)
        ast = parse(tokens)
        evaluator = Evaluator()
        start = evaluator.evaluate(ast)
        
        print('\n')
        print('__^__'* int(os.get_terminal_size()[0] / 5) + "\n\n")
        print("Tokens:\n\t", tokens, end="\n\n")
        print("Abstract Syntax Tree:\n\t", ast, end="\n\n")
        print("Evaluated AST:\n\t", start, end="\n\n")

    else:
        print("No code provided: file_reader is possibly turned off or there was connection error")
