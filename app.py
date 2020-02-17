# for loop

'''
for i in range(1, 10):
    print(i)
'''

'''
phone = ['xiaomi', 'iphone6', 'sumsang']

for phone in phone:
    print(phone)
'''

phone = [
    {"id": 1, "name": "xiaomi"},
    {"id": 2, "name": "iphone6"},
    {"id": 3, "name": "summsang"},
]

for phone in phone:
   print(phone['name'])