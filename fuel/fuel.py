def main():
    frac = get_frac("Fraction: ")
    fuel_gauge(frac)


def get_frac(prompt):
    while True:
        try:
            x,_,y = input(prompt).partition("/")
            frac = int(x) / int(y)
            if frac > 1:
                pass
            else:
                return frac
        except ValueError:
            print("It's Value error")
        except ZeroDivisionError:
            print("It's Zero division error")

def fuel_gauge(frac):
    percent = round(frac * 100)
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


######
if __name__ == "__main__":
    main()