li = []

while True:
    print("Please input what you want to do:")
    print("push 1 to add new user")
    print("push 2 to edit a user")
    print("push 3 to delet a user")
    print('push 9 to print all users')
    inpt = input("Please push your choice :")
	
    if(inpt == '9'):
        for i in li:
            print(i)
    elif(inpt == '1'):
        name = input('Please input the name :')
        age = input('please input the age :')
        job = input('please input the job :')
        li.append({'name':name, 'age':age, 'job':job})
    elif(inpt == '2'):
        name = input('Please input the name you want to edit :')
        notFound = True
        for i in li:
            if(i['name'] == name):
                i['name'] = input('Please input the new name :')
                i['age'] = input('please input the new age :')
                i['job'] = input('please input the new job :')	
                notFound = False		
        if(notFound):
            print("User not found")
    elif(inpt == '3'):
        name = input('Please input the name you want to delete :')
        notFound = True
        for i in range(len(li)):
            print(i)
            if(li[i]['name'] == name):
                del li[i]
                notFound = False
                break
        if(notFound):
            print('User not found')