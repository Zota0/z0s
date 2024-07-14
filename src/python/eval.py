import parser

class Evaluator:

    def evaluate(self, ast):

        for node in ast:

            if isinstance(node, parser.LogNode):
                print((node.value).replace('"', "").replace("'", ""))