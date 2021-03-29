from family_list import FamilyList


def setup():
    my_family = FamilyList('Myers')

    my_family.add_member('Thomas', 'Myers', 'Father')
    my_family.add_member('Lolita', 'Myers', 'Mother')
    my_family.add_member('Guy', 'Myers', 'Brother')
    my_family.add_member('Shawna', 'Parks', 'Sister')
    my_family.add_member('Kristina', 'Estabrook', 'Sister')
    my_family.add_member('Iana', 'Myers', 'Daughter')

    my_family.print_list()