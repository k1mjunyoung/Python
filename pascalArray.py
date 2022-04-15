testCaseNum = int(input("3부터 10까지의 정수 중 하나를 입력하세요: "))
list = []

for n in range(testCaseNum):
    list.append([])
    list[n].append(1)

    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])

    if(testCaseNum != 0):
        list[n].append(1)

print(list)