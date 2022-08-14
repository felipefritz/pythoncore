def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)


def mutate_string(string, position, character):
    """
        example: string = 'abcd'
        character = 'f'
        position: 1
        return:  afcd
    """
    string = string[:position] + character + string[position + 1:]
    return string


def count_substring(string, sub_string):
    """count occurences of a substring in a string"""
    counter = 0
    for s in (range(len(string))):
        if string[s:].startswith(sub_string):
            counter += 1
    return counter


def check_char_type_in_string(string):
    """
    You can change the isupper() for other verification like: isalnum()|
    return true or false
    """
    return any(char.isupper() for char in string)


