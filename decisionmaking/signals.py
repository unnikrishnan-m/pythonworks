# check signal is red or green or yellow

signal=input("enter the signal colur").lower()     #.lower() : use for convert uppercase to lowercase

if signal=="green":
    print("you can go")

elif signal=="red":
    print("you can't go ")

elif signal=="yellow":
    print("you can stop  ")

else:
    print("you are fool wrong signal")
