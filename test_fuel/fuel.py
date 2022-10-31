def main():
    percentage = None
    while percentage == None:
        prompt = input("Fraction: ")
        percentage = convert(prompt)
    print(gauge(percentage))




def convert(prompt):
    try:
        x,_,y = prompt.partition("/")
        frac = int(x) / int(y)
        if frac > 1:
            pass
        else:
            return round(frac * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


######
if __name__ == "__main__":
    main()