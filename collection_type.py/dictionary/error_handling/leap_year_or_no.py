def is_leapyear(year):
    #error check
     if year<0:
          return False
     if year%100!=0 and year%4==0 or year%400==0 and year%100==0:
          
          return True
     
     else:

           return False
    
def test_is_leap_year():
     assert is_leapyear(2024)==True,"non century chk failed"
     assert is_leapyear(2025)==False,"invalid non century chk failed"
     assert is_leapyear(2000)==False," century leap year chk failed"
     assert is_leapyear(1900)==False,"invalid century chk failed"
     assert is_leapyear(2029)==False,"invalid year chk failed"


try:
     test_is_leap_year()

     print("test case pass")

except Exception as e:

     print("test failed",e)        





         

