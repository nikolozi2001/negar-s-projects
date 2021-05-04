subjects = ["phisics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

GradeBook = zip(subjects,grades)
print(list(GradeBook))

#added more subjects

subjects.append("computer science")
grades.append(100)

GradeBook = zip(subjects,grades)
print(list(GradeBook))

grade_book = list(GradeBook)

grade_book.append(["visual arts", 93])
# (7) modify gradebook

grades[4] += 5
print(list(grade_book))

#here starts last semester gradebook

subjects2 = ["ethical hacking", "cyber security", "IoT", "artifical intellect"]