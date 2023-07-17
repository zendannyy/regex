import re
import email.utils as eu
import sys 

def email_match(email):
    """check if input is a valid email
    print name and email"""
    rex = r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}'
    # name, email = eu.parseaddr(input())
    if re.match(rex, email):
        print(eu.parseaddr((email)))
    else:
        sys.exit("That is an invalid email address")


if __name__ == '__main__':
    if len(sys.argv) <2:
        sys.exit("Usage: python3 email_validator.py name email")
    email = sys.argv[1]
    # email = sys.argv[2]
    email_match(email)
