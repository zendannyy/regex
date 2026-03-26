import argparse 
import errno
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
    """Yield text lines from .log/.txt files or extracted text from .pdf files."""
    if Path(logfile).suffix.lower() == ".pdf":
        for line in extract_text_from_pdf(logfile).splitlines():
            yield line
        return
    with open(logfile, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line


def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file"""
    try:
        with fitz.open(pdf_path) as doc:
            return "\n".join(page.get_text() for page in doc)
    except Exception as exc:
        logger.error(f"Error reading PDF: {exc}")
        sys.exit(1)


def domain_match(logfile):
    """parse and extract domains
    Supports fanged and defanged domains, e.g. api.example.com / api.example[.]com"""
    rex = r"\b(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.|\[\.\]))+(?:[A-Za-z]{2,63})\b"
    try:
        for line in iter_text_lines(logfile):
            match = re.search(rex, line)
            if match:
                print(match.group())
    except FileNotFoundError:
        logger.error(f"File '{logfile}' does not exist")
    logger.info("\n")


def ip_match(logfile):
    """parse and extract IP's
    alt re pattern with named capture groups 
    (?P<IP_Octet>\\d{1,3})\\.(?P<IP_Octetll>\\d{1,3})\\.(?P<IP_Octetlll>\\d{1,3})\\.(?P<IP_OctetlV>\\d{1,3})"""
    rex = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    logger.info(f'The following IP addresses were found in the logfile \n')
    
    found = False
    try:
        for line in iter_text_lines(logfile):
            match = re.search(rex, line)
            if match:
                print(match.group())
    except FileNotFoundError:
        logger.error(f"File '{logfile}' does not exist")
    logger.info("\n")


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
    except FileNotFoundError:
        logger.error(f"File '{logfile}' does not exist")
    if not found:
        logger.warning("no Status Code found")


def url_match(logfile):
    """parse and extract full URLs"""
    # Support fanged and defanged URLs, e.g. https://api.example.com,  https://api.example[.]com
    rex = r"\bhttps?(:|\[:])//[^\s\"'<>]+\b"
    logger.info(f'The following URLs were found in the logfile \n')

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

def fanged_ioc_match(logfile):
    """Parse and extract fanged IOCs: IPs, domains, URLs, and hashes."""
    patterns = {
        "ipv4": re.compile(
            r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
            r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
        ),
        "domain": re.compile(
            r"\b(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.|\[\.\]))+(?:[A-Za-z]{2,63})\b"
        ),
        # Match full URL for both fanged and common defanged forms:
        # https://example.com/path and hxxps://api.example[.]com/path
        "url": re.compile(r"\b(?:https?|hxxps?)://[^\s\"'<>]+"),
        "sha256": re.compile(r"\b[a-fA-F0-9]{64}\b"),
    }
    iocs = {key: set() for key in patterns}

    try:
        for line in iter_text_lines(logfile):
            for ioc_type, pattern in patterns.items():
                for match in pattern.findall(line):
                    iocs[ioc_type].add(match)
    except FileNotFoundError:
        logger.error(f"File '{logfile}' does not exist")
        return

    logger.info("The following fanged IOCs were found in the logfile\n")
    found_any = False
    for ioc_type in ("url", "domain", "ipv4", "sha256"):
        if not iocs[ioc_type]:
            continue
        found_any = True
        print(f"[{ioc_type}]")
        for value in sorted(iocs[ioc_type]):
            print(value)
        print()
    if not found_any:
        logger.warning("no fanged IOCs found")


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
    parser.add_argument('-i', '--ip', action='store_true', help='Specifying for IP addresses only')
    parser.add_argument('-d', '--domain', action='store_true', help='Specifying for domains addresses only')
    parser.add_argument('-u', '--url', action='store_true', help='Specifying for URLs only')
    parser.add_argument('-s', '--status', action='store_true', help='Specifying for Status codes only')
    
    args = parser.parse_args()

    if any((args.ip, args.domain, args.url, args.status)):
        if args.ip:
            ip_match(args.logfile)
            
        if args.domain:
            domain_match(args.logfile)
    
        if args.url:
            url_match(args.logfile)

        if args.status:
            status_match(args.logfile)
    else:
        fanged_ioc_match(args.logfile)
        status_match(args.logfile)


if __name__ == "__main__":
    main()
