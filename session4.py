from colorama import Back as b, Style as st
from student_data import all_students
message = f"""{b.CYAN}Welcome,{st.RESET_ALL}
      {b.LIGHTBLACK_EX}To EXIT               ->  0,{st.RESET_ALL}
      TO ADD new student    ->  1,
      To View All Students  ->  2,
      TO UPDATE a student   ->  3,
      TO DELETE a student   ->  4,
      """
print(message)
running = True
while running:
    user_input = input("> ")
    if user_input == "0":
        print("See You Again")
        running = False
    elif user_input == "1":
        last_students_ids = len(all_students) + 1
        student = {}
        print("you are registering new student...")
        name = input("enter student's name: ")
        age = int(input("enter student's age: "))
        grade = input("enter student's Grade: ")
        degree = input("enter student's degree: ")
        student['id'] = last_students_ids
        student['name'] = name
        student['age'] = age
        student['grade'] = grade
        student['degree'] = degree
        all_students.append(student)
    elif user_input == "2":
        print(all_students)