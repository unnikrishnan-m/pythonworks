
products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles

total=len(products)
print(total)

# print mobile titles
mobile_tiltle=[p.get("title") for p in products]

print(mobile_tiltle)

# print samsung mobiles

samsung_mobiles=[p.get("title") for p in products if p.get("brand")=="samsung"]


print(samsung_mobiles)

costly_products=max(products,key=lambda d:d.get("price"))

max_price=costly_products.get("price")

costly_products=[p.get("title")for p in products if p.get("price")==max_price]

print(costly_products)

samsung_mobiles=[p  for p in products  if p.get("brand")=="samsung"]

print(len(samsung_mobiles))

all_brands=[p.get("brand") for p in products]

print(all_brands)

brand_count={b:all_brands.count(b) for b in all_brands}

print(brand_count)