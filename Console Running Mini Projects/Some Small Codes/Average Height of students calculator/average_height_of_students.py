student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# to get the sum ( sum of heights) of all the numbers in the list
total = 0
for i in student_heights:
    total+=i

# to get the length (number of students) of the student_heights list
count=0
for j in student_heights:
    count=count+1

average = round(total/count)
print(average)
