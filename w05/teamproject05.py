print()
grade_percent = float(input('What is the grade percent? '))
if grade_percent >= 90 :
    grade = 'A'
elif grade_percent >= 80 :
    grade = 'B'
elif grade_percent >= 70 :
    grade = 'C'
elif grade_percent >= 60 :
    grade = 'D'
else : 
    grade = 'F'

if grade_percent % 10 >= 7 :
    sign = '+'
elif grade_percent % 10 < 3 :
    sign = '-'
else :
    sign = ''

if grade == 'A' and sign == '+':
    sign = ''
elif grade == 'F' :
    sign = ''

print()
print(f'The grade is {grade}{sign}.')
print()