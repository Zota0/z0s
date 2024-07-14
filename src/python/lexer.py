import re


TOKEN_REGEXES = [
    (r"#log", "LOG"),
    (r"\(", "LPAREN"),  
    (r"\)", "RPAREN"),
    (r'"([^"]*)"', "STRING"), 
    (r"\d+", "NUMBER"),        
    (r"\s+", "WHITESPACE"),    
]

def tokenize(code):
    tokens = []
    pos = 0

    while pos < len(code):
        match = None

        for regex, token_type in TOKEN_REGEXES:
            match = re.match(regex, code[pos:])

            if match:
                value = match.group(0)

                if token_type != "WHITESPACE":  
                    tokens.append((token_type, value))

                pos += len(value)
                break

        if not match:  
            raise SyntaxError(f"Unexpected character at position {pos} '{code[pos]}'")

    return tokens




