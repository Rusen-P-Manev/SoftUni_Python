import re
names_to_check = input()

pattern = r"\b[A-Z][a-z]* [A-Z][a-z]+\b"
matches = re.findall(pattern, names_to_check)

print(' '.join(matches))