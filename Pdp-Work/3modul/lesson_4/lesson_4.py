


# import json
#
# def decorator(func): # 4
#     def wrapper(user: dict): # 5
#         if user['role'] == "ADMIN":
#             return func(user) # 7
#         # 7
#
#     return wrapper
#
#
# @decorator
# def print_user(user: dict): # 8
#     return user['username'], user['role']
#
#
# with open("users.json" , 'r') as f: # 1
#     for user in json.load(f): # 2
#         response = print_user(user) # 3
#         if response:
#             print(response)
#
# import os
# os.rename('user.json', 'users.json')

# def my_decorator(n1): # 3
#     def inner(func): # 4
#         def wrapper(n2): # 5
#             return func(n2)  * n1
#         return wrapper
#     return inner
#
# @my_decorator(3) # 2
# def multiple_num(num): # 7
#     return num # 8
#
# print(multiple_num(10)) # 1

# def my_decorator(n1, n2):
#     def decorator(func):
#         def wrapper(*args):
#             result = func(*args)
#             return result[n1:n2]
#         return wrapper
#     return decorator
#
# @my_decorator(2, 10)
# def slicing_txt(satr):
#     return satr
#
# print(slicing_txt('hello world'))
# def make_out_word(out, word):
#     return out[:2] + word + out[2:]

# Example usage
# out_string = "<<>>"
# word_string = "word"
# new_string = make_out_word(out_string, word_string)
# print(new_string)

