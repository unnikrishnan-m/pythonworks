from json import load

f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\processing_json\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data))

#print all country names

all_country_names=[country.get("name")for country in data]


# print(all_country_names)

#print all region

all_region=[country.get("region")for country in data]

#print(set(all_region))

region_count={region:all_region.count(region) for region in all_region}

#print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))

# 
# capital of india

country_capital=[country.get("capital") for country in data if country.get("name")=="india"]

print(country_capital)


#most number of boaders

country_borders_count={country.get("name"):len(country.get("borders",[]))for country in data}

print(country_borders_count)
 
max_borders_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_borders_country)


# most populated country

populated_country=max(data,key=lambda country:country.get("populaton",0)).get("name")

print(populated_country)

alfa_three_code=[country.get("borders") for country in  data if country.get("name")=="india"]

for code in alfa_three_code:

    for country in data:

        if country.get("alpha3code")==code:
            print(country.get("name"))