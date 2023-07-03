#
import json

data = '{"name": "Jamshid","age": 19}'


# JSON matnini olish (stringify)
# json_str = json.dumps(data)
# print(json_str)
# Chiqish: {"name": "John", "age": 30}

# JSON matnini faylga yozish
with open("data.json", "w") as file:
    data1 = json.loads(data)
    json.dump(data1, file, indent=4)
# data.json faylida {"name": "John", "age": 30} yoziladi
# import json
# json_string = '{"name": "John", "age": 30}'
# with open('data.json', 'w') as file:
#     data = json.loads(json_string)
#     json.dump(data, file, indent=2)
# print(type(json_string))
#
# print(type(data))