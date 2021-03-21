class Bank:

    def __init__(self, account, cash_amount):
        self.account = account
        self.cash_amount = cash_amount

    def deposit_cash(self):
        return account + cash_amount

    def withdraw_cash(self):
        return account - cash_amount

    def close_account(self):
        return account

    try:
        client_name = input('Enter you name, please: ')
        open_account = input('Would you like to open an account:\nif yes - print y, if not - any symbol: ')

        if open_account != 'y':
            print('We are sorry about your decision')
            exit()
        account = int(input('To activate account, deposit some sum: '))
        client_option = input('Choose your option, please:\n1 for deposit, 2 for withdrawal, 3 for close account: ')

        if client_option == '1':
            cash_amount = int(input('Input an amount you wanna deposit on: '))
            total_account = account + cash_amount
            print('Operation is succeeded.\nAccount state: {} USD'.format(total_account))

        elif client_option == '2':
            cash_amount = int(input('Input an amount you wanna withdraw: '))
            total_account = account - cash_amount
            if total_account < 0:
                print('No enough money. Your account state: {} USD'.format(account))
            else:
                print('Operation is succeeded.\nAccount state: {} USD'.format(total_account))

        elif client_option == '3':
            print('Your account is closed.\nGet {} USD.'.format(account))
            exit()

        else:
            print('No such option!')

    except ValueError:
        print('Incorrect input.')
