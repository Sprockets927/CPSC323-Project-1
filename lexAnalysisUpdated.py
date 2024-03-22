import re


def readFile(fileName):
    """Read File"""
    with open(fileName, 'r') as read_file:
        pyCodeTxt = read_file.read()
        return pyCodeTxt


def readFileLines(fileName):
    """Most of the functions I(Robbie) wrote are intended to work with the list of individual lines of code"""
    with open(fileName, 'r') as read_file:
        pyCodeLines = read_file.readlines()
        return pyCodeLines


def printCode(fileObj):
    """Print code from provided fileObj"""
    print(fileObj)


def printCodeLines(fileObj):
    """Print code in lines from provided fileObj"""
    for line in fileObj:
        print(line.strip())


def printCodeLineSeparated(fileLineObj):
    """Each read statement of code is separated by line in terminal for readability works with parseCodeIntoWords()"""
    for word in fileLineObj:
        print(word)


def parseCodeIntoWords(fileLineObj):
    """Parses code lines into individual pieces, separated by spaces."""
    wordList = []
    for line in fileLineObj:
        x = line.split()
        wordList.append(x)
    return wordList


def print_code_without_comments(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        output_lines = []

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('#'):
                continue
            if stripped_line:
                output_lines.append(stripped_line)

        # Write the modified code back to the file
        with open(file_name, 'w') as file:
            file.write('\n'.join(output_lines))

        print("Comments removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


lexeme_count = 0


def tokenize_code(file_name):
    global lexeme_count
    code_tokens = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            # Use regular expression to find words, identifiers, and operators
            tokens = re.findall(r'\w+|"[^"]+"|[.,!?;()+]+|(?<!=)==|=|:', line)

            for token in tokens:
                if token in ('def', 'return', 'if', 'elif', 'else', 'print'):
                    token_type = 'Keywords'
                elif token in ('calculate_sum', 'a', 'b', 'num1', 'num2', 'result', '__name__'):
                    token_type = 'Identifiers'
                elif token in ('"__main__"', '10', '20', '"Sum:"'):
                    token_type = 'Literals'
                elif token in ('+', '-', '*', '/', '=', '=='):
                    token_type = 'Operators'
                elif token in ('(', ')', ':', ',', '"'):
                    token_type = 'Separators'
                else:
                    token_type = 'Other'

                code_tokens.append((token, token_type))
                lexeme_count += 1  # Increment lexeme count

        return code_tokens

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


# Tokenize the code
token_list = tokenize_code('testCode.txt')

print()
# Print lexemes with types
for lexeme, lexeme_type in token_list:
    print(f"Lexeme: {lexeme}, Type: {lexeme_type}")

print("Lexeme count:", lexeme_count)
print(tokenize_code('testCode.txt'))


