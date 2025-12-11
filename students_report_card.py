print("--------------STUDENT REPORT CARD--------------")
student_name=input("Enter student name: ")
student_class=int(input("Enter student's class: "))

subject1_name=input("Enter name of subject 1: ")
subject1_marks=int(input(f"Enter marks obtained in {subject1_name}: "))

subject2_name=input("Enter name of subject 2: ")
subject2_marks=int(input(f"Enter marks obtained in {subject2_name}: "))

subject3_name=input("Enter name of subject 3: ")
subject3_marks=int(input(f"Enter marks obtained in {subject3_name}: "))

total_marks=subject1_marks + subject2_marks + subject3_marks
percentage=(total_marks/300)*100  

print("--------------REPORT CARD--------------")
print("Student Name:", student_name)  
print("Class:", student_class)
print(f"{subject1_name}: {subject1_marks} marks")
print(f"{subject2_name}: {subject2_marks} marks")
print(f"{subject3_name}: {subject3_marks} marks")
print()
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print()
if percentage >= 90:
    grade = 'A'
elif percentage >= 75:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'D'
print("Grade:", grade)
print("Status: Passed" if grade != 'D' else "Status: Failed")