# # '''
# # Write a python program vowel.py that

# # takes in a series of words on a single line in from STDIN,

# # passes that input string into a function called find_vowels,

# # which then returns the frequency of how often each vowel appears.

# # This object is then outputted (however you think works best).

# # Assume all input is lowercase or uppercase letters, or spaces.

# # If there are any uppercase letters
# # passed in as part of the input,
# # a ValueError should be thrown

# # and caught in the main part of the code.
# # The user should then be given a clear error

# # First, write a failing unit test that asserts the error is thrown
# # Then modify your code so that the test passes
# # Then, update the if __name__ block to catch the exceptional case.
# # '''

# # def find_vowels(message):
# #     if not message.islower():
# #         raise ValueError

# #     vowels = {}
# #     for character in 'aeiou':
# #         vowels[character] = 0

# #     # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# #     for character in message:
# #         if character in 'aeiou':
# #             vowels[character] += 1

# #     return vowels

# # # https://www.freecodecamp.org/news/if-name-main-python-example/
# # if __name__ == '__main__':
# #     words = input("Please enter a sentence: ")

# #     try:
# #         vowels = find_vowels(words)
# #         for character in 'aeiou':
# #             print(f"{character}: {vowels[character]}")

# #     except ValueError:
# #         print("bla bla bla")

# string = "Usmaan is the best tutor"
# list_version = string.split("t")
# print(list_version)

name = 'Ralph'
def edit_name(new_name):
    global name
    name = new_name

if __name__ == "__main__":
    edit_name("Usmaan")
    print(name)