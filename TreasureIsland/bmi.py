# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height)**2
print(BMI)
BMI = round(BMI)
print(BMI)
if BMI < 18.5:
    print("Your BMI is under 18.5 they are underweight")
elif 18.5 < BMI < 25:
    print("Your BMI is under 25, you are normal weight")
elif 25 < BMi < 30:
    print("Your BMI is under 30, your are slightly overweight")
elif 30 < BMI < 35:
    print("Your BMI is under 35 you are obese.")
else:
    print("Your BMI is over 35, you are clinically obese")
