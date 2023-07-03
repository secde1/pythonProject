# decarator
# generator
# RegEx - Regular Expression

# import re
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string )
# print(result)

# candies = [4, 2, 1, 1, 2]
# extraCandies = 1
# for i, v in enumerate(candies):
#     if


import re

pattern = r'^[a-z0-9.]+@[a-z0-9]+\.[a-z]{2,3}$'
test_string = 'daniels21@gmal.com'

result = re.findall(pattern, test_string)

print(result)

