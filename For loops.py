#Vòng lặp for
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
for i in movies:
    print(i)

#Vòng lặp while 
#Cú pháp sử dụng
#while condition:
    # code
i = 1
while(i <= 10):
    print(i)
    i += 1
#Chúng ta có thể lồng vòng lặp while
i = 1
while(i <= 10):
    j = 1
    while (j <= 10 - i):
        print(j, end = " ")
        j += 1
    print("")
    i += 1
#Các từ khóa trong vòng lặp for break , continue
#break - break giúp chúng ta chấm 
#dứt vòng lặp tại thời điểm nó xuất hiện và các code cùng cấp phía sau nó sẽ không được thực thi nữa.
o = 1

while(i <= 10):
    print(i)
    if 0 == 5 :
        break
    i += 1
# 1
# 2
# 3
# 4
# 5
#continue - giúp chúng ta nhảy qua lần lặp hiện tại và chuyển đến lần lặp tiếp theo, 
# các code cùng cấp phía sau nó cũng sẽ không được thực hiện.
for p in "Thien Bui Dep Trai":
    if p == "n":
        continue
    print(p, end=" ")

# ket qua:
# T h i e   B u i   D e p   T r a i 

