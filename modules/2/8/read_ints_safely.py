def read_int(prompt, min, max):
    s: str = input(prompt)
    try:
        i: float = float(s)
        if i < min or i > max:
            raise Exception
        print("The number is:", i)
        return i
    except ValueError:
        print('Error: wrong input')
    except:
        print(f'Error: the value is not within permitted range [{min}, {max}]')


v = read_int("Enter a number from -10 to 10: ", -10, 10)

# print("The number is:", v)
