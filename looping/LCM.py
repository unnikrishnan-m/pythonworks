a=int(input("enter number"))  #16
b=int(input("enter number"))  #24
max= a if a>b else b           #24>16
LCM=max                        #LCM=24                
while(LCM %a!=0 or LCM %b!=0): #24%a!=0 
    LCM=LCM+max                #24+24
print(LCM)                 #48


