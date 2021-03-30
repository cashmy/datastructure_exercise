from linkedlist import LinkedList


def exec_linked_list():
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)

    linked_list.print_list()
    print('\nAdding an element(25)')
    linked_list.add_to_beginning(25)
    linked_list.print_list()

    data_exists = linked_list.contains(60)
    print(f'\nThe data of 60 was found: {data_exists}')

    print('\nNow deleting node 60')
    linked_list.delete_node(60)
    linked_list.print_list()

    print(f'\nNow reinsert 60 after 55')
    linked_list.insert_node_data(55, 60)
    linked_list.print_list()
