class BirthdayLocations:

    def __init__(self):
        self.old_locations = {'Nebraska', 'South Dakota', 'Minnesota',
                              'California', 'Arizona', 'Oklahoma', 'Missouri',
                              'Wisconsin', 'Wales', 'Scotland', 'Austria'}
        self.future_locations = {'Japan', 'Greece', 'Holy Lands'}
        self.locations = self.old_locations.union(self.future_locations)

    def places(self):
        print('\n\nYour Birthday locations both past, present, and future are: ')
        for each in self.locations:
            print(f'Location: {each}')
