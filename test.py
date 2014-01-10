import re


s = 'salut [[toto, comment ca va?]]'
re.sub("(\[\[.*\]\])", lambda m: "[%s](%s)"% (m.group(1), m.group(1)), s)