# text = input().split()
# new_text = [txt * len(txt) for txt in text]
# print(''.join(new_text))

# text = input().split()
# new_text = ''
#
# for txt in text:
#     new_text += txt * len(txt)
#
# print(new_text)


text = input().split()
new_text_list = []

for txt in text:
    new_text = txt * len(txt)
    new_text_list.append(new_text)

print(''.join(new_text_list))
