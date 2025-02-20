def cypher(text: str, shift: int) -> None:
    # validate inputs
    if not text:
        raise ValueError("non-empty string must be provided")

    if shift < 1 or shift > 25:
        raise ValueError("invalid shift value")

    # create result holder
    result: str = ''

    # iterate through chars in text
    for c in text:
        # skip non-letter chars
        if c.isalpha():
            # encode char by shifting
            # get base char of 'a'/'A' (same case as c)
            a: int = ord('a' if c.islower() else 'A')

            # shift char
            j: int = (ord(c) + shift - a) % 26 + a
            c = chr(j)
        result += c

    return result


text: str = input("enter text to be cyphered: ")
shift: int = int(input("enter shift value 1 to 25 (inclusive): "))
print(cypher(text, shift))