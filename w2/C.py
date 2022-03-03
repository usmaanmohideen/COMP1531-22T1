'''
Complete the definitions of the following functions using only a single line of code.
'''

def reverse_list(integers):
    '''
    Reverse the list (in-place)
    '''
    integers.reverse()

def minimum(integers):
    '''
    Find and return the lowest number in the list
    '''
    return min(integers)

def sum_list(integers):
    '''
    Return the sum of all numbers
    '''
    return sum(integers)

'''
Testing below!
'''

def test_reverse():
    random_list = [1, 2, 3]
    reverse_list(random_list)
    assert random_list == [3, 2, 1]

def test_min():
    random_list = [1, 2, 3]
    assert minimum(random_list) == 1

def test_sum():
    random_list = [1, 2, 3]
    assert sum_list(random_list) == 6