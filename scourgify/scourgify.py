import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:] != '.csv' and sys.argv[2][-4:] != '.csv':
        sys.exit("Not a csv file")
    try:
        infile = open(sys.argv[1],'r')
        outName = sys.argv[2]
        scourgify(infile, outName)
        infile.close()
    except FileNotFoundError:
        sys.exit("File Not Found!")

def scourgify(infile, outname):
    before = csv.reader(infile)
    next(before)                            # skipping the header
    outfile = open(outname, 'w')
    after = csv.writer(outfile)
    after.writerow(['first', 'last', 'house'])
    for row in before:
        last, first = row[0].split(',')
        house = row[1]
        after.writerow([first.strip(), last.strip(), house])
    outfile.close()


########## Testing #########
if __name__ == "__main__":
    main()