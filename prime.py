num=int(input("enter a number: "))
if num==1:
    print("prime!")
else:
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
        else:
            print("prime")
            break