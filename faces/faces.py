# writing a function to do the conversion
def convert(string_in):
    """
    This function take the input and convert :) to 🙂 and :( to 🙁
    Arguments:
    string_in: is the input string that needs to be converted

    Return:
    string_out: the result after the conversion
    """

    string_out = str(string_in).replace(":)","🙂").replace(":(","🙁")
    return string_out

def main():
    """Asks for input and call the convert function for conversion"""
    # lets take the input first
    string_in = input("What's your thought?\n")
    string_out = convert(string_in)

    # lets print the stuff out
    print(string_out)

# run the main function
main()