import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    num = random.randint(1,n)
    boo = True
    while boo:
        try:
            guess = int(input("Guess: "))
            if guess <=0:
                pass
            else:
                if guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too large!")
                else:
                    print("Just right!")
                    boo = False
        except ValueError:
            pass




if __name__ == "__main__":
    main()