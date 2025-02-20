def is_anagram(s1: str, s2: str) -> bool:
    """checks if given strings are anagrams"""
    if not s1 or not s2:
        return False

    return ''.join(sorted(s1)) == ''.join(sorted(s2))


s1: str = input("provide s1: ")
s2: str = input("provide s2: ")
print(is_anagram(s1, s2))