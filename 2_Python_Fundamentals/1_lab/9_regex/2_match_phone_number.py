import re

phonebook = input()

pattern = r'(\+359)( |-)2(\2)\d{3}(\2)\d{4}\b'
valid_number = re.findall(pattern, phonebook)
print(valid_number)

# import re
#
# numbers = input()
#
# regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
# matches = re.findall(regex, numbers)
# print(matches)
# print(', '.join(matches))