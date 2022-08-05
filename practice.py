# method - function
# syntax is def user_name():

def user_name():
    user_prompt = True
    while user_prompt:
        name = input("please enter your name" + " ")
        if name.isalpha():
            user_prompt = False
        else:
            print("make sure youre only using letters")
    print(f"welcome {name}")

user_name()

# Data collections
# dictionaries can have all typs of data collections

# Dictionaries

shopping_items = {
    "eggs":1.85,
    "bread":1.50,
    "peppers":0.90
}
# print only values
print(shopping_items.values())
print(sum(shopping_items.values()))
print(shopping_items)


# multiple options in tuples yes
# diff between list and tuples - lists are mutable vs tuples which are immutable

# list syntax []  tuples ()  dict {}


a= list(range(1,100)) # print a will give list of 1>100
print(sum(a)) # sum of everything in that range

print(4 % 2)

#for n in range(1,100): # use modulo operator to see if something is a mupltiple of #another
  #  if n % 2 ==0:
      #  print ("even")
    #else:
       # print ("odd")

def numbers():
    count=0
    for n in range(1,100):
        if n % 2 ==0:
            print("even")
        else:
            total1 =count + n
            print(total1)

print(numbers())


# control flow
list =["dog","cat","fox" ,"cow", "pig"]
for item in list:
    if item == "cat":
        print("found mitty")
    elif item == "dog":
        print("woof")
    else:
        print("not pets")


# bill ={5:4} - this is a dictionary

# correct supr index is
    # super().__init__()
    pass