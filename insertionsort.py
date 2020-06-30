#implementation of 
n=int(input("enter any n value"))
li=[]
print("enter {} number of elements".format(n))
for i in range(0,n):
    i=int(input())
    li.append(i)
print("elements before sorting")
print(li[0])
for i in range(0,n-1):
    j=i+1
    while(j>0):
        print("i={} j={}".format(i,j))
        if li[j-1] > li[j]:
            temp=li[j]
            li[j]=li[j-1]
            li[j-1]=temp
        j=j-1
        print(li[i], end=" ")
        print(li[j])
    print(li)
print("After sorting")
print(li)