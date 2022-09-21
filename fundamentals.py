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
    print('hello satinder')

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

# def find_treasure(arg1):
#     if(arg1 == 'treasure'):
#         return True
#     else:
#         return False

# treasure_array = ['treasure','Not treasure','treasure','Not treasure']
# for treas in treasure_array:
#     is_treas = find_treasure(treas)
#     if(is_treas):
#         print('there is a treasure')
#     else:
#         print('No treasure')

def find_treasure(treasure_array):
    for treasures in treasure_array:
        if(treasures == 'treasure'):
            print('There is a treasure')
            return True

    print('No Treasure')
    return False


treasure_array = ['man treasure','treasure']
find_treasure(treasure_array)

treasure_array = ['No treasure','yes treasure']
find_treasure(treasure_array)
