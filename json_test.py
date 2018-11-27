import json

# numbers_list = [1, 23, 5, 6, 7, 8, 4, 10]
# file_path = "numbers.json"
# with open(file_path, 'w') as file_obj:
#     json.dump(numbers_list, file_obj)

# numbers_list = []
# file_path = "numbers.json"
# with open(file_path) as file_obj:
#     numbers_list = json.load(file_obj)
# print(numbers_list)

# user_name = input("Pleas input your name: ")
# file_path = "json_test.json"
# with open(file_path, 'w') as file_obj:
#     json.dump(user_name, file_obj)

with open(file_path) as file_obj:
    user_name = json.load(file_obj)

print(user_name)
