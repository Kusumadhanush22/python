#implementation of selection sort.
#logic for selection sort we need find minimum and place to the left.
n=int(input("enter how many number you want to sort"))
li=[]
print("enter elements to sorts")
for i in range(0,n):
    k=int(input())
    li.append(k)
for i in range(0,n):
    min=li[i]
    for j in range(i+1,n):
        if min >li[j]:
            min=li[j]
            temp=li[i]
            li[i]=li[j]
            li[j]=temp
print(li)