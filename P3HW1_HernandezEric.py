# CTI-110
# P3HW1 - Debugging
# Eric Hernandez
# 6/18/2023

# User inputs grades for 6 different modules/tests
# The program then creates a list of the user's inputed grades
# The list then finds the lowest and highest grades, sum of grades, and the average grade
# The lowest grade, highest grade, sum of grades, and the average grade are then displayed in the program's output
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print('------------Results------------')
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / 6
# Program displays lowest grade from list
print(f"Lowest Grade:       {low}")
# Program displays highest grade from list
print(f"Highest Grade:      {high}")
# Program displays sum of grades from list
print(f"Sum of Grades:      {sum_of_grades}")
# Program calculates and displays the average grade from the list
print(f"Average:            {average:.2f}")
print('----------------------------------------')




# determine letter grade for average
# Displays letter grade average below the results

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
        print('Your grade is: B')
elif average >= 70:
        print('Your grade is: C')
elif average >=60:
        print('Your grade is: D')
else:
    if average <=50:
        print('Your grade is: F')








