import re

line = input()
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))'
text = re.finditer(regex, line)
matches = []

for i in text:
    matches.append(i.group())

print(' '.join(matches))