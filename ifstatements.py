#get input from user
gender = input('gender? ')
if gender == 'male' or 'gender' == 'Male':
    print('your cat is male')
else: 
    print('your cat is female')

age = int(input('age of your kitty? '))
if age < 5:
    print('your kitty is young')
else: 
    print('your cat is adult')
