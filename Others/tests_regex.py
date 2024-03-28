# import re
#
# dates = input()
#
# pattern = r'\d{1,2}\/[A-Z][a-z]{2}\/\d{4}|\d{1,2}\-[A-Z][a-z]{2}\-\d{4}|\d{1,2}\.[A-Z][a-z]{2}\.\d{4}'
# valid_dates = re.findall(pattern, dates)
# print(valid_dates)
# print(' '.join(valid_dates))
#
#
import re
dates = input()

pattern = r'(\d{2})([/.-])([A-Z][a-z]{2})(\2)(\d{4})'
valid_dates = re.findall(pattern, dates)
print(valid_dates)
for cd in valid_dates:  # налага се поже групите се отразяват като
                        # тюпъл в листа и принтираме за всеки тюпъл
    print(''.join(cd))