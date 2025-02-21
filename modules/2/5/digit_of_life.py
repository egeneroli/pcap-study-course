def sum_date(text: str) -> int:
    sum: int = 0
    for c in text:
        sum += int(c)
    return sum


text: str = input('enter birth date: ')

print(sum_date(text))