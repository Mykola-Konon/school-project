# # operator "and"
# a = True
# b = True

# if a and b is True:
#     print("True")
# else:
#     print("False")

# #operator "or"
# a = True
# b = False

# if a or b is True:
#     print("True")
# else:
#     print("False")

# operator "not"(!=)
# a = "Alisa"

# if type(a) != str():
#    print("True")
# else:
#     print("False")

# # Conditions(Умови) if, elif, else
# age = int(input("Enter your age: "))

# if age > 18: #
#     print("you can enter")
# elif age == 18:
#     print("You are 18 yers old")
# else:
#     print("Sorry...")

# x = 1

# while x <= 5:
#     print("Hello")
# #     x += 1

# mssege = "Tell somesing"
# loop = True

# while loop:
#     command = input(massege)
#     if command == "quit":
#         loop = False
#     else:
#         print(command)

# цикл while
# while True:
#     fruits = input("Give me a fruit: ")
#     if fruits == "quit":
#         break
#     else:
#         print(f"Yes I love this {fruits.title}!")

# continue - для повернення на початок циклу
# num = 0

# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)

#цикл for syntax(for _ in ___ )
# fruits = ["apple", "orange", "banana"]

# for fruit in fruits:
#     print(fruit)

# list_tuple = [(1, 2), (3, 4), (5, 6)]

# for I, n in list_tuple:
#     print(I, n)

# for letter in "Alisa":
#     print(letter)

# #randge(1, 10, 1) - (початок діапазону, кінець діапазону, крок перебору) тільки для int
# for n in range(1, 10):
#     print(n)

# #break
# tasks = ["run", "sign", "stop", "pool"]
# for task in tasks:
#     if task == "stop":
#         break
#     print(task)

# #continue
# tasks = ["run", "sign", "stop", "pool"]
# for task in tasks:
#     if task == "stop":
#         continue
    # print(task)



while True:
    x = int(input("Your number x: "))
    y = int(input("Your number y: "))
    
    try:
        res = x / y
        print(res)
        break

    except ZeroDivisionError:
        print(f"ZeroDivisionError: division by zero")
        
    finally:
        print("puk")
        
