"""Support for dnsdumpster.com."""
import re
import sys

import requests


def dnsdumpster(domain, output_dir):
    """Query dnsdumpster.com."""
    session = requests.Session()
    try:
        response = session.get('https://dnsdumpster.com/', timeout=30)
        csrf_match = re.search(
            r'name=\"csrfmiddlewaretoken\" value=\"(.*?)\"', response.text)
        if not csrf_match:
            print("[-] Could not extract CSRF token from dnsdumpster.com", file=sys.stderr)
            return
        csrf_token = csrf_match.group(1)

        cookies = {'csrftoken': csrf_token}
        headers = {'Referer': 'https://dnsdumpster.com/'}
        data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
        session.post(
            'https://dnsdumpster.com/', cookies=cookies, data=data, headers=headers, timeout=30)

        image = session.get('https://dnsdumpster.com/static/map/%s.png' % domain, timeout=30)
        if image.status_code == 200:
            with open('%s/%s.png' % (output_dir, domain), 'wb') as f:
                f.write(image.content)
    except Exception as e:
        print("[-] Failed to query dnsdumpster.com: %s" % e, file=sys.stderr)
