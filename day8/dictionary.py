student ={'name':'Fidel','age':20,'course':['Math','CompSci']}
print(student['course'])
print(student['name'])
print(student['age'])

#adding keys not found in the dictionary
student['phone'] = '555-5556'
print(student.get('phone','Not found'))

#Update
student = {'name' : 'Fidel','age' : 25, 'curse':['Math','CompSci']}
student.update({'name':'Passionate','age':19,'phone':'555-5556'})
print(student)  #{'name': 'Passionate', 'age': 19, 'curse': ['Math', 'CompSci'], 'phone': '555-5556'}

#check the number of keys in our dictionary 
print(len(student))

print(student.keys()) #dict_key(['name','age','curse'])

print(student.items()) #dict_items([('name','John'), ('age',29), ('course',['Math','CompSci])])
