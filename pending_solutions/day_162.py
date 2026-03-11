def count_words(sentence):
    """ Count number of words in a sentence. """
    return len(sentence.split())

# Example usage:
sentence = "https://example.com is an example sentence."
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")