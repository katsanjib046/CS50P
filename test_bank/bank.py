def main():
    greeting = input("Greeting: ")
    x = value(greeting) #get the out of the following money function
    print(f"${x}")


def value(greeting):
    """Calculates how much money does one get"""
    greeting = greeting.lower().strip(" ")
    if "hello" in greeting[:5]:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100

######
if __name__ == "__main__":
    main()


