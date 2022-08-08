
#Q5 1st time
def find_largest(numbers):
    return max(numbers)

print(find_largest([0,5,8,66,777,454])) # i added numbers here as thats the input requried

#Q6 1st time
def is_twin(a, b):
    word1 = a
    word2= b
    if word1.sort() == word2.sort() and (a,b) != None:
        return True
    else:
        return False

a="silent"
b="listen"
print(is_twin(a,b))


#Q7 1st time

def password(text):
    if len(text) < 5:
        return "Your password is too short"
    elif len(text) > 20:
        return "Your password is too long and may be forgotten"
    else:
        return "Your password is an acceptable length"

print(password("gkg")) # i added string here because thats the input
print(password("gkgyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
print(password("gkgyyyy"))