from tree import Tree

def test_find():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(7)
    tree.add(9)
    assert tree.find(5).data == 5
    assert tree.find(3).data == 3
    assert tree.find(8).data == 8
    assert tree.find(2).data == 2
    assert tree.find(4).data == 4
    assert tree.find(7).data == 7
    assert tree.find(9).data == 9
    assert tree.find(10) == None
    assert tree.find(1) == None
    tree.deleteTree()
    assert tree.find(5) == None
    assert tree.find(3) == None
    assert tree.find(8) == None
    assert tree.find(2) == None
    assert tree.find(4) == None
    assert tree.find(7) == None
    assert tree.find(9) == None
    assert tree.find(10) == None
    assert tree.find(1) == None
