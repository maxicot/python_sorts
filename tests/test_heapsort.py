from src.heapsort import heapsort as given_sort


def test_general():
    assert given_sort([0, 8, 3, -1, 5]) == [-1, 0, 3, 5, 8]
    assert given_sort([0, 8, 3, -1, 5], cmp=lambda x, y: x > y) == [8, 5, 3, 0, -1]


def test_special():
    assert given_sort([]) == []
    assert given_sort([1]) == [1]


class Custom:
    def __init__(self, n: int):
        self.inner = n

    def __eq__(self, rhs) -> bool:
        return self.inner == rhs.inner

    def into(self) -> int:
        return self.inner


def test_custom():
    assert given_sort([Custom(2), Custom(1)], cmp=lambda x, y: x.inner < y.inner) == [
        Custom(1),
        Custom(2),
    ]
