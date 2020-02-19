import random

# y = random.randint(1, 5)
# print(y)


# Game Random Number (normal form)
# secret_num = random.randint(1, 100)
#
# while True:
#     guess = int(input("guess the secret number"))
#     if guess > secret_num:
#         print("greater")
#     elif guess < secret_num:
#         print("lesser")
#     else:
#         print("correct :)")
#         break


# Game Random Number (functional form)
secret_num = random.randint(1, 100)
print(secret_num)


def check_num(guess, secret_num):
    if guess > secret_num:
        return 1
    elif guess < secret_num:
        return -1
    else:
        return 0
    # instead of lines above:
    # return 0 if guess == secret_num else 1 if guess > secret_num else -1


def show_msg(compare_result):
    msg = {
        1: "greater",
        -1: "lesser",
        0: "correct :)"
    }
    print(msg[compare_result])


while True:
    guess = int(input("guess the secret number"))
    compare_result = check_num(guess, secret_num)
    show_msg(compare_result)
    if compare_result == 0:
        break
