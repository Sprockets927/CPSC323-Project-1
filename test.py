# This file was used to test the functions seperate from lexAnalysis.py 

import re 

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

# Remove comments from the code and write the modified code back to the file
print_code_without_comments('testCode.txt')

# Tokenize the code
print('\n\n\n')
print(tokenize_code('testCode.txt'))

# |(?<!=)==|=
# tokens = re.findall(r"[\w']+|[.,!?;()]+|(?<!=)==|=", line)
# tokens = re.findall(r"[\w']+|[.,!?;()+]+|(?<!=)==|=|:", line)