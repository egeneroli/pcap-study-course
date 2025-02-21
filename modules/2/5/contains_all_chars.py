def contains_all(word: str, chars: str) -> bool:
    for c in word:
        if chars.find(c) == -1:
            return False
    return True


word: str = input('first string: ')
chars: str = input('second string: ')

print(contains_all(word, chars))