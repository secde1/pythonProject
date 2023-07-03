# public = self.c
# protect = self._c
# private =  self.__c
# dandermetod = __name__


#                           dekarator
# # Декоратор в Python — это функция, которая принимает другую функцию в
# # качестве аргумента и возвращает еще одну функцию . Декораторы могут быть
# # чрезвычайно полезными, поскольку они позволяют расширять существующую функцию
# # без какой-либо модификации исходного исходного кода функции.

# def logger_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} called with arguments {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} finished with result: {result}")
#         return result
#     return wrapper
# @logger_decorator
# def add_numbers(a, b, v ):
#     return a + b + v
# result = add_numbers(3, 5, 3)
# print(result)



#                           generate
# В Питоне генератор — это функция, возвращающая итератор, который создает
# последовательность значений при повторении . Генераторы полезны, когда
# мы хотим создать большую последовательность значений, но не хотим хранить их все в памяти сразу.
# def number_generator(n):
#     for i in range(n):
#         yield i
#
# # Использование генератора
# generator = number_generator(5)
#
# for num in generator:
#     print(num)

# #                           interator
# # Что такое итератор в Python? В Python итератор — это объект, который позволяет
# # перебирать наборы данных, такие как списки, кортежи, словари и наборы .
# # Итераторы Python реализуют шаблон проектирования итератора, который позволяет
# # вам перемещаться по контейнеру и получать доступ к его элементам.
#
#
# #                             yield
# #                   yield - interator qaytaradi
# # Мы должны использовать yield, когда хотим перебрать последовательность,
# # но не хотим хранить всю последовательность в памяти. Yield используются в генераторах
# # Python. Генераторная функция определяется как обычная функция, но всякий раз, когда ей
# # нужно сгенерировать значение, она делает это с помощью ключевого слова yield, а не return.
#
# # fibonaci yield iwlatilgan xolda
# '''
# def fibo(n):
#     a, b, k = 1, 1, 1
#     while k <= n:
#         yield a
#         a, b = b, a + b
#         k += 1
#
# print(tuple(i for i in fibo(10)))
# '''
# import json
#
# # tub sonlani chqazuvchi dastur yield
# '''
# def tub_sonlarni_topish(n):
#     for num in range(2, n + 1):
#         is_tub = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_tub = False
#                 break
#         if is_tub:
#             yield num
#return
# tub_sonlar = tub_sonlarni_topish(10)
# for tub_son in tub_sonlar:
#     print(tub_son)
# ''T

# import json
# json_string = '{"name": "John", "age": 30}'
# with open('data.json', 'w') as file:
#     data = json.loads(json_string)
#     json.dump(data, file, indent=2)
#
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print(data)

import json


#
# import json
#
# json_string = '{"name": "John", "age": 30, "city": "New York"}'
# data = json.loads(json_string)
# print(data)
#
#
#
