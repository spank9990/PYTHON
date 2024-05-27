n = int(input("enter the size of list:"))

list=[]
for _ in range(n):
    num=int(input())
    list.append(num)

print(list)
idx1=int(input("enter index 1:"))
idx2=int(input("enter index 2:"))

#for swaping list
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)