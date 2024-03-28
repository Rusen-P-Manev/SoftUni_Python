import re
times_to_repeat = int(input())

# ^([A-Z]{1}[a-z]{3,} [A-Z][a-z]+)\#+([A-Z][a-z]+\&*([A-Z][a-z]+)*\&*([A-Z][a-z]+)*)\d{2}(([A-Z][a-z]+\d*)+) (Ltd.|JSC)
pattern = r'(?P<name>^([A-Z]{1}[a-z]{3,} [A-Z][a-z]+))\#+(?P<position>[A-Z][a-z]+\&*([A-Z][a-z]+)*\&*([A-Z][a-z]+)*)\d{2}(?P<company>(([A-Z][a-z]+\d*)+) (Ltd.|JSC))'

for _ in range(times_to_repeat):
    data = input()
    valid_data = re.findall(pattern, data)
    data = [ele for ele in valid_data[0]]
    if valid_data:
        name = data[0]
        print(name)
        company = data[2]
        print(company)
