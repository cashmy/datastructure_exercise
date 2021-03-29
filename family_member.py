class FamilyMember:

    def __init__(self, first_name, last_name, relationship):
        self.family_member = {
            'first_name': first_name,
            'last_name': last_name,
            'relationship': relationship
        }

    def print_family_member(self):
        print(f'You have a {self.family_member["relationship"]} whose name is {self.family_member["first_name"]} {self.family_member["last_name"]} ')
