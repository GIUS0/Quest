grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students=list(students)
new_students.sort()
key=new_students[0]
value=sum(grades[0])/len(grades[0])
new_grades={key:value}
print(new_grades)