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
        if not c.isalpha():
            continue

        # encode char by shifting
        # get base char of a with proper case
        a: int = ord('a' if c.islower() else 'A')

        # shift char
        i: int = ord(c)
        j: int = (i + 1 - a) % 26 + a
        c = chr(j)
        result += c

    return result


text: str = input("enter text to be cyphered: ")
shift: int = int(input("enter shift value 1 to 25 (inclusive): "))
print(cypher(text, shift))