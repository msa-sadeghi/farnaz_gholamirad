numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(len(numbers))
# print(numbers[len(numbers) - 1])
# print("last element is", numbers[-1])

# print(numbers[:3])
# print(numbers[3:6])
# print(numbers[::2])
# x = int(input("enter a number: "))
# numbers.append(x)
# print(numbers)
# numbers.insert(0, x)
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(numbers.count(x))
# numbers.pop()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.index(2))
# new_copy = numbers.copy()
# print(new_copy)

# x = [1,2]
# y = [3,4]

# print(x + y)
# x.extend(y)
# print(x)
# x.append(y)
# print(x)
# numbers = [1,2,3,4,5]
# numbers.remove(3)
# del numbers[-1]
# numbers[0] = -123
# print(numbers)
# numbers = (1,2,3,4,5)

# favorite_foods = {
#     "sara":"pizza",
#     "artin":"burger"
# }

# print("sara likes", favorite_foods["sara"])
# print("artin likes", favorite_foods["artin"])
# favorite_foods["roze"] = "pepperoni"
# del favorite_foods["artin"]

# برنامه ای بنویسید که نام و غذای مورد علاقه
# سه فرد را از کاربر دریافت نماید و در یک دیکشنری ذخیره کند
# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "root" and password == "root":
#     print("welcome")
# else:
#     print(f"{user_name} is not valid")

# age = int(input("enter an age: "))
# if age >= 18:
#     print("ADULT")
# elif 13 <= age < 18:
#     print("TEENAGER")
# elif age < 13 and age >= 9:
#     print("JUNIOR")
# else:
#     print("KID")
# برنامه ای بنویسید که نام و نمرات سه درس سه دانش جو را از کاربر بگیرد
# و نام و معدل هر دانشجو را در دیکشنری اضافه نماید

# for i in range(3):
#     print("hello")
    
# i = 0
# while i < 3:
#     print("hello")
#     i += 1
    
# for number in [1,2,3,4,5]:
#     print(number)
# for ch in "python":
#     print(ch)
    
# با کمک حلقه فور و نیز حلقه وایل برنامه ای بنویسید که پنج عدد از کاربر دریافت نماید
# و سپس حاصلجمع آنها را محاسبه و نماش دهد


# برنامه ای بنویسید که اعداد زوج کوچکتر از 1000 را با هم جمع نماید
# %

# for i in range(100, 2_000_000, 200_000):
#     print(i)
    

# برنامه ای بنویسید که اعداد فرد بین 1000 تا 10000 را درون لیستی ذخیره نماید

numbers = [1,2,3,4,5]
for n in numbers:
    print(n ** 2)
    
for i in range(len(numbers)):
    print(numbers[i] ** 2)