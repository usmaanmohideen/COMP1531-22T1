def wondrous(start):
    '''
    Returns the wondrous sequence for a given number.
    '''

    # 1
    if start == 1:
        return [start]

    current = start
    sequence = []

    while current != 1:
        sequence.append(current)
        if (current % 2 == 0):
            # 2
            current //= 2
        else:
            current = (current * 3) + 1

    # 3
    sequence.append(current)
    return sequence

'''
1. Missing the case of when start = 1

2. / will take actual answer,
    // will take the lower absolute always

3. We need to append the 1 at the end!
'''