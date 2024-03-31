import re

def tokenize_code(file_name):
    local_lexeme_count = 0
    code_tokens = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            tokens = re.findall(r'"[^"]*"|\b\d+(?:\.\d+)?\b|\w+|\(|\)|\+=|==|-=|\*=|/=|%=|//=|\**=|&=|\|=|\^=|>>=|<<=|!=|>=|<=|[-.,!?;:`^~|@&#{}()+<>*%/\]\[]+|(?<!=)=|:', line)

            for token in tokens:
                if token in ('def', 'return', 'if', 'elif', 'else', 'print', 'and', 'or', 'not', 'is', 'in'
                             'False', 'await', 'import', 'pass', 'None', 'break', 'except', 'raise',
                             'True', 'class', 'finally', 'continue', 'for', 'lambda', 'try',
                             'as', 'from', 'nonlocal', 'while', 'assert', 'del', 'global',
                             'with', 'async', 'yield'):
                    token_type = 'Keywords'
                elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
                    token_type = 'Identifiers'
                elif re.match(r'"[^"]*"', token):
                    token_type = 'Literals'
                elif re.match(r'\d+', token):
                    token_type = 'Literals'
                elif token in ('+', '-', '*', '/', '=', '==', '<', '>', '**', '%', '++',
                               '--', '//', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=',
                               '|=', '^=', '>>=', '<<=', '!=', '>=', '<=', '&', '|', '^', '<<', '>>', '~'):
                    token_type = 'Operators'
                elif token in ('(', ')', ':', ',', '"', '.', '[', ']', '{', '}', '`', ';', "'", '@', '#'):
                    token_type = 'Separators'
                else:
                    token_type = 'Other'

                code_tokens.append((token, token_type))
                local_lexeme_count += 1

        return code_tokens, local_lexeme_count

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Tokenize the code
token_list, lexeme_count = tokenize_code('testCode.txt')

# Print lexemes with types
for lexeme, lexeme_type in token_list:
    print(f"Lexeme: {lexeme} Type: {lexeme_type}")

print("Lexeme count:", lexeme_count)
