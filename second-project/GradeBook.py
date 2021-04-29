subjects = ["phisics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

GradeBook = zip(subjects,grades)
print(list(GradeBook))

subjects.append("computer science")
grades.append(100)

GradeBook = zip(subjects,grades)
print(list(GradeBook))

GradeBook.append("visual arts", 93)
print(list(GradeBook))