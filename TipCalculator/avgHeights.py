# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0 
for height in student_heights:
  total += height

count = 0 
for x in student_heights:
  count += 1
#cannot use len() or sum()
print(round(total/count))
# lets use += 

