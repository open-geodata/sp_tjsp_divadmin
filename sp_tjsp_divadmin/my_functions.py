"""
Pequenas Funções utilizadas no código.
abr/2023
"""

import re


def keep_numbers(my_string):
    """
    Mantem apenas números
    '987978098098098'
    https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python

    :return: _description_
    :rtype: _type_
    """
    return re.sub('[^0-9]', '', my_string)


def find_text_between_parenthesis(my_string):
    """
    _summary_
    https://stackoverflow.com/questions/4894069/regular-expression-to-return-text-between-parenthesis

    """
    return my_string[my_string.find("(") + 1 : my_string.find(")")]


if __name__ == '__main__':
    a = keep_numbers('Michel   333  Metran')
    print(a)
