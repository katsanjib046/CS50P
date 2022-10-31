def main():
    Input = input("Input: ")
    print(vowelRemover(Input))

def vowelRemover(Input):
    output = ""
    for c in Input:
        if c.lower() not in ['a','e','i','o','u']:
            output += c
    return output



#########
if __name__ == "__main__":
    main()