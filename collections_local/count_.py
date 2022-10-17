from collections import Counter
from logs.loggers import Logger
import logging

"""
Methods availables
1. elements() : This method will return you all the elements 
                with count >0. Elements with 0 or -1 count will not be returned.
                
2. most_common(value): This method will return you the most common elements from Counter list.

3. subtract(): This method is used to deduct the elements from another Counter.

4. update(): This method is used to update the elements from another Counter.
"""


def count_items_in_a_list(list: []):
    Logger('info', f'counter running', logger_name=logging.getLogger(__name__))
    try:
        return Counter(list)

    except Exception as e:
        Logger(level='error', message=str(e), logger_name=logging.getLogger(__name__))


def count_most_common_in_object(list: []):
    """Count the most common items in a list"""
    count_most_common = Counter(list).most_common(2)
    Logger('info', f'count_most_common_in_object', logger_name=logging.getLogger(__name__))

    return count_most_common[0][0]


if __name__ == '__main__':
    list_test_1 = [1, 2, 3, 5, 5, 'hello', 'test', 'test', 'test']
    list_test_2 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
    print(count_most_common_in_object(list_test_1))
    print(count_items_in_a_list(list_test_1))
