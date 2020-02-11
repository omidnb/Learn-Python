if True:
    print("Hello")
print("outside of if-block")

num = 100
if num % 2 == 0:
    print("even")
if num % 2 != 0:
    print("odd")

cond = num % 2 == 0
if cond:
    print(":)))")
else:
    print(":(((")

answer = input("enter a number: ")
if answer.isdigit():
    num = int(answer)
    if num % 3 == 0:
        print("3K")
    elif num % 3 == 1:
        print("3k+1")
    elif num % 3 == 2:
        print("3k+2")
else:
    print("invalid")
