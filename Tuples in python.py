name = ('Thien','Tu','Gia Thien','Cuong','Phuong')
#tuples không thể bị thay đổi khi chúng ta định nghĩa chúng
age = () #tuples rỗng
#Truy cập đến từng phần tử của tuples 
print(name[1])
print(name[-1])
#Vì không thể thêm được giá trị nên ta dùng toán tử  + để nói 2 tuples lại với nhau 
name_one = ('Tai','Kiet','Tri' , name)
synthetic = name + name_one
print(synthetic) #('Thien', 'Tu', 'Gia Thien', 'Cuong', 'Phuong', 'Tai', 'Kiet', 'Tri')
print(name_one[3][0])
#tuples và list 
#Chúng ta được cho một danh sách 3 bộ phim cùng với ngày ra mắt
# sử dụng tuples không thôi thì sẽ in ra tên của bộ phim mà không ra ngày 
# sử dụng list và tuples sẽ in ra giá trị của cụm tuples
movies = [
    ('Bố Gìa', 25),
    ('Làm Gìau với Ma', 26),
    ('Anh try say bai', 27)
]
print(movies[0])
print(movies[0][0])
#exercies 
#Hàm input và lưu trữ kết quả tuples
name_movie = (input("nhập tên bộ phim :"))
day_movie = (input("nhập ngày sản xuất :"))
money_movie =(input("nhập số tiền kiếm được"))
movie_mavel = (name_movie ,day_movie,money_movie)
print(movie_mavel)
print(f"name movie {movies[0]} ,day movie{movies[1]}")