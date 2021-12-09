# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)
hei = 0
for s_height in student_heights:
  hei += s_height  
print(hei)

num_student = 0
for student in student_heights:
  num_student+= 1
print(num_student)

print(round(hei/num_student))