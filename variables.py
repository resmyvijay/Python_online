# Variables in Python

first_name = 'Resmy'
last_name = 'Vijay'
country = 'India'
city = 'Chennai'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'ML', 'Python']

person_info = {
    'firstname':'Resmy', 
    'lastname':'Vijay', 
    'country':'India',
    'city':'Chennai'
    }

# Printing the values stored in the variables

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

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Resmy', 'Vijay', 'Chennai', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
