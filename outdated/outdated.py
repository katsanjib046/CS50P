def main():
    year, month, day = ask_date()
    print(f"{year}-{month:02}-{day:02}")


def ask_date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            in_date = input("Date: ")
            if "/" in in_date:
                month, day, year = in_date.split("/")
                month, day, year =  int(month), int(day), int(year)
                if 0< month <=12 and 0 < day <31 and 999 < year <9999:
                    return year, month, day
            elif " " and "," in in_date:
                in_date = in_date.replace(",","")
                month, day, year = in_date.split(" ")
                day, year = int(day), int(year)
                if month.capitalize() in months and 0 < day < 31 and 999 < year <9999:
                    month = months.index(month.capitalize()) + 1
                    return year, month, day
        except ValueError:
            pass





#####
if __name__ == "__main__":
    main()