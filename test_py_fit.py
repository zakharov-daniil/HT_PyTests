import pytest
from one_hot_encoder import fit_transform


def test_none():
    with pytest.raises(TypeError):
        result = fit_transform()

def test_empty():
    result = fit_transform([])
    assert result == []

@pytest.mark.parametrize('text, expected', [
    (['Moscow', 'New York', 'Moscow', 'London'],
     [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]),
    (['hello', 'world'], [('hello', [0, 1]), ('world', [1, 0])]),
    (['red', 'red', 'green'], [('red', [0, 1]), ('red', [0, 1]), ('green', [1, 0])]),
    (['123'], [('123', [1])])
])
def test_fit_texts(text, expected):
    assert fit_transform(text) == expected


if __name__ == '__main__':
    pytest.main()
