import my_family
from retrieve_month import RetrieveMonth
from birthday_locations import BirthdayLocations
from sweepstakes import SweepStakes
import linked_list_demo
import binary_list
import bst_avl_test


def print_hi(name):
    print(f'Hi, {name}! Welcome to DataStructure Test')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Student')

    # User Story 1a
    year_2021 = RetrieveMonth()
    year_2021.get_month()   # National Pi Day
    # User Story 1b
    cash_birthdays = BirthdayLocations()
    cash_birthdays.places()  # Past, Present, and Future
    # User Story 1c
    new_sweepstakes = SweepStakes("devCodeCamp Give-A-Way")
    new_sweepstakes.enroll_contestants()
    new_sweepstakes.pick_winner()   # Sweepstakes contestants

    # User Story 2
    my_family.setup()

    # User Story 3
    linked_list_demo.exec_linked_list()

    # User Story 4
    binary_list.create_tree()

    # Bonus user story 6
    bst_avl_test.bst_avl_execute_test()
