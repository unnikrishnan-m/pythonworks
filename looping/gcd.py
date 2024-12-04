a=int(input("ennter number"))  #16
b=int(input("ennter number"))  #24
min= a if a<b else b           #24>16
gcd=min                        #LCM=24                
while(gcd %a==0 or gcd %b==0): #24%a!=0 
    gcd=gcd+min               #24+24
print(gcd) 