# make list of digit patterns
DIGITS = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]


def display(i: int) -> None:
    # validate input
    if i < 0:
        raise ValueError("input must be postive integer")

    # create list of lines to hold results
    lines: list[str] = ["" for _ in range(5)]

    # for each digit in i
    for d in str(i):
        # for each line
        for i in range(5):
            # add corresponding digit segment to line
            lines[i] += DIGITS[int(d)][i] + ' '

    # join result / print
    print('\n'.join(lines))


display(9081726354)