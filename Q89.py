
#Q8 1st time
def odd_even_counter(number):
    odd = []
    even = []
    for i in range(number+1): # range does not include last index
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return sum(even), sum(odd)

    # use odd_even_count(5) to get 6 and 9

print(odd_even_counter(5)) # calling function and then printing for argument

#Q9 1st time

def find_smallest_interval(numbers):
    if len(numbers) < 2:
        return "too short"
    elif len(numbers) > 100000:
        return "too long"
    else:
        list1=[]
        x=0
        for a in numbers:
            for b in numbers:
                if a != b:
                    list1.append(abs(a-b)) # put into list the absolute diffrences
                    x = min(list1) # from list of differences which is the smallest 
        return x

print(find_smallest_interval([3,50,9,-15,16,20]))