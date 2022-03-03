def find_vowels(message):
    '''
    which then return the frequency of how often each vowel appears.
    '''
    # 6. ValueError should be thrown
    if not message.islower():
        raise ValueError

    # 4. How can we store frequencies?
    vowels = {}

    for character in 'aeiou':
        vowels[character] = 0

    # 'a':0, 'e':0, 'i': 0, 'o': 0, 'u': 0

    # 5. How can we split a string into an array?
    words = message.split(' ')
    for word in words:
        for character in word:
            if character in 'aeiou':
                vowels[character] += 1

    return vowels

if __name__ == '__main__':
    # 1. takes in a series of words on a single line in from STDIN
    words = input('Please enter a message: ')
    try:
        # 2. passes that input string into a function called find_vowels
        vowels = find_vowels(words)
        for character in 'aeiou':
            print(f"{character}: {vowels[character]}")
    except ValueError:
        # 7. and caught in the main part of the code
        print("Please only enter lowercase letters")
