import argparse
import csv
import re
import sys
from re import findall

def phone_match(csv_file):
    """Take a csv with phone numbers as input 
    parses the file and extracts valid phone numbers

    Return valid phone numbers as output
    """
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            # line_count = 0 
            rex = r'(?:\+1)?\d{3}-\d{3}-\d{4}|\d{3}\s*-\d{3}-\d{4}'
            for row in reader:
                data = ' '.join(row)
                matches = findall(rex, data)
                for match in matches:
                    print(f"{match} is a valid phone number")
    except FileNotFoundError:
        print(f"Error: File {csv_file} does not exist")


def main():
    parser = argparse.ArgumentParser(description="""CLI tool for validating phone numbers. With the choice of individual emails, or a csv file.""")
    parser.add_argument('-i', '--ind', help='Performs validation for the individual phone number given')
    parser.add_argument('-f', '--file', help='Performs phone number validation and extraction for the csv given')

    args = parser.parse_args()

    if len(sys.argv) <2:
        sys.exit("Usage: python3 phone_number_validator.py file\n\n"
        "run python3 phone_number_validator.py -h for full help message")
        
    if args.ind:
        phone_match(args.ind)

    if args.file:
        phone_match(args.file)


if __name__ == '__main__':
    main()
