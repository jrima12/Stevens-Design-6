a=3
print(a)
print(type(a))
x=2.1
x;type(x)
print(a+x)
print(a-x)
print(a*x)
print(x/a)
print(a**2)
y=2+3j
y;type(y)
print(y.real)
print(y.imag)

s='Hello World!'
print(type(s))
print(s.upper())
print(s.lower())
print(s.strip('!'))
print(s[0])
print(s[6:])
print(s[6:-1])
print(len(s))
b=s.encode()
print(b)
print(type(b))
c=b.decode()
print(c)
print(type(c))
t=' This is a simple program.'
print(s+t)
print('"{:s}" has {:d} characters.'.format(s, len(s)))

veggies=('beet', 'corn', 'kale')
print(type(veggies))
print(len(veggies))
print(veggies[0:2])
print(veggies+('leek', 'okra'))

fruits=['apple', 'banana', 'mango']
print(type(fruits))
print(len(fruits))
print(fruits[0:2])
fruits+['orange', 'papaya']
fruits.append('orange')
print(fruits)
fruits.remove('mango')
print(fruits)
fruits.insert(1, 'mango')
print(fruits)

student={'name': 'Mary', 'id': '8776'}
print(type(student))
print(student['name'])
print(student.items())
print(student.keys())
print(student.values())
students={'1': {'name': 'Alex', 'grade': 3.8}, 
          '2': {'name': 'Barb', 'grade': 2.5}, 
          '3': {'name': 'Dave', 'grade': 4.2},
          '4': {'name': 'John', 'grade': 4.1},
          '5': {'name': 'Mary', 'grade': 3.5}}
print(students.keys())

z=25**5
if z>1000000:
    print('More')
else:
    print('Less')


if not 'major' in student.keys():
    student['major']='ECE'

print(student)

for v in s:
    print(v, end=' ')

i=0
for item in fruits:
    print('Fruit {:d}: {:s}'.format(i, item))
    i=i+1

for key in student:
    print('{:s}: {:s}'.format(key, student[key]))


i=0
while i<=10:
    if i%2==0:
        print(i, end=' ')
    i=i+1



m=1
for n in range(4, 256, 4):
    m=m*n
    if m>512:
        break
    print(m)


grains=['oat', 'rice', 'rye', 'wheat']
for item in grains:
    if item=='rice':
        continue
    else:
        print(item, end=' ')


import math
print(math.ceil(1.5))
print(math.floor(1.5))
print(math.factorial(10))
print(math.fmod(10,3))
print(10%3)
print(math.sqrt(64))
print(math.exp(1))
print(math.log(4,2))
print(math.degrees(1.5707963267948966))
print(math.radians(90))
print(math.asin(1))
print(math.sin(1.5707963267948966))
print(math.cos(math.pi))


r=range(10)
print(r)
print(r[::-1])
print(r[::2])
print(r[1::3])
print(range(10, 110, 10))

def printList(list):
    print('{:d} items on the list:'.format(len(list)))
    for item in list:
        print(item, end=' ')

def averageGrade(dict):
    sum=0.0
    for key in dict:
        sum=sum+dict[key]['grade']
    average=sum/len(dict)
    return average

print(averageGrade(students))

def printID(name, **kwargs):
    print('Student Name: ', name, sep='')
    for key in kwargs:
        print(key, ': ', kwargs[key], sep='')

printID(name='Mary', id='8776', major='ECE')


def printID(name, *varargs):
    print('Student Name:', name)
    for item in varargs:
        print(item)

printID('Barb')
printID('Mary', 'id: 8776', 'major: ECE')
exit()


def printID(name, *varargs):
    print('Student Name:', name)
    for item in varargs:
        print(item)

printID('Barb')
printID('Mary', 'id: 8776', 'major: ECE')
exit()


