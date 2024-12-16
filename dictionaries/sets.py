none_set = {None}
print(none_set)

twos = {'two', 2, 2.22, ('dos', 'Spainish')}
print(twos)

booleans = {True, False}
print(booleans)

challenge = {4.0, 4, 5.0, 5}
print(challenge)

#1) unordered collections
#2) sets have unique elements
#Behaviours of sets - remove duplicates from itself

empty_set = {}
print(empty_set)
print(type(empty_set))
#Result = dict not se. So instead try this...

empty_set = set()
print(empty_set)
print(type(empty_set))

sentence = "My favourite data type is the string"
letters = set (sentence)
print(letters)
print(len(letters) < len(sentence))

numbers = [3, 2, 1, 3, 2, 1, 2, 2, 2, 2, 3, 1, 1]
print(set(numbers))
#Result = removes all duplicates and prints in random order

numbers = [3, 2, 1, 3, 2, 2, 2, 2, 3]
numbers = set(numbers)
numbers = sorted(numbers)
print(numbers)
#Result = removes duplicates and numbers in order from 1 - 3

#add(element) = Add one element to a set
#update(iterable) = Add many elements to a set

vowels = set()
vowels.add('A')
print(vowels)
#Results = {'A'}
vowels.update('EIOU')
print(vowels)
#Results = {'U', 'I', 'A', 'E', 'O'}
#Add and Update are two ways of adding elements into a set

#There are four methods that remove an element from a set
#clear() - remove all elements from a set
#remove() - remove an element from a set; it must be a member. If the element is not a member, raise a KeyError
#discard() - same as remove() but does not raise an KeyError
#pop() - remove and return an arbitrary set element. Raises KeyError if the set is empty
