import argparse 
import csv
import re
import sys 
from re import findall

def email_match(email):
    """check if input is a valid email
    print name and email"""
    rex = r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}'
    # name, email = eu.parseaddr(input())
    if re.match(rex, email):
        print(f"{email}, is a valid email address")
    else:
        sys.exit(f"{email} is an invalid email address")


def emails_match(csv_file):
    """takes a csv as an argument
    parses the file and extracts valid email addresses
    """
    rex = r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}'
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            data = ' '.join(row)
            # data = file.read()
            matches = findall(rex, data)
            for match in matches:
                print(f"{email_match} is a valid email address")

def main():
    parser = argparse.ArgumentParser(description="""CLI tool for validating emails. With the choice of individual emails, or a csv file.""")
    parser.add_argument('-i', '--ind', help='Performs validation for the individual email given')
    parser.add_argument('-f', '--file', help='Performs email valditation and extraction for the csv given')

    args = parser.parse_args()
    
    if len(sys.argv) <2:
        sys.exit("Usage: python3 email_validator.py name email\n\n"
        "run python3 email_validator.py -h for full help message")
    # email = sys.argv[1]
    # email = sys.argv[2]


    if args.ind:
        email_match(args.ind)
        
    if args.file:
        emails_match(args.file)


# if __name__ == '__main__':
    # if len(sys.argv) <2:
    #     sys.exit("Usage: python3 email_validator.py name email")
    # email = sys.argv[1]
    # # email = sys.argv[2]
    # email_match(email)


if __name__ == '__main__':
	main()
