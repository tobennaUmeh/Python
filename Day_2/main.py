# print('welcome to the print Calculator!')
# a = int(input('What was your total bill?: \n$'))
# b = int(input('How much tip would you like to give? 10, 20, or 15? \n'))
# c = int(input('How many people to split the bill?\n'))

# d = (a * (b/100))/c

# print(f'Each person should pay: ${d}')


def Tip_Calculator():
    print('Welcome to the Tip Calculator!')
    a = float(input('What was your total bill?: $'))
    b = int(input('How much tip would you like to give? 10, 20, or 15? '))
    c = int(input('How many people to split the bill? '))

    tip_percentage = b / 100
    total_tip_amount = a * tip_percentage
    total_bill_with_tip = a + total_tip_amount
    individual_share = total_bill_with_tip / c

    print(f'Each person should pay: ${individual_share:.2f}')
    
    f = input('Do you want to compute again? Y/N\n').lower()
    if f == 'y':
        Tip_Calculator()
    elif f == 'n':
        print('Thanks for using the app')
        return
    else:
        print('Invalid input. Please enter Y or N.')
        Tip_Calculator()

Tip_Calculator()
