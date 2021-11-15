from sort import __version__
from sort.sort import mergeSort

def test_version():
    assert __version__ == '0.1.0'

def test_mergeSort():
    arr = [8,4,23,42,16,15]

    actual = mergeSort(arr)
    excepted = [4, 8, 15, 16, 23, 42]
    assert actual == excepted


def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    actual = mergeSort(arr)
    excepted = [-2, 5, 8, 12, 18, 20]
    assert actual == excepted


def test_few_uniques():
    arr = [5,12,7,5,5,7]
    
    actual = mergeSort(arr)
    excepted = [5, 5, 5, 7, 7, 12]
    assert actual == excepted


def nearly_sorted():
    arr = [2,3,5,7,13,11]
    
    actual = mergeSort(arr)
    excepted = [2, 3, 5, 7, 11, 13]
    assert actual == excepted