# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# s = 0
# for row in matrix:
#     for col in row:
#         if col % 2 == 0:
#             s += col
        
# print(s)
# s = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0:
#             s += matrix[i][j]
# print(s)
       
# names = [
#     [["ali", 19.1], ["artin", 12.5], ["armin", 19.8], ["arman", 10.3]],
#     [["sara", 11], ["samin", 14], ["arezo", 19.9], ["yasaman", 9]],
# ]


# g_s = names[0][0][1]
# g_n = names[0][0][0]

# for gender in names:
#     for student in gender:
#         if student[1] > g_s:
#             g_s = student[1]
#             g_n = student[0]
# print(f"greatest score is: {g_s} and his/her name is {g_n}")





# boy's average   vs    girl's average

# boys_ave = 0
# girls_ave = 0
# for boy in names[0]:
#     boys_ave += boy[1]
    
# boys_ave = boys_ave / len(names[0])
# for girl in names[1]:
#     girls_ave += girl[1]
    
# girls_ave = girls_ave / len(names[1])
    
# if boys_ave > girls_ave:
#     print("boys")
# else:
#     print("girls")




       
# x = (1,2)
# print(type(x))
# for number in x:
#     print(number)

# set

# x = {1,2,3}
# print(type(x))
# x.add(7)
# print(x)
# # x.remove(2)
# print(x)
# y = {8,9,1}
# print(x.union(y))
# print(x.intersection(y))

# x = [1,2,3,4,5,6,7,8,9,12,3,4,56,7,8,9]
# y = set(x)
# print(y)
# print(len(y))


# پیاده سازی سیستم ثبت نام دانشگاه
# با استفاده از حلقه، لیست، دیکشنری







