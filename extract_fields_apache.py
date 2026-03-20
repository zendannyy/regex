import argparse 
import errno
import ipaddress
import logging
import re
import sys
from pathlib import Path


logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF
except ImportError:
    logger.error("PyMuPDF not installed. Install with: pip install PyMuPDF")
    sys.exit(1)

def iter_text_lines(logfile):
    """Yield text lines from .log/.txt files
    or extracted text from .pdf files."""
    if Path(logfile).suffix.lower() == ".pdf":
        text = extract_text_from_pdf(logfile)
        for line in text.splitlines():
            yield line
        return

    with open(logfile, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line


def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file"""
    try:
        doc = fitz.open(pdf_path)
        text_content = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            text_content.append(text)
        
        doc.close()
        return '\n'.join(text_content)
    
    except Exception as e:
        logger.error(f"Error reading PDF: {e}")
        sys.exit(1)

def domain_match(logfile):
    """parse and extract domains"""
    rex = r"\b\w+[.]\w{1,3}"
    logger.info(f'The following domains were found in the logfile \n')

    found = False
    try:
        for line in iter_text_lines(logfile):
            match = re.search(rex, line)
            if match:
                print(match.group())
                found = True
    except FileNotFoundError as fe:
        if fe.errno == errno.ENOENT:
            logger.error(f"File '{logfile}' does not exist")

    logger.info('\n')


def ip_match(logfile):
    """parse and extract IP's
    alt re pattern with named capture groups 
    (?P<IP_Octet>\\d{1,3})\\.(?P<IP_Octetll>\\d{1,3})\\.(?P<IP_Octetlll>\\d{1,3})\\.(?P<IP_OctetlV>\\d{1,3})
    """
    rex = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    logger.info(f'The following IP addresses were found in the logfile \n')
    
    found = False
    try:
        for line in iter_text_lines(logfile):
            match = re.search(rex, line)
            if match:
                print(match.group())
                found = True
    except FileNotFoundError as fe:
        if fe.errno == errno.ENOENT:
            logger.error(f"File '{logfile}' does not exist")

    logger.info('\n')


def extract_ips_with_lib(logfile):
    """parse and extract IP's
    the same as above function, but with ipaddress library"""
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
    """parse and extract status codes"""
    rex = r"\s[2-5]\d{2}"
    logger.info(f'The following Status Codes were found in the logfile \n')

    found = False
    try:
        for line in iter_text_lines(logfile):
            match = re.search(rex, line)
            if match:
                print(match.group())
                found = True
    except FileNotFoundError as fe:
         if fe.errno == errno.ENOENT:
            logger.info(f"File %s logfile does not exist")
    if not found:
        sys.exit("no Status Code found")


def main():
    parser = argparse.ArgumentParser(
        description='Read log file, parse & extract IP addresses and status codes.'
        """
        Examples: 
        python3 extract_fields.py server_logs.log
        python3 extract_fields.py server_logs.pdf
        """
        )
    parser.add_argument('logfile', type=str, help='The name of the log file to parse')
    args = parser.parse_args()
    ip_match(args.logfile)
    domain_match(args.logfile)
    status_match(args.logfile)


if __name__ == "__main__":
    main()
