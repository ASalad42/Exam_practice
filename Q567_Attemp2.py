# Q5

def find_largest(numbers):
    return max(numbers)
print(find_largest([1,7,88,999,1250]))

# Q6

def is_twin(a,b):
    if sorted(a.lower()) == sorted(b.lower()) and a and b != 0:
        return True
    else:
        return False
a= "listen"
b= "silent"

print(is_twin(a,b))

# Q7

def password(word):
    if len(word) < 5:
        return "Your password is too short"
    elif len(word) > 20:
        return "Your password is too long and may be forgotten"
    else:
        return "Your password is an acceptable length"

print(password("wewe"))
print(password("wewytytytytytytytytytye"))
print(password("wewhhe"))