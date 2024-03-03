import re

def readFile(fileName):
    """Read File """
    with open(fileName, 'r') as readFile:
        pyCodeTxt = readFile.read()
        return pyCodeTxt


def readFileLines(fileName):
    """Most of the functions I(Robbie) wrote are intended to work with the list of individual lines of code"""
    with open(fileName, 'r') as readFile:
        pyCodeLines = readFile.readlines()
        return pyCodeLines

def printCode(fileObj):
    """Print code from provided fileObj"""
    print(fileObj)

def printCodeLines(fileObj):
    """Print code in lines from provided fileObj"""
    for line in fileObj:
        print(line.strip())

def printCodeLineSeperated(fileLineObj):
    """Each read statement of code is seperated by line in terminal for readability works with parseCodeIntoWords()"""
    for word in fileLineObj:
        print(word)

def parseCodeIntoWords(fileLineObj):
    """Parses code lines into individual pieces, seperated by spaces."""
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

def tokenize_code(file_name):
    code_tokens = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line in lines:
            # Use regular expression to find words, identifiers, and operators
            tokens = re.findall(r'\b\w+\b|==|[^\s\w]', line)
            code_tokens.extend(tokens)

        return code_tokens

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Jeffrey's code begins
print("\n-----------Jeffrey's code begins-------------\n")

# Call the function to remove comments from the code and write the modified code back to the file
# Commented out because we don't need to see if the comments were removed successfully 
# print_code_without_comments('testCode.txt')

# Tokenize the code
print('\n\n\n')
print(tokenize_code('testCode.txt'))

# Jeffrey's code ends
print("\n-------------Jeffrey's code ends-----------------\n")
