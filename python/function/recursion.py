#recursive function
num = int(input("Enter number:"))
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(num)

#factorial
num = int(input("Enter number:"))
def fact(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * fact(num-1)
    
print(fact(num))