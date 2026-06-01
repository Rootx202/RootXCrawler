import os
import re

from core.colors import run, que, good, green, end, info
from core.requester import requester


def updater():
    """Update the current installation.

    RootXCrawler does not auto-update from the original rootxcrawler repository.
    This is a local fork and update behavior is intentionally disabled.
    """
    print('%s Checking for updates' % run)
    print('%s Automatic updates are not available for RootXCrawler.' % info)
