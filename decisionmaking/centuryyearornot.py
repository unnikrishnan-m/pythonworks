#check century year or not

year=int(input("enter the year to check"))

if year%100==0:

    print(f"{year} is a century year")

else:

    print(f"{year} is not a century year")