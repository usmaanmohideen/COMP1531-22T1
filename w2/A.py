'''
“pythonic describes a coding style that leverages Python's
unique features to write code that is readable and beautiful"

printing example with print statements!

How can we be more pythonic about the example below?
'''

random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []

for value in random_list:
#     if value % 2 == 0:
#         result.append(value * 2)
#     else:
#         result.append(value)

print([(value * 2 if value % 2 == 0 else value) for value in random_list])

'''
What does it do?


What style could be improved here?


How can we change the code to be what we would describe as "pythonic"?
'''

'''
Ternary Operator:
    https://careerkarma.com/blog/python-ternary-operator/

    [execute if true] if [condition] else [execute if false]

    if value % 2 == 0:
        result.append(value * 2)
    else:
        result.append(value)

    result.append(value * 2) if value % 2 == 0 else result.append(value)


List Comprehension:
    https://www.w3schools.com/python/python_lists_comprehension.asp

    random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [value * 2 if value % 2 == 0 else value) for value in random_list]


'''


