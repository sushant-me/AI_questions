"""
Write a program to replace a word in a sentence.
"""

def replace_word(sentence, old_word, new_word):

    return sentence.replace(old_word, new_word)

# Example usage:
sentence = "Hello world, welcome to the world of Python."
old_word = "world"
new_word = "Earth"
modified_sentence = replace_word(sentence, old_word, new_word)
print(modified_sentence)  # Output: "Hello Earth, welcome to the Earth of Python."