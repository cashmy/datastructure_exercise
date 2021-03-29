from contestant import Contestant
import random


class SweepStakes:

    def __init__(self, sweepstakes_name):
        self.sweepstakes_name = sweepstakes_name
        self.contestant_list = []

    def add_contestant(self, first_name, last_name):
        self.contestant_list.append(Contestant(first_name, last_name))

    def pick_winner(self):
        winner_index = random.randint(0, len(self.contestant_list) - 1)
        winner = self.contestant_list[winner_index]
        winner.winner_status = True
        print(f'\n\nThe winner of the Sweepstakes "{self.sweepstakes_name}" is: {winner.first_name} {winner.last_name} ')

    def enroll_contestants(self):
        self.add_contestant('Happy', 'Smith')
        self.add_contestant('Cash', 'Myers')
        self.add_contestant('David', 'LaGrange')
        self.add_contestant('Michael', 'Terrill')
        self.add_contestant('Nevil', 'Seibel')
        self.add_contestant('Pascal', 'Pascarella')
        self.add_contestant('Brett', 'Johnson')
