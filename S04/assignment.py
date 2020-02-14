answer = input("enter a number: ")
if answer.isdigit():
    print("done")
else:
    print("invalid")

number = int(answer)
if number % 3 == 0:
    print("3K")
elif number % 3 == 1:
    print("3k+1")
elif number % 3 == 2:
    print("3k+2")
