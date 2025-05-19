
import re

class EmailAddressParser:

    _split_re  = re.compile(r"[,\s]+")
    _email_re  = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def __init__(self, addresses):
        self._raw = addresses or ""

    def parse(self):
        seen = set()
        for token in self._split_re.split(self._raw):
            if self._email_re.match(token) and token not in seen:
                seen.add(token)
        return sorted(seen)
