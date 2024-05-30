grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students=list(students)
new_students.sort()
key1=new_students[0]
value1=sum(grades[0])/len(grades[0])
key2=new_students[1]
value2=sum(grades[1])/len(grades[1])
key3=new_students[2]
value3=sum(grades[2])/len(grades[2])
key4=new_students[3]
value4=sum(grades[3])/len(grades[3])
key5=new_students[4]
value5=sum(grades[4])/len(grades[4])
new_grades={key1:value1,key2:value2,key3:value3,key4:value4,key5:value5}
print(new_grades)
