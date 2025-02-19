# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for ss in a:
#     if ss <  5:
#         print(ss)


# my_float = 1.64
# my_integer = int(my_float) после точкадан кийин баарын алп салат
# my_integer = round(my_float) арифметика мн иштейт

# print (my_integer)

# ee_int = 33 # квартира номер
# nm_int = (ee_int - 1)  // 20 +1  # подиезд номер  
# et_int = (ee_int - 1) % 20 // 4 +1 # этаж номер
# print (nm_int)
# print (et_int)



 

# my_string =  input("My name is")
# my_integer = int( input("My eayr my_list =[1,12,"edf"]
# print(my_list)


# big_int = 2 **1000
# print( len( str( big_int)))

# my_string = "Iskhak"
# print(my_string.upper())  # баарнн чон кылат
# print(my_string.lower())  # баарын кичиене кылат


# my_string = "Hello, world!"
# print(my_string.replace('world' , "Python"))  # replace алмаштырат



# <-------------->
# integer = input("Enter a number :")
# if integer.isdigit():
#     integer = int( integer)
# print(type(integer))   

# my_string = input("Enter a string :")

# if my_string.isdigit():
#       my_integer = int(my_string)
#       print(my_integer)
# else:
#  print(f"{my_string} not a number")



# fruties = ["Iskhak", "Mirlan", "keldibek"]
# print("ikshak"in fruties )
# print("Iskhak"in fruties)
# print(fruties[1])


# fruits = ["Banana", "Apfel","Kivi"]
# fruits.append("Anar")
# print(fruits)


# Name = ["Iskhak", "Mirlan", "Keldibek"]
# Name+ = Name.pop()#pop акыркы созду переменныйга айлантат
# print(Name)
# print(Name+)



# Name = ["Iskhak", "Mirlan", "keldibek"]
# Name+ = ["Batyrov","Burulay"]

# Name.extend(Name+)# extend кошот бири бирине 
# print(Name)

# my_list = [12,312,11,23,123,5,123,2]
# my_list.sort() # sort  сортировка кылат
# print(my_list)


# my_string ="My name is Iskhak"
# my_list = my_string.split(" ") # split бул баарын болуп берет 
# print(my_list)

# my_strings = " ".join(my_list)  # split бул болгондорду кайра чогултуп берет
# print(my_strings) 


# my_list = [1,21,32,12,34,2,112]

# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))

# my_list = [ 1,21,12,34,2,112 ]

# print(my_list[:4]) 

# my_list =[1,12,"edf"]
# print(my_list)


# my_list = True
# my_int = 2 
# my = my_list + my_int
# print(my) 

#<------------------>
# my_sekund = 3681

# minute = my_sekund // 60
# sekund = my_sekund % 60
# hour = minute // 60
# print(minute )
# print(sekund )
# print(hour )

# print(type(minute))
# print(type(sekund))
# print(type(hour))


# my_sekund = input("Сан киргиз")
# my_sekund = int(my_sekund)
# hour = my_sekund // 3600
# minute = (my_sekund % 3600) // 60 
# sekund = ((my_sekund % 3600) % 60)
# print(hour )
# print(minute )
# print(sekund )  



# db_login = "foot"
# db_pass = 1234
# if (db_login=="foot"):
#     print("professional")
# elif (db_pass==1234):
#     print("prof")
# else:
#         print("kk")



# for i in range ( 0, 10 ):
#     if i % 2 == 0:
#         continue
#     print(i)
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1



# b=1
# while b < 10:
#     if b % 2 == 0:
#         b += 1
#         continue
#     print(b)
#     b += 1
# print(b)



#<--------================----------------->
# dict
#set 
#tuple
#list
#<===================---------==============>



# x = 1
# while x < 10:
#     print(x)
#     x = x+1

# a= 10
# b= 11
# s= 12

# if a >b:
#     print(a)
# elif a < b and a >s and a < s:
#     print(a)
# elif b < a and b > s and b < s:
#     print(b)
# else:
#     print(s)

# a = 11
# b = 12
# s = 10 
# if a < b < s or s < b < a :
#     print(b)
# elif b < a < s or s < a < b :
#     print(a)
# else :
#     print(s)

# for i in range(0,10,-2):
#     print(i)


# print('Сан киргиз')

# a = int(input())

# if a >100:
#     print('100 дон чон сан иштеп жатат')
# elif a>50 and a < 100:
#     print('50 дон 100 го чейинки сан иштеп жатат')
# elif a == 100:
#     print('100 го барабар')
# else:
#     print('50 дон кичине сан иштеп жатат  ')





# i = 2
# while i < 10:
#     i = i + 2
#     print(i)


# class game:
#     name = 'Football'
#     age = 153
#     category = 'komand'

#     def start_game(self):
#         print(f'Game {self.age} started')

# s = game()
# s.start_game()


 
# class telefon:
#     name = "Iphone"
#     model = "Iphone 13 pro"
#     color = "Gold"

#     def tel_name(self):
#         print(f'Telefon name: {self.name}')

# t = telefon()
# t.tel_name()



# class person:
#     name = "Iskhak"
#     age = 25
#     country = "kyrgyz"

#     def person_info(self):
#         print(f"Person info:  {self.name}")


# p = person()
# p.person_info()



# class Cars:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# bmw = Cars('bmw M5',100)
# print(f'Cars model:{bmw.name},age is {bmw.age}')



#ООП окуп келуу 


#<Полиморфизм (Polymorphism)>


class Cat:
    def speak(self):
        return "Мяу-мяу!"

class Dog:
    def speak(self):
        return "Гав-гав!"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  



#<Инкапсуляция (Encapsulation)>
class Car:
    def __init__(self, brand, model):
        self.brand = brand       # Публичный атрибут
        self.__model = model     # Приватный атрибут (жашыруун)

    def get_model(self):
        return self.__model      # Приваттык өзгөрмөгө жетүү методу

car = Car("Toyota", "Camry")
print(car.brand)        
print(car.get_model())  

#<Мурастоо (Inheritance)>
class Animal:
    def speak(self):
        return "Дыбыш чыгарат"

class Dog(Animal):  # Мурастоо
    def speak(self):
        return "Гав-гав!"

dog = Dog()
print(dog.speak())  

#<Абстракция (Abstraction)>
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5

