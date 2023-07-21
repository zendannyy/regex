import argparse 
import re
import sys

def ip_match(logfile):
    """id and extract IP's"""
    rex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    with open('logfile.txt', 'r') as f:
        for line in f:
            try:
                # if re.search(rex, line):
                print(re.search(rex, line).group())
            except AttributeError:
                sys.exit("no IP found")


def status_match(logfile):
    "id and extract status codes"
    rex = "\s\d{3}"
    with open('logfile.txt', 'r') as f:
        for line in f:
            try:
                # if re.search(rex, line):
                print(re.search(rex, line).group())
            except AttributeError:
                sys.exit("no Status Code found")

def main():
    parser = argparse.ArgumentParser(description='Read log file, parse & extract IP addresses.')
    parser.add_argument('logfile', type=str, help='The name of the log file to parse')
    args = parser.parse_args()
    ip_match(args.logfile)
    status_match(args.logfile)


if __name__ == "__main__":
    main()
