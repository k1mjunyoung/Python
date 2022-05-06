def average(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

result = average(10,20,30,40,50)

print(result)

