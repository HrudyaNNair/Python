books={'Sapiens':100,'Divergent':150,'Insurgent':200}
print("Books :",books)
newbook=input("Enter the book to add: ")
n=int(input("Enter the number of stocks: "))
books.update({newbook:n})
print("Updated Books :",books)
x=input("Enter the book to delete : ")
element=books.pop(x)
print("Newly Updated Books :",books)
