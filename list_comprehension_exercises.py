print("""
    1.- Create a new list that contains fruits names only starting with a vowel.
    fruits = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']

    2.- What is the result of the code given below?
        print([char.upper() for char in "python"])

    3.-Implement multiplication of a matrix with a scalar number with LC.""", end='\n\n')


def _starts_with_a_vowel(list_of_items: list):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [item for item in list_of_items if item[0].capitalize() in vowels]


def get_and_validate_if_exists_numeric_input(text_input: str):

    while True:
        variable = input(text_input)
        if variable.isnumeric():
            variable = int(variable)
            return variable


def _scalar_multiplication():

    matrix_rows = get_and_validate_if_exists_numeric_input('Enter the number of columns for the matrix')
    matrix_cols = get_and_validate_if_exists_numeric_input('Enter the number of rows for the matrix')
    scalar_number = get_and_validate_if_exists_numeric_input('Enter the scalar number')
    print('\n ')
    matrix = [[i + (y * matrix_cols) for i, x in enumerate(range(matrix_cols), 1)] for y in range(matrix_rows)]
    results = [[scalar_number * number for number in row] for row in matrix]

    return matrix, results


if __name__ in "__main__":
    fruits = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']
    print("RESULTS:", end='\n')
    print( '1: ' + str(_starts_with_a_vowel(fruits)), end='\n\n')
    print( '2: ' + str([char.upper() for char in "python"]), end='\n')

    matrix, results = _scalar_multiplication()
    print( f'3:Results:\n Matrix: {str(matrix)} \n '
           f'multiplication of the matrix: {results}')

