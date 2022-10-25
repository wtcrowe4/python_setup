def hello():
    print("Hello user, welcome to my world.")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty, I need food.")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f'First I ate {list[i]}')
            else: 
                print(f'Next I ate {list[i]}')



print('---------------------------------')
print('My hello function:')
hello()
print('---------------------------------')
print('My pack function:')
print(pack(1, 2, 3))
print(pack('clothes', 'toothbrush', 'razor'))
print('---------------------------------')
print('My eat_lunch function:')
eat_lunch([])
eat_lunch(['sandwich'])
eat_lunch(['sandwich', 'apple', 'chips'])
print('---------------------------------')