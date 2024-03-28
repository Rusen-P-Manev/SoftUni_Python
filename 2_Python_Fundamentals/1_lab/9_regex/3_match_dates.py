# import re
#
# data_input = input()
#
# patter = r'(\d{2})([/.-])([A-Z][a-z]{2})(\2)(\d{4})'
# valid_dates = re.findall(patter, data_input)
#
# for curret_ele in valid_dates:
#     day = curret_ele[0]
#     month = curret_ele[2]
#     year = curret_ele[4]
#     print(f'"Day: {day}, Month: {month}, Year: {year}"')

import re

data_input = input()

patter = r'(\d{2})([/.-])([A-Z][a-z]{2})(\2)(\d{4})'
valid_dates = re.finditer(patter, data_input)

for curret_ele in valid_dates:
    day = curret_ele.group(1)
    month = curret_ele.group(3)
    year = curret_ele.group(5)
    print(f'"Day: {day}, Month: {month}, Year: {year}"')