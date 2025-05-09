amount_due = 50
while amount_due > 0:
    amount_owed = 0
    amount_paid = 0
    insert = 0
    print(f'Amount Due: {amount_due}')
    insert = int(input('Insert Coin: '))

    if insert != 5 and insert != 10 and insert != 25:
        print(f'Amount Due: {amount_due}')
        insert = int(input('Insert Coin: '))

    else:
        amount_due = amount_due - insert

else:
    print(f'Change Owed: {amount_paid - amount_due}')
