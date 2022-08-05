# indexing practice

index = ["one","two",3,4,5]
        #    0   1    2 3 4

print(index[4]) # will print 5
index[1] = 2 # changes value "two" to number 2
print(index)

index.append("car")
print(index)
index.remove("car")
print(index)

greeting ="hello friends" # quotations arent in index
        #  01234567891111
print(len(greeting))

print(greeting[-7]) # value 7 going from left to right
print(greeting[4])

#print only hello using slicing
# if we leave out the start index the range will start at the first character
# get characters from start to position 4(not included)
print(greeting[:4])

#by leaving out the end index - range will go to the end
#get the characters from position 2 all the way to the end
print(greeting[2:])

# get the characters from position 2 to position 5(not included)
print(greeting[2:5])

# use negative indexes to start the slice from the end of the string

print(greeting[-2:]) # position -2 (not incldued) till the end
print(greeting[:-5]) # get from start to position -5 (inc)



print(greeting.strip()) #returns without whitespaces

