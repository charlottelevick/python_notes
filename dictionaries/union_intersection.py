vowels = set()
vowels.add('A')
vowels.update('EIOU')
print(vowels)

#COPY
#example; I have one set right now "Vowels" and I do not want to change anything in that set so,
example_1 = vowels.copy()#copy method to mutate a copy rather than the orginal
print(example_1)
example_1.clear() #removes all elements from the set
print(example_1)

#REMOVE
example_2 = vowels.copy()
example_2.remove('E')#if you try to remove element that doesn't exist = KeyError
print(example_2)

#DISCARD
example_3 = vowels.copy()
example_3.discard('E')#Unlike remove, no KeyError
print(example_3)

#When to use Remove and Discard? Depends if you want the KeyError to occur, e.g. try except block, remove is ideal beacuse you can use KeyError to catch 

#POP 
example_4 = vowels.copy()
vowel = example_4.pop()
print(example_4)
print(vowel)
#assigned return value to a variable
#pop returns a random element everytime

#MEMBERSHIPS - membership testing
vowels = {'A', 'E', 'I', 'O', 'U'}
print('A' in vowels)
print('B' in vowels)
print('C' not in vowels)
print('D' not in vowels)

#RELATIONS
import string 
vowels = {'A', 'E', 'I', 'O', 'U'}
alphabet = set(string.ascii_uppercase)
print(alphabet)

#loop through vowels and conduct a membership test
#if letter in alphabet, set flag to True
#else change to False, break loop

is_related = None 
for letter in vowels:
    if letter in alphabet:
        is_related = True
    else:
        is_related = False
        break
if is_related is True:
    print("It's related!")
    
#vowels.issubset(alphabet) #Result in terminal = True (checking if vowels is a subset of alphabet)
#alphabet.issuperset(vowels) #Result in terminal = True (checking if alphabet is a superset of vowels)
#vowels <= alphabet #Result = True (short form for subset)
#alphabet >= vowels #Result = True (short form for superset)
#alphabet == alphabet #Result = True
#vowels == vowels #Result = True
#vowels == alphabet #Result = False

digits = set(string.digits)
print(digits.isdisjoint(alphabet)) #Result = True

#Euler diagram = subset within a superset
#Use a Venn diagram to compare and contrast the memberships of sets. Each section of the Venn diagram is a subset

#UNION AND INTERSECTION
#UNION
turkey_omlette = {'turkey', 'cheese', 'eggs'}
bacon_omlette = {'eggs', 'mushroom', 'bacon'}
print(turkey_omlette.union(bacon_omlette))
#Result = a list of all ingredients minus duplicates
#if you have lots of other omlettes, you can add them all together e.g. print(turkey_omlette.union(bacon_omlette, cheese_omlette))
#short hand =
all_ingredients = turkey_omlette | bacon_omlette
print(all_ingredients)
#this is the union

#INTERSECTION
#what ingredients are common to all omlettes. These are the intersection to all ingredients for all omlettes
#intersection = middle overlapping point of venn digram

print(turkey_omlette.intersection(bacon_omlette))
#Result = eggs (found in both ingredients)

shared_ingredients = turkey_omlette & bacon_omlette
print(shared_ingredients)