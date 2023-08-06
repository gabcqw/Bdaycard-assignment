# with open("example.log") as f:
#     logs = f.readlines()

# warning_logs = [log for log in logs if "WARNING" in log]

# print(len(warning_logs))
# print(len(warning_logs) / len(logs))

# warning_logs = []

# with open("example.log") as f:
#     for log in f:
#         if "WARNING" in log:
#             warning_logs.append(log)

# print(len(warning_logs))
# print(warning_logs)


def func(num):
    if num == 23:
        return 123
    else:
        print("End of the function")
        return 451


# def gen_func():
#     print("First run")
#     yield 1
#     print("Second run")
#     yield 2
#     print("Third run")
#     yield 3

# for element in gen_func():
#     print(element)
#     input("Input something: ")

# genartor_obj = gen_func()
# for element in genartor_obj:
#     print(element)
#     break

# print("\nBetween loops.\n")

# for element in genartor_obj:
#     print(element)

# import random


# def gen_random_letter():
#     letters = list("abcdefghijklmnopqrstuv")
#     for _ in range(5):
#         yield random.choice(letters)


# for letter in gen_random_letter():
#     print(letter)
