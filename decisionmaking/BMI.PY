# program to calculate BMI
# BMI = weight in kg / height in meter square
# DATA

#print under weight if bmi < 19
#print normal weight if bmi 19 to 25
#print overweight if bmi 25 to <30
#print obese if bmi >=30


weight_in_kg=int(input("enter the value in kg => "))

height_in_cm=int(input("enter the value in cm => "))

height_in_meter=height_in_cm/100

Bmi=weight_in_kg/(height_in_meter**2)

BMI=round(Bmi)

print(BMI)

if BMI<19:
    print("under weight")

elif BMI<25:
    print("normal weight")

elif BMI<30:
    print("overweight")

elif BMI>=30:
    print("obese")
else:
    ("invalid")
