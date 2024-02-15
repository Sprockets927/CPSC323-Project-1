#Robbie Robertson
#2/12/2024
#Lexical Aanalysis Project

def readFile(fileName):
    """Read File """
    with open(fileName,'r') as readFile:
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


#Reads the entirety of the code given by the prof into a string(read()) & prints
testFile0 = readFile('testCode.txt')
print(testFile0)
print("\n")

#Reads the code into a list entry for each line(readlines()) & prints
testFile = readFileLines('testCode.txt')
print(testFile)
print("\n")

#Turns fileLineObj testFile into a list of pieces seperated by spaces prints pieces line by line
wordList = parseCodeIntoWords(testFile)
printCodeLineSeperated(wordList)
