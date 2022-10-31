def main():
    # Ask user for the input name
    camelCase = input("camelCase: ")
    snakeCase = snake_case(camelCase)
    print("snake_case: ",snakeCase)

def snake_case(camelCase):
    snakeCase =""
    for letter in camelCase:
        if letter.islower() == False:
            snakeCase += '_'
        snakeCase += letter.lower()
    return snakeCase


####
if __name__ == "__main__":
    main()
