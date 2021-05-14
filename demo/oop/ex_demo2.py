
try:
    num = int(input("Enter a number :"))
    v = 100 / num
    print(num)
except ValueError as ex:
    print("Sorry! Invalid Input!")
finally:
    print("Over")


print("The End")
