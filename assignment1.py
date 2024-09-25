labs_completed = int(input("Enter the number of labs completed: "))
quizzes_completed = int(input("Enter the number of quizzes completed: "))
assignment_1 = int(input("Enter grade for Assignment 1: "))
assignment_2 = int(input("Enter grade for Assignment 2: "))
assignment_3 = int(input("Enter grade for Assignment 3: "))
assignment_4 = int(input("Enter grade for Assignment 4: "))
midterm_1 = int(input("Enter grade for Midterm 1: "))
midterm_2 = int(input("Enter grade for Midterm 2: "))
final_exam = int(input("Enter grade for Final Exam: "))
mid_and_final_prep = int(input("Enter grade for Midterms and Final Preparation: "))

if labs_completed > 6:
    labs_completed  = 6
if quizzes_completed > 6:
    quizzes_completed = 6
labs_grade = labs_completed / 6 * 100
quizzes_grade = quizzes_completed /6 * 100
grade = (labs_grade * .2 + quizzes_grade * .15 + (assignment_1 + assignment_2 + assignment_3 + assignment_4)/ 4 * .16 + (midterm_1 + midterm_2)/ 2 * .25 + final_exam * .18 + mid_and_final_prep * .06) 
grade = int(round(grade))
print("Your grade is:" , grade)
