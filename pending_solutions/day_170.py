""" Patterns """

def find_patterns(text):
    patterns = []
    for word in text.split():
        if word.endswith('ing'):
            patterns.append(word)
    return patterns

text = "He is singing in the garden."
print(find_patterns(text))