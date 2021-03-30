from binary_node import BinaryNode


def create_tree():
    root = BinaryNode(12)
    root.insert_node(6)
    root.insert_node(14)
    root.insert_node(3)
    root.insert_node(7)
    root.insert_node(13)
    root.insert_node(18)

    print('\n\nNode entry order: 12, 6, 14, 3, 7, 13, 18')
    print('This uses an in-order traversal method.')
    print('Printing the sorted tree')
    root.print_tree()

    print('\n\nNode entry order: 12, 6, 14, 3, 7, 13, 18')
    print('This uses a pre-order traversal method.')
    print('Printing the sorted tree')
    root.print_tree_pre_order()

    print('\n\nNode Search Tests:')
    root.search_tree(13)
    root.search_tree(6),
    root.search_tree(5)
