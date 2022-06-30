f  = open("file.txt", "r")
a=f.read()
b=a.split(",")
num=[]
for i in b:
    if(i!='\n'):
        num.append(int(i))
print(num)
prime=[]
flag=0
for i in num:
    if (i > 1):
        for j in range(2,i):
            if (i%j == 0):
                flag=1
        if(flag==0):
            prime.append(i)
        flag=0
print("prime numbers = ",prime)
