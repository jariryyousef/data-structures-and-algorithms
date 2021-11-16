from quick_sort.quick_sort import QuickSort

def test_QuickSort():
    arr = [8,4,23,42,16,15]

    actual = QuickSort(arr,0,len(arr)-1)
    excepted = [4, 8, 15, 16, 23, 42]
    assert actual == excepted


def test_Reverse_sorted():
    arr = [20,18,12,8,5,-2]
    actual = QuickSort(arr,0,len(arr)-1)
    excepted = [-2, 5, 8, 12, 18, 20]
    assert actual == excepted


def test_Few_uniques():
    arr = [5,12,7,5,5,7]
    actual = QuickSort(arr,0,len(arr)-1)
    excepted = [5, 5, 5, 7, 7, 12]
    assert actual == excepted


def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    actual = QuickSort(arr,0,len(arr)-1)
    excepted = [2, 3, 5, 7, 11, 13]
    assert actual == excepted