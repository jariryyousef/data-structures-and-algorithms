from insertion.insertion import *

def test_Reverse():
    arr= [8,4,23,42,16,15]
    actual = inserttion(arr)
    excepted = [4,8,15,16,23,42]
    assert actual == excepted

def test_Few_uniques():
    arr= [5,12,7,5,5,7]
    actual = inserttion(arr)
    excepted = [5,5,5,7,7,12]
    assert actual == excepted

def test_Nearly_sorted():
    arr= [2,3,5,7,13,11]
    actual = inserttion(arr)
    excepted = [2,3,5,7,11,13]
    assert actual == excepted

def test_big_array():

    arr= [2,3,5,7,13,11,22,13,31,44,66,88,55,3,4,23,61,87,12,1,0]
    actual = inserttion(arr)
    excepted = [0,1,2,3,3,4,5,7,11,12,13,13,22,23,31,44,55,61,66,87,88]
    assert actual == excepted