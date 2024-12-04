def multi_table(num,end):#we can set a defult value for end 'end=10'
    for i in range(1,end+1):
        print(f"{i}*{num}=",num*i)

multi_table(5,10)