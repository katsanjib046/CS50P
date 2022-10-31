import random
def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        counter = 0 # to count the number of mistakes
        while counter < 4:
            if counter == 3: # after 3 mistakes, we output the answer and break while loop
                print("%i + %i = %i" % (x[0],x[1],x[0]+x[1]))
                break
            try:
                ans = int(input("%i + %i = " % (x[0],x[1])))
                counter += 1 #counting the number of tries
                if ans != x[0] + x[1]:
                    print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                counter += 1
                pass
    print(score)




def get_level():
    """Ask for a level from th user"""
    while True:
        try:
            level = int(input())
            if level in [1,2,3]:
                return level
        except ValueError:
            pass




def generate_integer(level):
    """Generate integer bases on the level input by the user"""
    if level == 1:
        x = [random.randint(0,9) for i in range(2)]
    elif level ==2:
        x = [random.randint(10,99) for i in range(2)]
    else:
        x = [random.randint(100,999) for i in range(2)]
    return x




if __name__ == "__main__":
    main()