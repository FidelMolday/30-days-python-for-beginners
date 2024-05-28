first_name = 'Fidel'
last_name = 'Ouma'
country = 'Kenya'
city = 'Nairobi'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'JS','React', 'Python']
personal_info = {
    'firstname':'Fidel',
    'lastname':'Ouma',  
    'country':'Kenya',
    'city':'Nairobi',
}
print (personal_info,skills,age)

#printing the the values stored in the variables
print('First name:',first_name)
print('First name length:',len(first_name))
print('Last name:',last_name)
print('Last name length:',len(last_name))
print('country:',country)
print('city:',city)
print('Age:',age)
print('Married:','not_married')
print('skills:',skills)
print('Personal information:',personal_info)

#Declaring multiple variablesin one line
first_name,last_name,country,age,is_married = 'Fidel','Ouma','Kenya',20,False

print(first_name,last_name,country,age,is_married)
print('First name:',first_name)
print('Last name:',last_name)
print('Country:',country)
print('Age:',age)
print('Married:',is_married)