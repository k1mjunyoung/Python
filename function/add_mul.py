def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    else:
        print("Error!!!")

    return result

result = add_mul("mul", 1, 2, 3, 4, 5)
print(result)

