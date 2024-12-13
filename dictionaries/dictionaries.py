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