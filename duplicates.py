l1=[1,5,5]
l2=[3,4,5,5,10]
l3=[5,5,10,20]

#type casting into a set
s1=set(l1)
s2=set(l2)
s3=set(l3)

# s1.intersection_update(s2)
# s3.intersection_update(s1)
# print(list(s3))

#another way to take intersection of a set
s1s2=s1.intersection(s2)
final_set=s3.intersection(s1s2)
final_list=list(final_set)
print(final_list)