import sys

def main():
    """Main function to call functions and implement everything"""
    cArguments = sys.argv #
    file = check_command_arg(cArguments)
    print(count_lines(file))

def check_command_arg(cArguments):
    """Function to be called to check the command-line arguments"""
    if len(cArguments) < 2: #check the arguments
        sys.exit("Too few command-line arguments")
    elif len(cArguments) > 2:
        sys.exit("Too many command-line arguments")
    extension = cArguments[1][-3:]
    if extension != ".py":
        sys.exit("Not a python file")
    try:
        file = open(cArguments[1], 'r')
    except FileNotFoundError:
        sys.exit("File not found")
    file.close()
    return cArguments[1]

def count_lines(file):
    """Counts the number of lines excluding blank lines and comments in the given python file file"""
    counter = 0
    with open(file,'r') as doc:
        lines = doc.readlines()
    for line in lines:
        stripped = line.strip()
        if stripped != '':
            if stripped[0] != '#':
                counter += 1
    return counter



####
if __name__ == "__main__":
    main()
