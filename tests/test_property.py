from hypothesis import given
from hypothesis import strategies as st
from src.heapsort import heapsort
from src.mergesort import mergesort
from src.bubblesort import bubblesort
from src.quicksort import quicksort


@given(st.lists(st.integers(), max_size=100))
def test_property(arr):
    result = sorted(arr)

    for s in [heapsort, mergesort, bubblesort, quicksort]:
        assert result == s(arr)
