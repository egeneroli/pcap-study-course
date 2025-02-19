def mysplit(s: str) -> list:
    # create list for results
    results: list[str] = []

    # start building word
    word: str = ''

    # iterate through chars in s, add space to end
    for c in s + ' ':
        # if not space, add to word
        if c != ' ':
            word += c

        # if space, add word to results, reset word to empty (skip if word already empty)
        elif word:
            results.append(word)
            word = ''

    return results


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))