def main():
    lst = grocery()
    for items in sorted(set(lst)):
        print(f"{lst.count(items)} {items}")

def maind():
    lst = grocery_d()
    for keys in sorted(lst.keys()):
        print(f"{lst[keys]} {keys}")


def grocery():
    lst = []
    while True:
        try:
            lst.append(input().upper())
        except EOFError:
            print()
            lst.sort()
            return lst

def grocery_d():
    lst = {}
    while True:
        try:
            item = (input().upper())
            if item in lst:
                lst[item] += 1
            else:
                lst[item] = 1
        except EOFError:
            print()
            return lst

###
if __name__ == "__main__":
    maind()