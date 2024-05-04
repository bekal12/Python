#1
z = input("ente")
i = "hello"
print(i,z)
x = 1 + (0 * 10) * 3 / 8 ** 1
print(x)

#
my_tuple = (1,2,3,4)
my_set = {1,2,3,4}


print(my_tuple == my_set)
# 2.

while True: 
    print("True") 
    break 
    print("Break") 
    break 
    print("False") 

# 3.    
x = 0
while x < 10:
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big")

# 4
print(1 > 3 or 2 > 1)
x = 3 
print(x) 
while True: 
    x = x - 1 
    if x == 1: 
        continue 
    elif x == 0: 
        print("END") 
        break 
    else: 
        print(x)         