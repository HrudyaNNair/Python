list=[]
n=int(input("Enter the number of elements in the tuple : "))
for i in range(0,n):
    print("Enter element",i+1,":",end=" ")
    list.append(int(input()))
tup=tuple(list)
tup1=()
tup2=()
for i in range (0,n):
    if(tup[i]%2==0):
        tup1+=(tup[i],)
    else:
         tup2+=(tup[i],)
print("Original tuple : ",tup)
print("Even tuple : ",tup1)
print("Odd tuple : ",tup2)
