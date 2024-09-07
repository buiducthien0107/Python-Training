#Khai báo biến
#cú pháp | tenBien = giaTribien
name = "Bui Duc Thien"
age = 22 
male = True
#Khai báo biến 1 dòng theo thứ tự 
name1 , age1 , male1 = "Trieu Tu Long", 27 , True

print(name)
print(age)
print(male)
print(name1)
print(age1)
print(male1)
#Kiểm tra dữ liệu bằng type 
print(type(name)) #string
print(type(age)) #int
print(type(male)) #bool
#Ép kiểu dữ liệu 
famale = int(True)
print(type(famale))
age2 = 55 
floatAge = float(age2)
print(type(floatAge))