cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]


#count of vehicles

print(f"total vehicles {len(cars)}")

#print available colors of beleno

beleno_colors=[c.get("colors")for c in cars if c.get("name"=="beleno")]



print(beleno_colors)


#print all brands

all_brands=[c.get("brand") for c in cars]

print(set(all_brands)) #used set for no dupliction


#print car names available in amt transmission

amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_cars)

#the cars are avilable in blue color

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_cars)


#print all transmission

#all_transmossions={t for c in cars for t in c.get("transmossions")}

#print(all_transmossions)

costly_cars=max(cars,key=lambda d:d.get("price"))

print(costly_cars)

low_cost_car=min(cars,key=lambda d:d.get("price"))

print(low_cost_car)

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_cars_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_cars}
print(sorted_cars_name)

