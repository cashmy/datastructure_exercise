class BstAvl:
    # Binary Search Tree - AVL (Adelson-Velsky and Landis)

    def __init__(self, data):
        # Note: if "data" is an object, then this class could be refactored to break out a 'key' value from the
        #       rest of the object and use it appropriately
        self.data = data
        self.left_child_node = None
        self.right_child_node = None
        self.height = 1


class BstTree:
    def insert_node(self, node, data):
        # Parameters: Node = object, data = data value, object, or class

        # Perform normal insert operations
        if not node:  # assume root node
            return BstAvl(data)
        elif data < node.data:
            node.left_child_node = self.insert_node(node.left_child_node, data)
        else:
            node.right_child_node = self.insert_node(node.right_child_node, data)
        # Now update the height of the ancestor node
        node.height = 1 + max(self.get_height(node.right_child_node), self.get_height(node.left_child_node))

        # Now determine the balance factor
        balance = self.get_balance(node)
        # Now determine the rotation method: LEFT-LEFT, LEFT-RIGHT, RIGHT-RIGHT, RIGHT-LEFT
        # LEFT-LEFT
        if balance > 1 and data < node.left_child_node.data:
            return self.right_rotate(node)
        # RIGHT-RIGHT
        if balance < -1 and data > node.right_child_node.data:
            return self.left_rotate(node)
        # LEFT-RIGHT
        if balance > 1 and data > node.left_child_node.data:
            node.left_child_node = self.left_rotate(node.left_child_node)
            return self.right_rotate(node)
        # RIGHT-LEFt
        if balance < -1 and data < node.right_child_node.data:
            node.right_child_node = self.right_rotate(node.right_child_node)
            return self.left_rotate(node)

        return node

    def left_rotate(self, node_z):
        node_y = node_z.right_child_node
        subtree_node_2 = node_y.left_child_node

        # Perform rotation
        node_y.left_child_node = node_z
        node_z.right_child_node = subtree_node_2

        # Update heights
        node_z.height = 1 + max(self.get_height(node_z.left_child_node),
                                self.get_height(node_z.right_child_node))
        node_y.height = 1 + max(self.get_height(node_y.left_child_node),
                                self.get_height(node_y.right_child_node))

        return node_y

    def right_rotate(self, node_z):
        node_y = node_z.left_child_node
        subtree_node_3 = node_y.right_child_node

        # Perform rotation
        node_y.right_child_node = node_z
        node_z.left_child_node = subtree_node_3

        # Update heights
        node_z.height = 1 + max(self.get_height(node_z.left_child_node),
                                self.get_height(node_z.right_child_node))
        node_y.height = 1 + max(self.get_height(node_y.left_child_node),
                                self.get_height(node_y.right_child_node))

        # Return the new root
        return node_y

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child_node) - self.get_height(node.right_child_node)

    def print_tree_pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.data), end="")
        self.print_tree_pre_order(node.left_child_node)
        self.print_tree_pre_order(node.right_child_node)

    # a) Left Left Case
    #
    # T1, T2, T3 and T4 are subtrees.
    #          z                                      y
    #         / \                                   /   \
    #        y   T4      Right Rotate (z)          x      z
    #       / \          - - - - - - - - ->      /  \    /  \
    #      x   T3                               T1  T2  T3  T4
    #     / \
    #   T1   T2
    #
    # b) Left Right Case
    #
    #      z                               z                           x
    #     / \                            /   \                        /  \
    #    y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
    #   / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
    # T1   x                          y    T3                    T1  T2 T3  T4
    #     / \                        / \
    #   T2   T3                    T1   T2
    #
    # c) Right Right Case
    #
    #   z                                y
    #  /  \                            /   \
    # T1   y     Left Rotate(z)       z      x
    #     /  \   - - - - - - - ->    / \    / \
    #    T2   x                     T1  T2 T3  T4
    #        / \
    #      T3  T4
    #
    # d) Right Left Case
    #
    #    z                            z                            x
    #   / \                          / \                          /  \
    # T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    #     / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
    #    x   T4                      T2   y                  T1  T2  T3  T4
    #   / \                              /  \
    # T2   T3                           T3   T4
