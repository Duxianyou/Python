# def get_file_count(file_name):
#     """计算一个文件大致包含多少个单词"""
#     try:
#         with open(file_name) as file_object:
#             contents = file_object.read()
#             print(contents.lower().count("the"))
#     except FileNotFoundError:
#         #pass
#         print("This file not exit!")
#         return 0
#     else:
#         msg = contents.split()
#         return len(msg)


# file_path = 'alice.txt'
#
# file_len = get_file_count(file_path)
#
# if file_len:
#     print(str(file_len))
