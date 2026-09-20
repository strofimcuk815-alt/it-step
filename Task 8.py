first=int(input("Введіть перше число: "))
second=int(input("Введіть друге число: "))
operation=input("Введіть математичну дію (+, -, *, /): ")
if operation=="+":
    print(first + second)
elif operation=="-":
    print(first - second)
elif operation=="*":
    print(first * second)
elif operation=="/":
    if second==0:
        print("Ділення на нуль")
    else:
        print(first / second)