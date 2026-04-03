"""
Dictionary

collection - key+value = pair = data1

left - side -= key
right-side = value

{key1:value1, key2:value2, key3:value3}

add 
update
delete
view
exit

#create a dictionary 
student = {
    'Paras': 100,
    'Gopal': 200,
}
#Accessing a element
print(student['paras']) #100

#update a element
student['paras'] = 150

#to delete 
#del student['paras']
#print(student)

"""


#Initialising dictionary
student_grade = { }

#Add a new student
def add_student(name,grade):
    student_grade[name] = grade

    print(f"Added {name} with a {grade}")

#Update a student grade
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade

        print(f"{name} with marks are update {grade}")

    else:
        print(f"{name} is not found!")

#Delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]

        print(f"{name} has been deleted")

    else:
        print(f"{name} is not found!")

#View all students
def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")

        else:
            print("NO students found!")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break   

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


