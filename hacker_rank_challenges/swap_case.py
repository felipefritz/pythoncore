def swap_case(s):
    string = ''

    for char in iter(s):
        if char.islower():
            string += char.upper()
        else:
            string += char.lower()
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)