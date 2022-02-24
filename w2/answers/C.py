'''
Complete the definitions of the following functions using only a single line of code.

Test-driven development is a software development process relying on
software requirements being converted to test cases
before software is fully developed, and
tracking all software development by repeatedly
testing the software against all test cases.


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




def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]
    print("PASSED")

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1
    print("PASSED")

def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
    print("PASSED")

if __name__ == "__main__":
    test_reverse()
    test_min()
    test_sum()