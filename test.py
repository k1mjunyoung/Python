try:
    age = int(input('Enter your age : '))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print