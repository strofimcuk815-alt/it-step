mark=int(input("Введіть оцінку: "))
if mark >= 0 and mark < 50:
    print("Незадовільно")
elif mark >= 50 and mark < 70:
    print("Задовільно")
elif mark >= 70 and mark < 90:
    print("Добре")
elif mark >= 90 and mark <= 100:
    print("Відмінно")