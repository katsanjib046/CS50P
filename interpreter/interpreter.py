def main():
    user_input = input("Expression: ")
    print(interpreter(user_input))

def interpreter(user_input):
    left,mid,right = user_input.rsplit()
    if mid == '+':
        return float(int(left) + int(right))
    elif mid == '-':
        return float(int(left) - int(right))
    elif mid == '*':
        return float(int(left) * int(right))
    elif mid == '/':
        return float(int(left) / int(right))
    else:
        return "Error"

main()