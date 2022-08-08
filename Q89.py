
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


   # numbers.sort()
    #return numbers[1]-numbers[0]

print(find_smallest_interval([1,6,4,-8,2]))