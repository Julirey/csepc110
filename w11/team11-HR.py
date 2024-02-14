
with open('Team Project\hr_system.txt') as line:
    for i in line:
        parts = i.split(' ')
        paycheck = float(parts[3]) / 24
        if parts[2] == 'Engineer':
            paycheck += 1000
        print(f'Name: {parts[0]} (ID: {parts[1]}), Title: {parts[2]} - ${paycheck:.2f}')