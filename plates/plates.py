def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 6 < length or length <2:
        return False
    if s.isalnum() == False:
        return False
    if s[0:2].isalpha() == False:
        return False
    checker = True #is true until you find first numeric character
    for i in range(2,length-1):
        if s[i].isnumeric() and s[i+1].isalpha():
            return False
        if checker and s[i].isnumeric():
            checker = False
            if s[i] == '0':
                return False
    return True




main()