class Bank:

    def __init__(self, money, sum_, funds):
        self.money = money
        self.sum_ = sum_
        self.funds = funds
        self.currency = 'USD'
        self.option = {'deposit': '1', 'withdraw': '2', 'close': '3'}

    def open_account(self):
        client_decision = input('Would you like to open an account:\nif yes - print y, if not - any symbol: ')
        if client_decision != 'y':
            print('We are sorry about your decision')
            exit()
        return 'Your request is processing'

    def client_request(self):
        client_option = input('Choose your option, please:\n1 for deposit, 2 for withdrawal, 3 for close account: ')
        if client_option == self.option['close']:
            return self.close_account()
        self.sum_ = int(input('Input a sum: '))
        if client_option == self.option['deposit']:
            return self.deposit_cash()
        elif client_option == self.option['withdraw']:
            return self.withdraw_cash()
        else:
            print('No such option!')
            raise ValueError('Incorrect input')

    def deposit_cash(self):
        print('Your account: {} {}.'.format((self.money + self.sum_), self.currency))
        return self.money + self.sum_

    def withdraw_cash(self):
        if self.money - self.sum_ < 0:
            print('Insufficient funds')
        return 'Your assets: {} {}'.format(self.money, self.currency)

    def close_account(self):
        print('Your account is closed.\nGet {} {}.'.format(self.money, self.currency))
        return self.money


client = Bank(0, 0, 0)
print(client.open_account())
while True:
    print(client.client_request())
