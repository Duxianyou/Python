try:
    num1 = int(input("First num :"))
    num2 = int(input("second num :"))
except ValueError:
    print("input num error!")
else:
    print(num1 + num2)

