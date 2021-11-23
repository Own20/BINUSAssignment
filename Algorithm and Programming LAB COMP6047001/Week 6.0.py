# li = ['hello', 'there', 'general', 'torvalds']

# a = 'brand'

# car = {
#     'brand': 'honda',
#     'year': '2010',
#     'color': 'red'
# }

# for i in car:
#     print(car['brand'])
# print(car.keys())
# print(list(car.keys()))
# print(car.values())
# print(car.items())

# car['brand'] = 'toyota'
# print(car)
# car.update({'brand': 'toyota', 'price': '200000000'})
# print(car)

# print(car[a])   #honda
# print(car['brand']) = a
# print(car)

# car[a] = 'xyz'  #get the value of a
# print(car)

# car[li] = 'xyz'
# print(car)      #error

# car[1]: li
# li.append('hi')
# print(car[1])   #add 'hi' to li

# def increment(x):
#     x = x + 1
# x = 0
# increment(x)
# print(x)

# def increment(y):
#     global x
#     x = y + 1
# x = 0
# increment(x)
# print(x)

# def increment(x):
#     return x + 1
# x = 0
# x = increment(x)
# print(x)

# def main():
#     x = 'hello'
#     print(x)
# if __name__ == "__main__":
#     main()
# print(__name__)

# x = 0
# for i in range(10):
#     x = i
#     x = x + i
# print(x)

# def add1(x):
#     x += 1
#     return add1(x)
# print(add1(4))

#1, 2, 3, 5, 8, 13 -> return
#1, 2, 3, 4, 5,  6 -> x
# def fib(x):
#     if(x > 1):
#         return fib(x - 1) + fib(x - 2)
#     else:
#         return 1
# print(fib(6))

di = {
    'greetings': 'hello',
    'salutations': 'Lord',
    'name': 'Ryo'
}
di.keys()
di.values()
di['greetings'] = 'hi'
print(di)
del di['greetings']
print(di)