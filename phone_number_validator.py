import csv
import re
from re import findall

def phone_match():
    """take phone numebrs as input 
    print valid phone numbers as output"""
    with open('phone_numbers.csv') as file:
        reader = csv.reader(file, delimiter=' ')
        line_count = 0 
        # rex = '\d\d\d-\d\d\d-\d\d\d\d'
        rex = '\d[-]|((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}'
        for row in reader:
            data = file.read()
            match = findall(rex, data)

    print(match)
        # print(row)
        # if line_count == 0:
        #     print(f'This is the data {','.join(row)}')


if __name__ == '__main__':
    phone_match()
