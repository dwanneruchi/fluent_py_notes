from typing import Optional

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