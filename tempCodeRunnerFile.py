def tokenize_code(file_name):
    code_tokens = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            # Use regular expression to find words, identifiers, and operators
            tokens = re.findall(r"[\w']+|[.,!?;()=+:]|==|:", line)
            code_tokens.extend(tokens)

        return code_tokens

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")