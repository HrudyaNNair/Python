file1 = open("H.txt","w")
X=input("Enter the String :")
file1.write(X)
file1 = open("H.txt","r")
f=file1.read()
a=""
W=0
words=f.split()
for word in words:
    W=W+1
    a=a+word
U=0
L=0
S=0
T=0
for j in a:
    if j.isupper():
        U=U+1
    elif j.islower():
        L=L+1
    else:
        S=S+1
        if j=='.':
            T=T+1
        
print("The number of Words :" +(str(W)))
print("The number of Upper case letters :"+(str(U)))
print("The number of lower case letters :"+(str(L)))
print("The number of special characters :"+(str(S)))
print("The number of sentences :"+(str(T)))
