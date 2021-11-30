from graph import __version__
from graph.graph import  Graph, Vertex
#  ,business_trip

def test_version():
    assert __version__ == '0.1.0'

import pytest



def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44





#######################################Code Challange 36############################################## 
def test_breadth_first_search():
    graph = Graph()

    yousef = graph.add_node('yousef')
    mohammad = graph.add_node('mohammad')
    abd = graph.add_node('abd')
    jariry = graph.add_node('jariry')

    graph.add_edge(yousef,mohammad)
    graph.add_edge(mohammad,abd)
    graph.add_edge(abd,jariry)

    assert graph.breadth_first_search(yousef) ==  ['yousef' ,'mohammad' ,'abd','jariry'] 



####################################### Code Challange 37 ##############################################
def test_business_trip():
  graph = Graph()

  node1 = graph.add_node('Pandora')
  node2 = graph.add_node('Arendelle')
  node3 = graph.add_node('Metroville')
  node4 = graph.add_node('Monstropolis')
  node5 = graph.add_node('Narnia')
  node6 = graph.add_node('Naboo')

  graph.add_edge(node1,node2,150)
  graph.add_edge(node1,node3,82)
  graph.add_edge(node2,node3,99)
  graph.add_edge(node2,node4,42)
  graph.add_edge(node3,node4,105)
  graph.add_edge(node3,node5,37)
  graph.add_edge(node3,node6,26)
  graph.add_edge(node4,node6,73)
  graph.add_edge(node5,node6,250)
  cities = [node1,node2,node3]
  
  assert graph.business_trip(cities) == (True, '$249')