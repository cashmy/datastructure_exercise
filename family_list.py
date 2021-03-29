from family_member import FamilyMember


class FamilyList:

    def __init__(self, family_name):
        self.family_name = family_name
        self.member_list = []

    def add_member(self, first_name, last_name, relationship):
        self.member_list.append(FamilyMember(first_name, last_name, relationship))

    def print_list(self):
        print(f'\n\n===== The {self.family_name} family =====')
        for member in self.member_list:
            FamilyMember.print_family_member(member)
