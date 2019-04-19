import random

from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """

    for v_dict in data:
        try:
            v_dict['name'] = v_dict['name'].title()
        except KeyError:
            continue
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """

    for counter in range(len(data)):
        for key in redundant_keys:
            del data[counter][key]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """

    return list(filter(lambda v_dict: value in v_dict.values(), data))


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """

    return min(data, default = None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """

    v_result = None
    for v_item in data:
        if v_result is None:
            v_result = str(v_item)
            continue
        if len(str(v_item)) < len(v_result):
            v_result = str(v_item)
    return v_result


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """

    v_data = [0, 0]
    flag = False
    for v_index, v_dict in enumerate(data):
        try:
            if v_dict[key] < v_data[1] or not flag:
                v_data[0], v_data[1] = v_index, v_dict[key]
                flag = True
        except KeyError:
            continue
    return data[v_data[0]]


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """

    v_data = []
    for v_list in data:
        if len(v_list):
            v_list.sort(reverse=True)
            v_data.append(v_list[0])
    v_data.sort(reverse=True)
    return v_data[0]


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """

    return sum(map(lambda x: x, data))


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """

    return sum(map(lambda x: ord(x), text))


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """

    def is_prime(value):
        if value == 1:
            return False
        for i in range(2, value):
            if value % i == 0:
                return False
        return True

    v_out = 1
    while v_out <= 200:
        if is_prime(v_out):
            yield v_out
        v_out += 1


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each
    element is random letter from latin alphabet

    """

    return [chr(random.randint(97, 122)) for i in range(20)]
