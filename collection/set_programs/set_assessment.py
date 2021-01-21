students=["name1","name2", "name3", "name4"]
student=set(students)
fail=["name1","name2"]
failed_student=set(fail)
pass_student=student.difference(failed_student)
print((pass_student))
print("passed students :",list(pass_student))