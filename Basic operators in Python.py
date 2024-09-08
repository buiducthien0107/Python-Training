#Toán tử số học - Arithmetic Operators
a = 5 
b = 4
print(a+b)#toán +
print(a-b)#Toán -
print(a/b)#Toán /
print(a*b)#Toán *
print(a%b)#Chia lấy phần dư
print(a**b)#Toán tử mũ. a**b = ab
print(a//b)#toán làm tròn
#Toán tử quan hệ - Comparison (Relational) Operators
print(a==b)#So sánh giá trị 
print(a!=b)# 2 giá trị khác nhau thì trả về True , ngược lại thì false
print(a<b)#Bên a nhỏ hơn b thì true , ngược lại thì false
print(a>b)#Bên a lớn hơn b thì true , ngược lại thì false
print(a<=b)#Bên a bé hơn hoặc b thì true , ngược lại thì false
print(a>=b)#Bên a lớn hơn hoặc b thì true , ngược lại thì false
#Toán tử gán - Assignment Operators.
c = a #c=5
c +=a # c = c +a
c -=a # c = c-a
c*=a # c = c*a
c/=a # c = c/a
print(c)
# Toán tử logic.
# and , or , not
d = True
e = False
logic = d and e 
print(logic)# 2 giá trị True thì kết quả True , 1 trong 2 giá trị False thì là False
logic_one = d or e
print(logic_one)#True 1 trong 2 giá trị True thì kết quả True 
f = True
logic_two = not f
print(logic_two)#False đảo nghịch giá trị , f = True thì sẽ đảo nghịch thành False
#Toán tử biwter
print(a & b)
print(a|b)
print(a^b)
print(-a)
print(a<<a)
print(a>>b)
#Toán Tử khai thác.
m = 3
n= [4, 3, 2, 1]
print(m in n )
print(m not in n)
#Toán tử xác thực.
l = 3
k = 4 
print(l ==k)#Toán tử này sẽ trả về True nếu l == k và ngược lại
print(l !=k)#Toán tử này sẽ trả về True nếu l != k và ngược lại
#Thứ tự các phé so sánh nhân nhân chia trước cộng trừ sau 
g = 5+ 4 < 3*2
print(g)#False