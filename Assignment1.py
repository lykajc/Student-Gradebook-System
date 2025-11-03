
gradebook = {'Lyka': 98, 'Jasmine': 97, 'Samantha': 96, 'Red': 95, 'Jester': 94}

print('\n----------Student Gradebook System----------')

print('Student Gradebook:')
for student, grade in gradebook.items():
    print(f"{student} -> {grade}")

print()

find_name = input ('Search student name:')
if find_name in gradebook:
    print(f"{find_name}'s grade is: {gradebook[find_name]}")
else:
    print('Student not found.')
    print("\n")

update_stud = input('\nEnter student name to update:')
if update_stud in gradebook:
    prev_grade = gradebook[update_stud]
    new_grade = int(input(f"Enter new record for {update_stud}:"))
    print(f"Updating the grade of: {update_stud} -> {prev_grade} to {new_grade} ")
    gradebook[update_stud] = new_grade
else:
    print('Student not found.')

print('\nUpdated Gradebook:')
for student, grade in gradebook.items():
    print(f"{student} -> {grade}")

Top_student = None
highest_grade = -1

for student, grade in gradebook.items():
    if grade > highest_grade:
        highest_grade = grade
        Top_student = student
print(f"\nTop Student: {Top_student} with the grade of {highest_grade}")

