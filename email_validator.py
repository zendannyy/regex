# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils as eu
import sys 

# check if input is a valid email
#  print name and email
rex = '<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
for i in range(int(input())):
    name, email = eu.parseaddr(input())
    if rex.match(email):
        print(eu.formataddr(name, email))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 email_validator.py name email")
    name = ''.join(sys.argv[1:])
    email = ''.join(sys.argv[2:])
    print(name, email)
