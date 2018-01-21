students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for i in students:
    print i['first_name'], i['last_name']

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for i in users:
    print i
    if i == 'Students':
        count = 0
        for i in users['Students']:
            count = count + 1
            length = len(i['first_name']) + len(i['last_name'])
            print count,"-", i['first_name'], i['last_name'],"-", length
    else:
        count = 0
        for i in users['Instructors']:
            count = count + 1
            length = len(i['first_name']) + len(i['last_name'])
            print count,"-", i['first_name'], i['last_name'],"-", length



    
