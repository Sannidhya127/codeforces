'''
Vanya really likes math. One day when he was solving another math problem, he came up with an interesting tree. This tree is built as follows.

Initially, the tree has only one vertex with the number 1
 — the root of the tree. Then, Vanya adds two children to it, assigning them consecutive numbers — 2
 and 3
, respectively. After that, he will add children to the vertices in increasing order of their numbers, starting from 2
, assigning their children the minimum unused indices. As a result, Vanya will have an infinite tree with the root in the vertex 1
, where each vertex will have exactly two children, and the vertex numbers will be arranged sequentially by layers.

Part of Vanya's tree.
Vanya wondered what the sum of the vertex numbers on the path from the vertex with number 1
 to the vertex with number n
 in such a tree is equal to. Since Vanya doesn't like counting, he asked you to help him find this sum.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

This is followed by t
 lines — the description of the test cases. Each line contains one integer n
 (1≤n≤1016
) — the number of vertex for which Vanya wants to count the sum of vertex numbers on the path from the root to that vertex.

Output
For each test case, print one integer — the desired sum.

'''




def print_tree(tree, level=0):
    '''Prints tree structure in a human readable format'''
    if isinstance(tree, list):
        print('  ' * level + '|_' + str(tree[0]))
        for child in tree[1:]:
            print_tree(child, level + 1)
    else:
        print('  ' * level + '|_' + str(tree))

def find_in_tree(tree, node):
    if node in tree:
        return True
    return any(find_in_tree(subtree, node) for subtree in tree if isinstance(subtree, list))
# Constructing tree as given in problem set

def path(node, end, tree, path=[]):
    if node in tree:
        path.append(node)
        for subtree in tree:
            if isinstance(subtree, list):
                path.append(subtree)
                return path
tree = [1, [2, [4, [8, 9]], [5, [10, 11]]], 3, [6, [12, 13], 7, [14, 15]]]
print_tree(tree)

def find_path(tree, start_node, end_node):
    stack = [(tree, [tree[0]])]
    while stack:
        node, path = stack.pop()
        if node[0] == end_node:
            if start_node in path:
                return path
            else:
                continue
        for child in node[1:]:
            if isinstance(child, list):
                stack.append((child, path + [child[0]]))
    return []

while True:
    init_node = int(input("initial node: "))
    end_node = int(input("end node: "))
    if not find_in_tree(tree, init_node):
        print("Init Node not found")
    elif not find_in_tree(tree, end_node):
        print("End Node not found")
    else:
        break

path = find_path(tree, init_node, end_node)
print(sum(path))