first=input("Введите первое число: ")
print(first)
second=input("Введите второе число: ")
print(second)
third=input("Введите третье число: ")
if first==second and second==third and first==third:
    print (3)
elif first==second or first==third or second==third:
    print(2)
elif first!=second or second!=third:
    print(1)


