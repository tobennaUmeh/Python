print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_names = name1 + name2
combined_names_lowercase = combined_names.lower()

t = combined_names_lowercase.count('t')
r = combined_names_lowercase.count('r')
u = combined_names_lowercase.count('u')
e = combined_names_lowercase.count('e')
l = combined_names_lowercase.count('l')
o = combined_names_lowercase.count('o')
v = combined_names_lowercase.count('v')



first_number = t + r + u + e
second_number = l + o + v + e

combined_love_numbers = int(str(first_number) + str(second_number))

if combined_love_numbers < 10 or combined_love_numbers > 90:
  print(f'Your score is {combined_love_numbers}, you go together like coke and mentos.')
elif combined_love_numbers >= 40 and combined_love_numbers <= 50:
  print(f'Your score is {combined_love_numbers}, you are alright together.')
else: 
  print(f'Your score is {combined_love_numbers}.')