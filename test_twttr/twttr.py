def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    output = ""
    for c in word:
        if c.lower() not in ['a','e','i','o','u']: #correct version
        #if c not in ['a','e','i','o','u']: # incorrect version
            output += c
    return output



#########
if __name__ == "__main__":
    main()