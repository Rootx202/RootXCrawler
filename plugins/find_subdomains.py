"""Support for findsubdomains.com."""
import sys
from re import findall

from requests import get, ConnectionError, Timeout


def find_subdomains(domain):
    """Find subdomains according to the TLD."""
    result = set()
    try:
        response = get('https://findsubdomains.com/subdomains-of/' + domain, timeout=30)
        matches = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response.text)
        for match in matches:
            result.add(match.replace(' ', '').replace('\n', ''))
    except (ConnectionError, Timeout) as e:
        print("[-] Failed to fetch subdomains from findsubdomains.com: %s" % e, file=sys.stderr)
    return list(result)
