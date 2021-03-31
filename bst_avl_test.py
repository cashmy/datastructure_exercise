from bst_avl import BstAvl, BstTree


def bst_avl_execute_test():
    my_tree = BstTree()
    node = None

    print(f'\n\n=== Binary Search Tree (AVL) ===')
    node = my_tree.insert_node(node, 10)
    node = my_tree.insert_node(node, 20)
    node = my_tree.insert_node(node, 30)
    node = my_tree.insert_node(node, 40)
    node = my_tree.insert_node(node, 50)
    node = my_tree.insert_node(node, 25)

    print('\n\nPreorder traversal of the constructed AVL tree is: ')
    my_tree.print_tree_pre_order(node)
