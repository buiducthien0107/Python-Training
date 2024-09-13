#map
def mutiply(x):
    return x*x
result = map(mutiply,[1 , 2 , 3 , 4 , 5])
print(list(result))

result_t = map(lambda x, y: x + " " + y, ['red', 'blue'], ['green', 'black'])

print(list(result_t))  # ['red green', 'blue black']
#filter
# cú pháp filter(function, iterable)
#Những số chia hết cho 2
result = filter(lambda x : x /2, [1, 2, 3,4,5,6])
print(list(result))
