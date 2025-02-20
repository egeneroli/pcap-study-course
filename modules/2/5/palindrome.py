def is_palindrome(s: str) -> bool:
    """determines whether given text is palindrome"""
    return s.lower().replace(' ', '') == s.lower().replace(' ', '')[::-1]


text: str = input("enter text: ")
print(is_palindrome(text))