#function definition
def calc_sum(a, b): #parameter
    return a + b
sum = calc_sum(1234, 2345) #function call; arguments
print(sum)

#without parameter and return value
def intro():
    print("Hello")

output = intro()
intro()
intro()
intro()
print(output) # it doesn't have return value so, it shows none.

#average of 3 number
def calc_avg(a, b, c):
    sum = (a + b + c)
    avg = sum / 3
    print(avg)
    return avg

calc_avg(23, 45, 65)

#Default parameter
def cal_prod(a=5, b=3):
    print(a * b)
    return a * b

cal_prod()

