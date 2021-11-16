from stack_and_queue.stack_queue_brackets import *

def test_true():
    actual= True
    expected=is_par_balanced('{}')
    assert actual == expected
    actual= True
    expected=is_par_balanced('{}(){}')
    assert actual == expected
    actual= True
    expected=is_par_balanced('(){}[[]]')
    assert actual == expected
    

def test_Expected_failure():
    actual=is_par_balanced('[({}]')
    expected=False
    assert actual == expected


def test_false():
    assert is_par_balanced('(](') == False
    assert is_par_balanced('{(})') == False
    assert is_par_balanced('{') == False
    assert is_par_balanced(')') == False
    assert is_par_balanced('[}') == False