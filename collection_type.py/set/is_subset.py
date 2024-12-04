st1={1,2,3,4,5}

st2={1,2,3,4,5,7,8,9}

print(st1.issubset(st2))


#superset

print(st2.issuperset(st1))



#symmetric diiference (AuB)-(AnB)
symmetric_difference_set=st1.symmetric_difference(st2)
print(symmetric_difference_set)

st1.update(st2)
print(st1)