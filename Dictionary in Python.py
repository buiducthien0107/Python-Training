#Dictionary(dict) sử dụng  {} 
#Cấu trúc cơ bản của dic key : value1 , value2 , value3
person = {
'name': 'Bui Duc Thien',
'age' : 22,
'male' : True
}
print(person['name'])
#Thay đổi giá trị của dict 
person['male'] = False
print(person['male']) #False

del person['male']
print(person) #{'name': 'Bui Duc Thien', 'age': 22}
#dict lồng nhau
person_one = {
'name': 'Bui Duc Thien',
'age' : 22,
'male' : True, 
'option' :{
           'favorite' : 'play game',
           'game': 'pubg',
           'time play game' : 6
}
}
print(person_one['option']['game'])
#Cập nhật từ điển (dict)
person["game"] = 'pubg'
print(person)
#update từ điển (dict)
person.update(person_one)
print(person)
#Xóa một giá trị trong từ điển (dict)
del person['male']
print(person)
#Lặp lại qua các từ điển 
for attribute in person:
    print(attribute)
#name
#age
#game
#option
#exercises
music = { 
    'musica' :  'The Dark Side of the Moon' ,
    'name' :'Pink Floyd',
    'year' : 1973,
    'musica_one' : {"Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"}

}
for i in music:
    print(i)

for key, value in music.items():
    print(f"{key}:{value}")