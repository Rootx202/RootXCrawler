"""Support for archive.org."""
import datetime
import json
import sys

from requests import get, ConnectionError, Timeout


def time_machine(host, mode):
    """Query archive.org."""
    now = datetime.datetime.now()
    to = now.strftime("%Y%m%d")
    from_date = now - datetime.timedelta(days=180)
    fro = from_date.strftime("%Y%m%d")
    url = "https://web.archive.org/cdx/search?url=%s&matchType=%s&collapse=urlkey&fl=original&filter=mimetype:text/html&filter=statuscode:200&output=json&from=%s&to=%s" % (host, mode, fro, to)
    try:
        response = get(url, timeout=30).text
    except (ConnectionError, Timeout) as e:
        print("[-] Failed to fetch from archive.org: %s" % e, file=sys.stderr)
        return []
    try:
        parsed = json.loads(response)[1:]
    except (json.JSONDecodeError, IndexError):
        return []
    return [item[0] for item in parsed]
