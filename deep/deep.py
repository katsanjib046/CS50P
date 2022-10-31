def main():
    if deep_answer():
        print("Yes")
    else:
        print("No")


# defining the funciton for deep_answer
def deep_answer():
    answer = input("What's the answer to all the deep questions?").lower().strip(" ")
    if answer in ["42", "forty-two", "forty two"]:
        return True
    else:
        return False

main()