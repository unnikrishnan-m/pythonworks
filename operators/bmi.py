#create a python program to calculate BMI

weight_in_kg=int(input("enter the weight in kg :"))

height_in_cm=int(input("enter the height in cm :"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre**2

BMI=round(BMI,1)

print(BMI)