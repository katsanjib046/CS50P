#----------- Some imports-----------
import re


#----------- Functions--------------
def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe .*src=\"https?://(?:www\.)?youtube\.com/embed/([^\"^ ]+)\".*></iframe>$', s, re.DOTALL):
        return f"https://youtu.be/{matches.group(1)}"




#------------ Testing--------------
if __name__ == "__main__":
    main()
