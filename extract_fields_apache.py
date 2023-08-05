import argparse 
import errno
import re
import sys

def ip_match(logfile):
    """id and extract IP's"""
    rex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    print(f'The following IP addresses and Status Codes were found in the logfile \n')
    
    try:
        with open(logfile, 'r') as f:
            for line in f:
                if re.search(rex, line):
                    print(re.search(rex, line).group())
    except FileNotFoundError as fe:
        if fe.errno == errno.ENOENT:
            print(f"File '{logfile}' does not exist")
    except AttributeError:
        sys.exit("no IP found")
    print('\n')


def status_match(logfile):
    "id and extract status codes"
    rex = "\s[2-5]\d{2}"
    try:
        with open(logfile, 'r') as f:
            for line in f:
                # if re.search(rex, line):
                print(re.search(rex, line).group())
    except FileNotFoundError as fe:
         if fe.errno == errno.ENOENT:
            print(f"File '{logfile}' does not exist")
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
