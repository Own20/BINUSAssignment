#%%
def myPow(base=3,exponent=2):
    return base**exponent

myPow(10)    #base=10,exponent=2
myPow(3,0.5) #base=3,exponent=0.5
myPow(base=3) #base=3,exponent=2
myPow() #base=3,exponent=2
myPow(exponent=4) #base=3,exponent=4
myPow(exponent=5,base=10)
#%%
def square(x):
    return x*x

square(x=10)

y = 5
square(x=y)
#%%

print("bye","hi",end=" ",sep="#")
print("bye","hi",sep=" ",end="#")

#%%
def f0(x):
    def g0(y):
        return y**3+3
    return g0(x)**4+4

f0(4)
#%%
weight = 160
#getter or accessor functions
def changeWt(weight):
    return weight - 10

weight = changeWt(weight)
print(weight)

#%%
weight = 160   #global

def changeWt(weight):#local, pass by value
    #whatever gets in, does not get out
    weight = weight - 10
    print("weight is now",weight)
    
changeWt(weight)
print(weight)
#%%
def getWtHt():
    weight = float(input("Enter weight in kg:"))
    height = float(input("Enter height in cm:"))
    return weight, height

weight,height = getWtHt()

print(weight,",",height)

#%%
def calc_q2(x):
    q = 4 * x + 1
    print(q)
    
q = calc_q2(5)
print("q is",q)
#%%
"""
create a function called divmod that accepts
2 parameters x and y and returns the 
quotient and remainder of x and y
"""
def divmod(x,y):
    return x//y,x%y

a,b = divmod(10,5)

print(a,b)   # a = 2, b = 0
#%%
#declaration (place to create functions)
#mutator or setter functions
def greetings():    #void function, no parameters
    print("Hello")
    print("Goodbye")

def greetMe(name): #void function, with 1 parameter
    print("Hello",name)
    
def addMe(x,y):
    sum = x + y
    print("Sum of",x,"and",y,"is",sum)
    
def myPow(base,exp):
    return base ** exp
  
    # f(n) = 3 * n
    # f(3) = 3 * 3 = 9
#invocation (place to execute functions)
    
v = myPow(2,3)
print(v)

print(myPow(3,3))

greetings()
print("End")
greetMe("Tartaglia")
myStr = "Childe"
greetMe(myStr)
addMe(2,4.5)
a = 5
b = 10
addMe(a,b)
x = 2
y = 4
addMe(x,y)

w = addMe(a,x)
print(w)


#main() function - used as a driver
#%%
"""
Functions
    0. User defined and Pre-defined
    1. Declaration
        def <functionName>([<parameters>]):
            <body>
    2. Invocation
    3. Important concepts:
        #local - refers to an identifer defined within a 
        function or block
        #scope of local identifiers - can be used from point 
        of declaration to end of the block

        #global - refers to an identifer defined outside a 
        function or block
        #scope of global identifiers - can be used in any function 
        or block as long as there isn't a local variable with 
        the same name
    4. Void and Non-Void Functions
    5. Parameters and Parameter passing (by value, by reference)
    ...
"""
#%%