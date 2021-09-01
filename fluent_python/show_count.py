from __future__ import annotations
from typing import Optional, TypeVar
from collections.abc import Iterable
from collections import Counter

def show_count(count: int, word: str) -> str:
    """Passes mypy tests by clearly defining argument and return types"""
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'

def show_count_plural(count: int, singular: str, plural: Optional[str] = None) -> str:
    """
    Notes for David:
    - This is built to handle optional spelling of plural if not just adding an S (e.g. Mouse -> Mice)
    - Optional[str] = None means that plural can either be a str type of a None type, we need to add the default here
        - default must be added here otherwise Python will treat it as required at runtime (outside of mypy test)
    """
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'


def tokenize(text: str) -> list[str]:
    """Example of using a collection, in this case output will be a list where each element is a string"""
    return text.upper().split()

# an example using iterable instead of list, which is more flexible
FromTo = tuple[str, str] # we create an alias which we can reference further on

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    """By using Iterable instead of list we can accept any iterable (tuple, list, generator - i think)"""
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

# An example using generic types, which I ran across in Java!
# Generic types will allow us to ensure our return matches the type of the argument input
T = TypeVar('T')

def our_mode(data: Iterable[T]) -> T:
    """Able to take a sequence of any type and guarantee we output the same data type (representing mode)
    This is pretty cool - the pytest shows how we can pass in a tuple/list/etc, and varying data types but still things work
    """
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]