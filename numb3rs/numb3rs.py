#---------- imports ----------------
import sys
import re

#---------- Functions ---------------
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Given a string, returns true or false after checking whether it is an IP address"""
    if re.search(r"^(([0-9]{1,2}|1[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]{1,3})$", ip):
        return True
    return False


#----------checking ----------------
if __name__ == "__main__":
    main()