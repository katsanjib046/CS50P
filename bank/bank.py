def main():
    x = money() #get the out of the following money function
    print(f"${x}")


def money():
    """Calculates how much money does one get"""
    greeting = input("Greeting: ").lower().strip(" ")
    if "hello" in greeting[:5]:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100

main()


