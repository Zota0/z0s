from lexer import tokenize

class LogNode:
    def __init__(self, value):
        self.value = value

def parse(tokens):
    """Parses a list of tokens into an AST."""
    if not tokens:
        return None

    ast = []
    current_token = 0

    while current_token < len(tokens):

        token_type, value = tokens[current_token]

        if token_type == "LOG":
            
            if current_token + 1 < len(tokens) and tokens[current_token + 1][0] == "LPAREN":
                current_token += 2  
                log_argument = []

                while current_token < len(tokens) and tokens[current_token][0] != "RPAREN":
                    log_argument.append(tokens[current_token][1])
                    current_token += 1
                
                if current_token < len(tokens) and tokens[current_token][0] == "RPAREN":
                    ast.append(LogNode(" ".join(log_argument)))  
                    current_token += 1

                else:
                    raise SyntaxError("Missing closing parenthesis ')' for '#log'")

            else:
                raise SyntaxError("Missing opening parenthesis '(' for '#log'")

        else:
            raise SyntaxError(f"Unexpected token: {value}")

    return ast




