from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


# Recursive quicksort implementation.
# Either comparisons between elements must be supported
# on the type's level or the `cmp` argument must be provided.
# The default behavior of `cmp` is to check
# whether the first argument is lesser than the second
def quicksort(array: list, cmp: Callable[[T, T], bool] = lambda x, y: x < y) -> list:
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if cmp(arr[j], pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def inner(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            inner(arr, low, p - 1)
            inner(arr, p + 1, high)

        return arr

    return inner(array, 0, len(array) - 1)
