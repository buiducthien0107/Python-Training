#Định nghĩa list bằng []
name = ["Thien","Tu","Gia Thien","Cuong","Phuong"]
#Có thể định nghĩa xuống dòng như sau :
name_one = ["Thien",
            "Tu",
            "Gia Thien"
            ,"Cuong",
            "Phuong"]
#Không nhất thiết chỉ có số nguyên hoặc chuỗi 
friend_details = ["Gia Thien", 21 , "boostrap"]
# list số nguyên , tập thói quen có một dấu cách sau dấu phẩy 
number = [21, 22, 23, 24, 25]
print(name)
print(name_one)
print(friend_details)
print(number)
#Ta có thể truy cập giá trị của từng phần tử trong list
print(name[1]) #Tu
print(name_one[2]) #Gia Thien
#Cộng thêm 1 phần tử 
name = name + ["Thi"]
print(name)
#Từ trái qua phải mình sẽ tính là 0 1 2 ... ngược lại phải qua trái -1 -2 -3
print(name[-2])
print(name.pop(5))
#Thêm các giá trị mới
number.insert(25,26) #[21, 22, 23, 24, 25, 26]
print(number)
name.append("Huy")
print(name) #['Thien', 'Tu', 'Gia Thien', 'Cuong', 'Phuong', 'Huy']
#Xóa phần tử khỏi list 
name.remove("Huy")
print(name)# ['Thien', 'Tu', 'Gia Thien', 'Cuong', 'Phuong']
#del có thể xóa bất kì phần tử hay List
del name[-1]
print(name) #['Thien', 'Tu', 'Gia Thien', 'Cuong']
#Pop sẽ xóa phần tử cuối cùng của List và lưu trữ vào biến 
name_pop = name.pop()
print(name)
print(name_pop) #Cuong