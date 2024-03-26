weight = float(input('What is your weight'))
height = float(input('What is your height'))
float_weight = float(weight)
height_sqr = height ** 2
BMI = float_weight / height_sqr

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
  print(f'Your BMI is {BMI}, you have a normal weight.')
elif BMI >= 25 and BMI < 30:
  print(f'Your BMI is {BMI}, you are slightly overweight.')
elif BMI >= 30 and BMI < 35:
  print(f'Your BMI is {BMI}, you are obese.')
elif BMI >= 35:
  print(f'Your BMI is {BMI}, you are clinically obese.')
else:
  print('Please check the values')