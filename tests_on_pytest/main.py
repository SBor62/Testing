def count_vowels(text):
    russian_vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'й'}
    return sum(1 for char in text.lower() if char in russian_vowels)
