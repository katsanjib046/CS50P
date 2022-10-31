def main():
    price = 50 #cost of the coke in cents
    print("Change owed:", coke(price))

def coke(price):
    while price > 0:
        print(f"Amount Due: {price}")
        coin = int(input("Insert Coin:"))
        if coin in [25, 10, 5]:
            price = price - coin

    return abs(price)

##########
if __name__ == "__main__":
    main()


