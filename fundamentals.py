number= 50
string='hello! world!!'
boolean= True
array_string = ['Javascript','SQL','Mariadb','Python']
array_num = [22,44,66,88]
for word in array_string:
    print('This is one of the language ,',word)
for num in array_num:
    if( num > 50):
        print( 'Look at this number',num)

def static_greeting():
    print('satinder')

def dynamic_greeting(name):
    print('hello',name)

print(number)
print(string)
print(boolean)
if(number>10):
    print('That is larger than 10')
else:
    print('That is NOT larger than 10')

dynamic_greeting('family')
dynamic_greeting('class')

if(number <= -1 and boolean == True):
    print('Negative and true')
elif(number>=0 and boolean == False):
    print('Positive and False')
elif(number>100 or boolean == True):
    print('Large and True')
else:
    print("I don't know")

static_greeting()
dynamic_greeting('simran')