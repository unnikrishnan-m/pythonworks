employee={"id":100,"name":"das","dept":"sales","sal":25000}
print(employee["name"])


product={"id":100,"title":"goodday","price":55,"brand":"britania"}

print(product["price"])

product["price"]=70

print(product["price"])


product["brand"]="Parle"


print(product["brand"])


product["use_by_date"]="26-04-2025"

product["offer"]=5

print(product)


#add offer as 10 if offer exist else add offer as 20

if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20

print(product)    
