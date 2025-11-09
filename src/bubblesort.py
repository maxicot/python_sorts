from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


# Iterative bubblesort implementation.
# Either comparisons between elements must be supported
# on the type's level or the `cmp` argument must be provided.
# The default behavior of `cmp` is to check
# whether the first argument is lesser than the second
def bubblesort(array: list, cmp: Callable[[T, T], bool] = lambda x, y: x < y) -> list:
    arr = array
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if not cmp(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
