def wondrous(start):
    '''
    Returns the wondrous sequence for a given number.

    The Wondrous Sequence is generated by the simple rule:

    If the current term is even,
        the next term is half the current term.
    If the current term is odd,
        the next term is three times the current term, plus 1.

    For example, the sequence generated by starting with 3 is:

    3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    '''
    current = start
    sequence = []

    while current != 1:
        sequence.append(current)
        if (current % 2 == 0):
            current /= 2
        else:
            current = (current * 3) + 1

    return sequence
