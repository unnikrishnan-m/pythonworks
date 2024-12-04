num1=int(input("enter num1  :"))

num2=int(input("enter num2 :"))


try:
    result=num1/num2

    print(result)

except Exception as e:
    # num2=int(input("enter number 2 :"))

    # result=num1/num2

    print(e)
finally:
    print("file write")

    print("database commit")