import sys
import csv
import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:] != '.csv':
        sys.exit("Not a csv file")
    try:
        csvfile = open(sys.argv[1],'r')
        print(pizza_art(csvfile))
        csvfile.close()
    except FileNotFoundError:
        sys.exit("File Not Found!")

def pizza_art(csvfile):
    """Given a menu as a csv file, returns an ascii art"""
    file = csv.DictReader(csvfile)
    return tabulate.tabulate(file, headers = "keys", tablefmt = 'grid')





############ Testing ###########
if __name__ == "__main__":
    main()