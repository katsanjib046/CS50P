#---------- Some Imports -------------
from validator_collection import validators


#---------- Functions ---------------
def main():
    print(response(input("Email: ")))

def response(s):
    try:
        if validators.email(s):
            return "Valid"
    except ValueError:
        return "Invalid"

#---------- Testing -------------
main()
