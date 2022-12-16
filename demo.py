name1=input("enetr name1:")
name2=input("enetr name2:")
i=0
while i<len(name1):
    j=0
    while j<len(name2):
       j=j+1
    i=i+1
if i>j:
    print(name1)
elif i<j:
    print(name2)
else:
    print("equal",name1,name2)
