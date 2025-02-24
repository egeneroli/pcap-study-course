def sudoku_validator(s: str) -> bool:
    # parse string to nested list of chars
    x: list[list[str]] = [list(row) for row in s.split()]

    # transpose matrix (flip diagonally to swap rows and columns)
    x_t: list[list[str]] = list(zip(*x))

    # flatten sub-squares to lists
    squares: list[list[str]] = [x[i][j:j + 3] + x[i + 1][j:j + 3] + x[i + 2][j:j + 3] for i in range(0, len(x), 3) for j
                                in range(0, len(x[i]), 3)]

    # check rows, cols and subsquares
    for row in x + x_t + squares:
        if sorted(row) != list('123456789'):
            return False

    # all rows, cols, sub-squares are complete -- sudoku is valid
    return True


s: str = '''
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
'''

s2: str = '''
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''

print(sudoku_validator(s))
print(sudoku_validator(s2))
