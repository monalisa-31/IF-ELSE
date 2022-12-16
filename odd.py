# import math
# Test=int(input("enter a number"))
# print(math.log2(Test))

import math
Test=int(input("enter"))
for i in range(Test):
    N=int(input("enter any number"))
    A=int(input("enter any number"))
    B=int(input("enter any number"))
    total=math.log2(N)
    print(int(total*A+(total-1)*B))