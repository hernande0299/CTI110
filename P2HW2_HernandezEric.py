# CTI-110
# P2HW2 - List
# Eric Hernandez
# 6/11/2023
#
#User inputs grades for 6 different modules/tests
#The program then creates a list of the user's inputed grades
#The list then finds the lowest and highest grades, sum of grades, and the average grade
#The lowest grade, highest grade, sum of grades, and the average grade are then displayed in the program's output

#User inputs their grade for Module 1
print('Enter grade for Module 1:', end=' ')
module_1 = float(input())
#User inputs their grade for Module 2
print('Enter grade for Module 2:', end=' ')
module_2 = float(input())
#User inputs their grade for Module 3
print('Enter grade for Module 3:', end=' ')
module_3 = float(input())
#User inputs their grade for Module 4
print('Enter grade for Module 4:', end=' ')
module_4 = float(input())
#User inputs their grade for Module 5
print('Enter grade for Module 5:', end=' ')
module_5 = float(input())
#User inputs their grade for Module 6
print('Enter grade for Module 6:', end=' ')
module_6 = float(input())
print()
print()
#All user's input of module grades are put into a list
grades = [module_1, module_2, module_3, module_4, module_5, module_6,]

print('------------Results------------')
#Program finds the lowest grade, highest grade, sum of grades, and the average
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / 6
#Program displays the lowest grade from the list
print(f"Lowest Grade:       {lowest_grade}")
#Program displays the highest grade from the list
print(f"Highest Grade:      {highest_grade}")
#Program displays the sum of grades from the list
print(f"Sum of Grades:      {sum_of_grades}")
#Program calculates and displays the average grade from the list
print(f"Average:            {average:.2f}")
print('----------------------------------------')













