course = {"teacher":"Ashley", "title":"introducing dictionaries", "level":"beginner"}
print(course["teacher"])
#Result = Ashley

course = {"teacher":"Ashley", "title":"introducing dictionaries", "level":"beginner"}
print(course.keys())
print(course.values())
print(sorted(course.keys()))
print(sorted(course.values()))
#Result = dict_keys(['teacher', 'title', 'level'])
#dict_values(['Ashley', 'introducing dictionaries', 'beginner'])
#['level', 'teacher', 'title']
#['Ashley', 'beginner', 'introducing dictionaries']

course = {"teacher":"Ashley", "title":"introducing dictionaries", "level":"beginner"}
course["teacher"] = "Treasure"
course["level"] = "intermediate"
print(course.values())
course["stages"] = "2"
print(course)
#Result = dict_values(['Treasure', 'introducing dictionaries', 'intermediate'])
#{'teacher: 'Treasure', 'title': 'introducing dictionaries', 'level': 'intermediate', 'stages': '2'}
del(course['stages'])
print(course)
#Result = {'teacher: 'Treasure', 'title': 'introducing dictionaries', 'level': 'intermediate'}

#Iterate over dictionaries 
course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}
for key, value in course.items():
    print(key)
    print(value)
#Result = 
#teacher
#Ashley
#title
#Introducing Dictionaries
#level
#Beginner

#Before packing
def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
print_teacher(name='Ashley', job= 'Instructor', topic= 'Python')

#After packing
def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')
print_teacher(name='Ashley', job='Instructor', topic= 'Python')
#Result = name: Ashley
#job: Instructor
#topic: Python

teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print_teacher(**teacher)
    
#CLEANING DATA
data = [
    {
        "email": "we@afi.co",
        "name": "Warren Bates",
        "date_joined": "4/20/2048",
        "admin": "False",
        "id": "36"
    },
    {
        "email": "koz@ma.cf",
        "name": "Edgar Howell",
        "date_joined": "2/2/2022",
        "admin": "False",
        "id": "40"
    },
    {
        "email": "li@kifal.vi",
        "name": "Benjamin Newman",
        "date_joined": "6/12/2090",
        "admin": "False",
        "id": "17"
    },
    {
        "email": "unauli@suiju.gw",
        "name": "Ray Greer",
        "date_joined": "9/15/2022",
        "admin": "False",
        "id": "71"
    },
    {
        "email": "vi@cipu.io",
        "name": "Ina Goodman",
        "date_joined": "1/19/2052",
        "admin": "False",
        "id": "8"
    },
    {
        "email": "bannoj@jik.hm",
        "name": "Irene Larson",
        "date_joined": "10/16/2053",
        "admin": "False",
        "id": "73"
    },
    {
        "email": "kaf@wun.nr",
        "name": "Florence Olson",
        "date_joined": "8/27/2031",
        "admin": "False",
        "id": "89"
    },
    {
        "email": "imuahezu@ga.fo",
        "name": "Madge Edwards",
        "date_joined": "9/10/2117",
        "admin": "False",
        "id": "35"
    },
    {
        "email": "tagap@ulti.fm",
        "name": "Lola Griffin",
        "date_joined": "4/20/2023",
        "admin": "False",
        "id": "27"
    },
    {
        "email": "ku@oku.mg",
        "name": "Bryan Tate",
        "date_joined": "6/1/2036",
        "admin": "False",
        "id": "98"
    },
]

#from data import data

#INSTRUCTIONS
#1)Split the full name into two fields, first name and last name
#2)Convert the admin field to a boolean value
#3)Convert the id to an integer
#4)Keep the rest of the info the same
#5)Complete this in a function(s)
#6)Save the data into a new data structure: a list of dictionaries

def clean_data(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["email"] = user["email"]
        fixed["first_name"] = user["name"].split(" ")[0]
        fixed["last_name"] = user["name"].split(" ")[1]
        fixed["date_joined"] = user["date_joined"]
        if user["admin"] == "True":
            fixed["admin"] = True
        else:
            fixed["admin"] = False
            fixed["id"] = int(user["id"])
            cleaned.append(fixed)
    return cleaned
    
print(clean_data(data))