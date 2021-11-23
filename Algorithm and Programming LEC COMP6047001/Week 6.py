"""
list [], Tuple (), String "" or '', Dictionary {}
When to use a list - if you have a collection of data that may need to be adjusted
When to use a tuple - if you know data should not be changed
When to use a dictionary - if you want to store associated data
    Dictionary is great for associative relationships
    Made up of a key and value pair (<key:value>)
    Needs key - immutable type - unique
    Value can be mutable
Usable functions: items(), keys(), values(), sorted(), get()
    got get() - if the key exists, it returns it
              - if the key does not exist, it creates it, then returns it
"""
from _typeshed import SupportsTrunc

# define a dictionary
myDict1 = {}
myDict2 = dict()

# populate data
myDict3 = {'school': 'Binus', 42: 'myAge', (3, 4): {'first':33, 'second':3+4}, 5.7: [5, 0.7]}
print(myDict3[(3, 4)])
print(myDict3[5.7])
print(myDict3)

myDict1['name'] = 'Rizky'
myDict1['age'] = 18
myDict1['height'] = 165
print(myDict1)

myDict2[0] = 3.5
myDict2[1.5] = 100
myDict3['hi'] = 'bye'
print(myDict2)

myProfile = {'name': 'Arvin', 'age': 18, 'height': 160}
for data in myProfile:                              #not clear for the reader what it does
    print(data)
print()

for key in myProfile.keys():                        #get and print keys (clearer accessing the keys)
    print(key)
print()

for v in myProfile.keys():                          #get and print values
    print(v)
print()

# \t = tab
for kv in myProfile.keys():                         #get key and values pair and display it
    print(kv, ':\t', myProfile[kv], sep="")
print()

for key,value in myProfile.items():                 #get key value by useing items()
    print(key, ":\t", value, sep="")
print()

"""
for key,value in myProfile.items():
    print(key, "\t", ': ', value, sep="")
print()
"""
students = {'Dimas': 'B+', 'Alysha': 'A-', 'Arvin': 'A', 'Jess': 'B', 'Maria': 'C', 'Steph': 'D', 'Richie': 'F'}
for key in students:
    print("{:2} {}".format(students[key], key))
print()

for key in sorted(students):                        #sort according to value
    print("{:2} {}".format(students[key], key))

myProfile1 = {'name': 'Arvin', 'age': 18, 'height': 160}
for key in ['name', 'age', 'height']:
    print(key, ':\t', myProfile1.get(key), sep="")   #get key value pair using get()

myProfile2 = {'name': 'Arvin', 'height': 160}
for key in ['name', 'age', 'height']:
    print(key, ':\t', myProfile2.get(key,0), sep="")

myProfile3 = {}
for key in ['name', 'age', 'height']:
    print(key, ':\t', myProfile3.get(key,0), sep="")