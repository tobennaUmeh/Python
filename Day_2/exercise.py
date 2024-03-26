two_digit_number = input()


a = str(two_digit_number)
# b = float([*a])[1] + float([*a])[2]
int1 = int([*a][0])
int2 = int([*a][1])

total = int1 + int2

print(total)

print( 2 ** 3)

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_sqr = float(height) ** 2
float_weight = float(weight)

BMI = float_weight / height_sqr

print(round(BMI))

age = input()

age_in_float = float(age)
age_in_float_in_weeks = age_in_float * 52
age_in_total = 90 * 52

age_left_in_weeks = age_in_total - age_in_float_in_weeks

print(f"You have {age_left_in_weeks:.0f} weeks left")
