import re
import sys

def validate_phone_number(phone_number):
    pattern = re.compile(r'^\d[-]|((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$')
    if pattern.match(phone_number):
        print(f'{phone_number} is a valid phone number.')
    else:
        print(f'{phone_number} is not a valid phone number.')

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: Please enter a phone number: ')
    # try:
    #     arg = sys.argv[1]
    # except IndexError:
    #     print("expected 1 argument (a phone number), got 0")
    #     raise (SystemExit)

    phone_number = ''.join(sys.argv[1:])
    validate_phone_number(phone_number)


if __name__ == '__main__':
    main()
