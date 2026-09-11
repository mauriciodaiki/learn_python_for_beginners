def count_vowels(text):
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    counter = 0
    unique_vowels = set()
    for char in text:
        if char in vowels:
            counter += 1
            unique_vowels.add(char)
    return counter, unique_vowels
