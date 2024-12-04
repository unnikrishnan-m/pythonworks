num1=int(input("enter the num1:"))#16
num2=int(input("enter the num2:"))#24
gcd=1                                   
min_num=min(num1,num2)#          ( #1,,,,16 )                   #min_num=num1 if num1<num2 else num2
for i in range(1,min_num+1):       
    if num1%i==0 and num2%i==0:
        gcd=i

print(gcd)        
            
   
