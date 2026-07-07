#--add
# s1={10,20,30,40,50}
# s1.add(77)
# print(s1)

#---remove-Remove an element from a set; it must be a member.
        # If the element is not a member, raise a KeyError.
# s1={10,20,30,40,50}
# s1.remove(70)
# print(s1)

#---pop
# s1={10,20,30,40,50}
# s1.pop()
# print(s1)

#--discard -emove an element from a set if it is a member.
           # Unlike set.remove(), the discard() method does not raise
           # an exception when an element is missing from the set.
# s1={10,20,30,40,50}
# s1.discard(70)
# print(s1)


#---intersection -used to get common value from two set
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s=s1.intersection(s2)
# print(s)

#--difference-used to get different value for comparing s1 and s2
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s=s1.difference(s2)
# print(s)

#symmentric_difference-used to get diff value from both s1 and s2 and same value will be deleted and return none 

# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s=s1.symmetric_difference(s2)
# print(s)

#---intersection_update-used to get common value and return none but they will update s1 by intersection value when you will call s1
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s1.intersection_update(s2)
# print(s1)

#---difference_update-used to get different value and return none but they will update s1 by difference value when you will call s1
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s1.difference_update(s2)
# print(s1)

#symmentric_difference_update-used to get diff value from both s1 and s2 and same value will be deleted and return none if you call them they will update s1 with these value
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s1.symmetric_difference_update(s2)
# print(s1)

#---update-used to update s1 and merge s1 and s2 and remove common values updated occur in original s1 or existing obejcet
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s1.update(s2)
# print(s1)

# #--union-used to update s1 and merge s1 and s2 and remove common values updated occur in new s1 but original objectwill same
# s1={10,20,30,40,50,60,70}
# s2={50,60,70,80,90,100}
# s=s1.union(s2)
# print(s1)
# print(s)

#--issuperset & issubset - here superset is which set who contain all element of a subset and subset is which set which contain few element of a superset
# s1={10,20,30,40,50,60,70}
# s2={50,60,70}
# print(s2.issubset(s1))
# print(s1.issuperset(s2))

