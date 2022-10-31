from datetime import date
import sys
import inflect
p = inflect.engine()


def main():
    bday = get_bday()
    print(calculate_minute(bday))

def get_bday():
    try:
        bday = input("Date of birth: ")
        bday_date = date.fromisoformat(bday)
        return bday_date
    except ValueError:
        sys.exit("Invalid date")

def calculate_minute(bday):
    today = date.today()
    minutes = (today - bday).days * 24 * 60
    return p.number_to_words(int(minutes), andword = '').capitalize() + ' minutes'



# -------- testing--------
if __name__ == "__main__":
    main()