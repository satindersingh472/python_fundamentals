number= 50
string='hello! world!!'
boolean= True
print(number)
print(string)
print(boolean)
if(number>10):
    print('That is larger than 10')
else:
    print('That is NOT larger than 10')

if(number <= -1 and boolean == True):
    print('Negative and true')
elif(number>=0 and boolean == False):
    print('Positive and False')
elif(number>100 or boolean == True):
    print('Large and True')
else:
    print("I don't know")