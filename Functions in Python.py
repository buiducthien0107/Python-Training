#Bổ sung chức năng range()
for i in range(10):
    print(i)
for t in range(3,10):
    print(t)
#Functions trong python
#def ten_ham(param...):
    #code

def say():
    print("Tôi năm nay 22 tuổi")
say()
def sum(a,b):
    print("sum = " + str(a+b))
sum(5,6)
#Hàm có kết quả trả về
def sumb(d,e):
    return d +e 
c = sumb(4,6)
print("Tổng = " + str(c))
#Phạm vi của biến trong hàm
def say_hello():
    g = "Hello"
    print(g)

#print(g)
# Lỗi: name 'a' is not defined