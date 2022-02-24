randomNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for number in randomNumbers:
    if number % 2 == 0:
        result.append(number * 2)
    else:
        result.append(number)

print(result)

'''
What does it do?
    Multiply even numbers by 2 and leave odd numbers as is

What style could be improved here?
    - Spacing not consistent
    - Indentation not 4 spaces (refer to style guide on webcms3)
    - Could use for-range loop in this case
    - range(len(x)) is redundant, could just use range normally

How can we change the code to be what we would describe as "pythonic"?
   Fix the above.
'''

'''
[(element * 2 if element % 2 == 0 else element) for element in x]
'''