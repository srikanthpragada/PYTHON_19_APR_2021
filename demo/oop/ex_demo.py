
try:
    num = int(input("Enter a number :"))
    v = 100 / num
    print(num)
except ValueError as ex:
    print("Sorry! Invalid Number!")
    print(ex)
except ZeroDivisionError:
    print("Sorry! Zero is not valid!")

print("The End")