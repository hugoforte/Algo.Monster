
from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

#todo - make more space efficient
def ternary_tree_paths(root: Node) -> List[str]:
    if root is None:
        return None
    if len(root.children) == 0:
        return [str(root.val)]

    paths_from_me = []
    for child in root.children:
        for child_path in ternary_tree_paths(child):
            paths_from_me.append(str(root.val) +  '=>'  + str(child_path))
    return paths_from_me

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter("1 3 2 1 5 0 3 0 4 0".split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)