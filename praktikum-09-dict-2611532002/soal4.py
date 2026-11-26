all_students = input("Class list: ").split()
submitted_list = input("Submitted: ").split()

submitted = set(submitted_list)
not_submitted = set(all_students) - submitted

print("Submitted:", len(submitted), "students")
print("Not submitted:", len(not_submitted), "students")
for num in all_students:
    if num not in submitted:
        print(num)