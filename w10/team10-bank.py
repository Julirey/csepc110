bank_accounts =[]
balances = []
total = 0
average = 0
highest_balance = 0
account = None
value = 0
update = 'yes'

print('Enter the names and balances of the bank accounts (type quit when done)')

while account != 'quit':
    account = input('What is the name of the account? ')
    if account != 'quit':
        bank_accounts.append(account)
        value = float(input('What is the balance of that account? '))
        balances.append(value)

    print()

while update != 'no':
    print()
    print('Account Information')
    for i in range(len(bank_accounts)):
        print(f'{i}. {bank_accounts[i]} - {balances[i]:.2f}')



    for k in balances:
        total += k

    print()
    print(f'Total: ${total:.2f}')

    average = total / len(balances)

    print()
    print(f'Average: ${average:.2f}')

    for l in range(len(balances)):
        if balances[l] > highest_balance:
            highest_balance = balances[l]
            index = l

    print(f'Highest Balance: {index}. {bank_accounts[index]} - {balances[index]}')


    print()
    update = input('Do you wish to update an account? ')
    if update != 'no':
        print()
        update_index = int(input('Which account index do you want to update?'))
        balances[update_index] = float(input('What is the new amount? '))

print()