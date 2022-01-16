import time
import random

li = []

for i in range(6000):
    li.append(random.randrange(100000000))


# def timeWrapper(funct):
#     def wrapper(*arg, **kw):
#         start = time.time()
#         result = funct(*arg, **kw)
#         end = time.time()
#         return result, end-start
#     return wrapper





def selectionSort(li):
    start = time.time()
    li2 = []
    counter = 0
    li2 = list(li)
    for i in range(len(li)):
        smallest = i
        for j in range(len(li2) - i - 1):
            if li2[smallest] > li2[j+1]:
                smallest = j+1
        
        li2.insert(counter, li2[smallest])
        counter += 1
        del li2[smallest+1]
    end = time.time()
    result = end - start
    print(f'selection sort : {result}')
    return li2
    




def insertionSort(li):
    start = time.time()
    li2 = list(li)
    currentIndex = 0
    for i in range(len(li2) - 1):
        currentIndex = i + 1
        while True:
            if currentIndex == 0:
                break
            if li2[currentIndex] >= li2[currentIndex - 1]:
                break

            li2.insert(currentIndex-1, li2[currentIndex])
            del li2[currentIndex+1]
            currentIndex -= 1
    end = time.time()
    result = end - start
    print(f'insertion sort : {result}')
    return li2






def bubbleSort(li):
    start = time.time()
    li2 = list(li)
    for i in range(len(li2)):
        for j in range(len(li2)-1):
            #compare li2[j] and li2[j+1]
            if li2[j] > li2[j+1]:
                li2.insert(j, li2[j+1])
                del li2[j+2]
    end = time.time()
    result = end - start
    print(f'bubble sort : {result}')
    return li2






li2 = selectionSort(li)
# print(li2)
li2 = bubbleSort(li)
# print(li2)
li2 = insertionSort(li)
# print(li2)