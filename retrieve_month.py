class RetrieveMonth:

    def __init__(self):
        self.months = ('January', 'February', 'March',
                       'April', 'May', 'June',
                       'July', 'August', 'September',
                       'October', 'November', 'December')
        self.pi = 3.14
        self.month_number = int(self.pi - 1)

    def get_month(self):
        print(f'\n\nThe month of National Pi day is {self.months[self.month_number]}')
