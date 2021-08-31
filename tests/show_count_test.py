from pytest import mark

from fluent_python.show_count import show_count, show_count_plural

# this is a pretty cool way to do multiple tests, shown below
@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts'),
])
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected

def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'

def test_irregular() -> None:
    got = show_count_plural(2, 'child', 'children')
    assert got == '2 children'