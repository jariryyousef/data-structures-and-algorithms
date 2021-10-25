# from stack_queue_animal_shelter.stack_queue_animal_shelter import *
from stack_queue_animal_shelter.stack_queue_animal_shelter import *

def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('isco', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('tott', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['isco', 'tott']
    assert actual == excepted


def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('tes1', 'test2')
    excepted = 'This not cat or dog'
    assert actual == excepted


def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('isco', 'dog')
    animal.enqueue('tott', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['isco', 'tott']
    assert actual == excepted


def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('animal')
    excepted = 'This not cat or dog'
    assert actual == excepted
