import argparse 
import re
import sys

def matches(logfile):
    """id and extract IP's
    id and extract Status codes's, output on same line
    """
    ip_rex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    status_rex = "\s\d{3}\s"

    with open('logfile.txt', 'r') as f:
        for line in f:
            try:
                # if re.search(rex, line):
                ip_match = re.search(ip_rex, line)
                status_match = re.search(status_rex, line)
                if ip_match and status_match:
                    print(f"IP: {ip_match.group()}, Status Code: {status_match.group()}")
            except AttributeError:
                sys.exit("no IP or Status Code found")
                re.search()


def main():
    parser = argparse.ArgumentParser(description='Read log file, parse & extract IP addresses.')
    parser.add_argument('logfile', type=str, help='The name of the log file to parse')
    args = parser.parse_args()
    matches(args.logfile)


if __name__ == "__main__":
    main()
