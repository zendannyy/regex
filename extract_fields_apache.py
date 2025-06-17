import argparse 
import errno
import ipaddress
import re
import sys

def ip_match(logfile):
    """id and extract IP's
    alt re pattern with named capture groups 
    (?P<IP_Octet>\d{1,3})\.(?P<IP_Octetll>\d{1,3})\.(?P<IP_Octetlll>\d{1,3})\.(?P<IP_OctetlV>\d{1,3})
    """
    rex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    print(f'The following IP addresses and Status Codes were found in the logfile \n')
    
    try:
        with open(logfile, 'r') as f:
            for line in f:
                # if re.search(rex, line):
                    print(re.search(rex, line).group())
    except FileNotFoundError as fe:
        if fe.errno == errno.ENOENT:
            print(f"File '{logfile}' does not exist")
    except AttributeError:
        sys.exit("no IP found")
    print('\n')

def extract_ips_with_lib(logfile):
    ip_addresses = []
    with open(logfile, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                try:
                    ip = ipaddress.ip_address(word)
                    ip_addresses.append(str(ip))
                except ValueError:
                    continue
    return ip_addresses

def status_match(logfile):
    """id and extract status codes"""
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
