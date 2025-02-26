print('hello, world!')
print(len('hello, world!'))
print(type('hello, world!'))
print(str('hello, world!'))
print(int('12'))
print(float('12'))

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

print(min(20,30,40,200))
print(max(20,30,40,200))
print(min([20,30,40,200]))
print(max([20,30,40,200]))
print(sum([20,30,40,200]))

first_name = 'Santiago'
last_name = 'Mendoza López'
country = 'Mexico'
city = 'Aguascalientes'
age = 18
is_married = False
skills = ['PseInt', 'Python']
person_info = {
   'firstname':'Santiago',
   'lastname':'Mendoza López',
   'country':'Mexico',
   'city':'Aguascalientes'
   }

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Santiago', 'Mendoza López', 'Mexico', 18, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)