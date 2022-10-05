print("Hello! Welcome to the BMI Calculator. Please follow the upcoming steps. ")

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg? "))
bmi = round(weight / height ** 2)


if bmi <= 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")
