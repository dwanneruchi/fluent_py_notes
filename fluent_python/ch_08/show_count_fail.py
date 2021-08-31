def show_count(count, word):
    """This function doesn't have static checking we need for mypy

    Pass: mypy show_count_fail.py

    Fails: mypy --disallow-untyped-defs show_count_fail.py
      - This will fail 3 times since we don't have expect type for either argument or return value

    Passes, but could fail in the future: mypy --disallow-incomplete-defs show_count_fail.py
    - Once we add a type for either argument or return but not for all this will start to fail
    """
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'