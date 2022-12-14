def main():
    menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }
    total = taqueria(menu)

def taqueria(menu):
    total = 0
    while True:
        try:
            food = input("Item: ").lower()
            if food in menu:
                total += menu[food]
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break





######
if __name__ == "__main__":
    main()