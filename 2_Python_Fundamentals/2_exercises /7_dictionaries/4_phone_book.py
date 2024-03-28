# phonebook = {}
# while True:
#     entry = input()
#     if "-" not in entry:
#         break
#     name, phone_number = entry.split("-")
#     phonebook[name] = phone_number
# searches = int(entry)
# for search in range(searches):
#     searched_name = input()
#     if searched_name in phonebook.keys():
#         print(f"{searched_name} -> {phonebook[searched_name]}")
#     else:
#         print(f"Contact {searched_name} does not exist.")



details_container = {}
n = 0
while True:
    person_details = input()
    if "-" not in person_details:
        n = int(person_details)
        break
    person_details = person_details.split('-')
    details_container[person_details[0]] = person_details[1]

for _ in range(n):
    searched_name = input()

    if searched_name in details_container:
        print(f"{searched_name} -> {details_container[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
