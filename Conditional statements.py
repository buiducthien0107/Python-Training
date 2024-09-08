#Câu lệnh có điều kiện
#nếu điều kiện này đúng thì thực hiện khối lệnh A, nếu sai thì thực hiện khối lệnh B
#các điều kiện trả về giá trị 
#khác 0 hoặc bằng True thì coi là đúng và trả về 0, None hoặc False thì coi là sai.
#Câu lệnh if-else
#if condition: 
    #code
#else:
    #code
a = 99
if(a==100):
    print("Tôi được 100 điểm")
else:
    print("Bạn chỉ được 99 điểm")
#Câu lệnh if-elif-else
#if condition:
    # code
#elif condition2:
    # code
#elif condition3:
    # code
#else:
    #code
#Gỉai quyết một bài toán tính điểm học sinh trung bình khá giỏi 
b = 4
if (b >=8):
    print("bạn được học sinh giỏi")
elif(b>=6.5 and b<=8):
    print("Bạn học sinh khá")
else:
    print("Bạn học sinh Trung bình")