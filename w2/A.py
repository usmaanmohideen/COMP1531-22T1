'''
“pythonic describes a coding style that leverages Python's
unique features to write code that is readable and beautiful"

printing example with print statements!

How can we be more pythonic about the example below?
'''

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for idx in range(len(x)):
  if x[idx] % 2 == 0:
    result.append(x[idx] * 2)
  else:
    result.append(x[idx])

print(result)

'''
What does it do?


What style could be improved here?


How can we change the code to be what we would describe as "pythonic"?
'''

'''
Ternary Operator:
    https://careerkarma.com/blog/python-ternary-operator/

List Comprehension:
    https://www.w3schools.com/python/python_lists_comprehension.asp
'''
