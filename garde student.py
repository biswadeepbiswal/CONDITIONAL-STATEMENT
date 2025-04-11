# grade syudent based on mark

# marks >= 90 , grade  = "A"
# 90 > marks >= 80 , grade = "b"
# 80 > marks >= 70 , grade = "c'
# 70 > marks, grade = "d"


marks = int(input("enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"

print("Grade of the student is:", grade)


