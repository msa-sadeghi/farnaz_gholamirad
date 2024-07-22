# from colorama import Back as b, Style as st
# from student_data import all_students
# message = f"""{b.CYAN}Welcome,{st.RESET_ALL}
#       {b.LIGHTBLACK_EX}To EXIT               ->  0,{st.RESET_ALL}
#       TO ADD new student    ->  1,
#       To View All Students  ->  2,
#       TO UPDATE a student   ->  3,
#       TO DELETE a student   ->  4,
#       """
# print(message)
# running = True
# while running:
#     user_input = input("> ")
#     if user_input == "0":
#         print("See You Again")
#         running = False
#     elif user_input == "1":
#         last_students_ids = len(all_students) + 1
#         student = {}
#         print("you are registering new student...")
#         name = input("enter student's name: ")
#         age = int(input("enter student's age: "))
#         grade = input("enter student's Grade: ")
#         degree = input("enter student's degree: ")
#         student['id'] = last_students_ids
#         student['name'] = name
#         student['age'] = age
#         student['grade'] = grade
#         student['degree'] = degree
#         all_students.append(student)
#     elif user_input == "2":
#         print(all_students)
#     elif user_input == "3":
#         print("you are in edit page...")
#         user_id = int(input("enter user id:> "))
        
#         print("which item to edit? ")
#         user_choice = input(":> ")
#         x = all_students[user_id - 1].get(user_choice)
#         if x != None:
#             print(f"what do you want to put instead of {x}")
#             new_value = input(":> ")
#             all_students[user_id - 1][user_choice] = new_value
                    
#     elif user_input == "4":
#         print("you are in delete page...")
#         user_id = int(input("enter user id:> "))        
#         print(f"you are deleting {all_students[user_id - 1]['name']} are you aure?(y or n)")
#         if input(":> ") == "y":
#             del all_students[user_id - 1]
        
                
                
                
# about function