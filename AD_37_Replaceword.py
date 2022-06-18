a=input("Enter the sentence : ")
old=input("Enter word to be replaced : ")
new=input("Enter the new word : ")
words=a.split()
r=""
for i in words:
    if(i==old):
        r=r+" "+new
    else:
        r=r+" "+i
print(r)
