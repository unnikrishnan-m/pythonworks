years_read="C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\file_write.txt"

century_path="C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\century_year.txt"

f_leap_year_path="C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\leap_year.txt"

f_read=open(years_read,"r")

f_century=open(century_path,"w")

leap_year_path=open(f_leap_year_path,"w")



for year in f_read:

    year=int(year)

    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        leap_year_path.write(str(year)+"\n")

f_read.close()

f_century.close()

f_leap_year_path.close()










