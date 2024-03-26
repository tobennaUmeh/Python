print("Thank you for choosing Python Pizza Deliveries!")
size = input().lower() # What size pizza do you want? S, M, or L
add_pepperoni = input().lower() # Do you want pepperoni? Y or N
extra_cheese = input().lower() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇\

S = 15
M = 20
L = 25

def pizza_cost(size, add_pepperoni, extra_cheese):
    total_price = 0  # Initialize total price

    # Calculate base price based on size
    if size == 's':
        total_price += S
    elif size == 'm':
        total_price += M
    elif size == 'l':
        total_price += L
    else:
        print('Please select a valid option')
        return

    # Add $2 for pepperoni if selected
    if add_pepperoni == 'y':
        total_price += 2

    # Add $1 for extra cheese if selected
    if extra_cheese == 'y':
        total_price += 1

    # Print the final bill
    print(f'Thank you for choosing Python Pizza Deliveries! Your final bill is: ${total_price}.')

pizza_cost(size, add_pepperoni, extra_cheese)