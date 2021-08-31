def show_count(count: int, word: str) -> str:
    """Passes mypy tests by clearly defining argument and return types"""
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'