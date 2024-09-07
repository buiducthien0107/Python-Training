#Kiểu dữ liệu
print(type(1))#int
print(type(1.25))#float
print(type("Thien Bui"))#str
print(type(True))#bool

#Tên biến không có nghĩa là x | tên được đặt chuẩn nghĩa nhất như myName
x = 5 
print(x)
print(type(x))
#Tên không hợp lệ 
#1st_value : không được phép vì nó bắt đầu bằng một con số.
#given-name : chứa ký tự gạch nối không hợp lệ.
#john's_age : không được phép vì có dấu nháy đơn.
#example variable : bao gồm một khoảng trắng, điều này cũng không được phép.
_a = 45
myName = "Bui Duc Thien"
print(_a)
print(myName)

name = str(input("nhập tên của bạn vào đây : "))
print(name)
print(type(name))
age = int(input("nhập tuổi của bạn : "))
print(age)
print(type(age))
#Tham chiếu các biến
hours = 40 
hourly_wage = 20.00
print("tiền lương của bạn là :",hours*hourly_wage,"vnd")
#Toán tử cơ bản |: + - * / 
