from linkedlist import LinkedList


def exec_linked_list():
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)

    linked_list.add_to_beginning(25)

    data_exists = linked_list.contains(60)
    print(f'\n\nThe data of 65 was found: {data_exists}')