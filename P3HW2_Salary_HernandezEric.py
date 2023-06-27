# CTI-110
# P3HW2 - Salary
# Eric Hernandez
# June 22 2023
#

# User inputs employee's name, hours worked, and pay rate
# Program evalutes employee's information to include overtime
# Program displays employee's name, pay rate, hours worked, overtime hours/pay, pay for regular hours, and gross pay

# User inputs employee's name
print('Enter employee\'s name:', end=' ')
employee_name = input()

# User inputs employee's number of hours worked
hours_worked = float(input('Enter number of hours worked: '))

# User inputs employee's pay rate
pay_rate = float(input('Enter employee\'s pay rate: '))

# Evaluates if employee has worked overtime(more than 40 hours)
if hours_worked <= 40:
    overtime_pay = 0
elif hours_worked > 40:
    over_time = hours_worked - 40
    overtime_pay = ((hours_worked - 40)* pay_rate * 1.5)

# Calculate amount employee should be paid for regular hours worked

reg_pay = (hours_worked - over_time) * pay_rate

# Calculate gross pay
gross_pay = reg_pay + overtime_pay
    


print('-------------------------------')

# Program display employee's name
print('Employee name:', ' ',employee_name)
print("")


# Program displays output

print("Hours Worked     Pay Rate      OverTime       OverTime  Pay           RegHour  Pay        Gross Pay")
print('-------------------------------------------------------------------------------------------------------')
print(f'{hours_worked}             {pay_rate}           {over_time}           ${overtime_pay:.2f}                 ${reg_pay:.2f}              ${gross_pay:.2f}')
