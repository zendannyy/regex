import argparse
import random
from datetime import datetime, timedelta


def log_file(logfile):
    # List of sample IP addresses
    ips = ["192.0.2." + str(i) for i in range(1, 101)]
    # List of sample request lines
    requests = ['"GET /index.html HTTP/1.1"', '"POST /form.php HTTP/1.1"', '"GET /products.html HTTP/1.1"']
    # List of sample status codes
    status_codes = [200, 302, 304, 404, 500]

    # Start time
    time = datetime.now()
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    log_lines = []

    for i in range(100):
        ip = random.choice(ips)
        request = random.choice(requests)
        status_code = random.choice(status_codes)
        size = random.randint(2000, 5000)
        
        # Print log entry
        # print(f"{time.isoformat()} {ip} - - {request} {status_code} {size}")
        log_lines.append(f"{time.strftime(TIME_FORMAT)} {ip} - - {request} {status_code} {size}")
        
        # Increment time by 1 minute
        time += timedelta(minutes=1)

     # with open('log.txt', 'w') as f:
    with open(logfile, 'w') as f:
        for line in log_lines:
            f.write(line + '\n')

    return log_lines


def main():
    parser = argparse.ArgumentParser(description='Generate a log file.')
    parser.add_argument('logfile', type=str, help='The name of the log file to create')
    args = parser.parse_args()
    log_file(args.logfile)


if __name__ == "__main__":
    main()

