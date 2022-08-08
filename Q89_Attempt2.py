

# Q8
def odd_even_counter(num):
    odd = []
    even = []
    for e in range(num + 1):
        if e % 2 == 0:
            even.append(e)
        else:
            odd.append(e)
    return sum(even), sum (odd)

print(odd_even_counter(5))


# Q9