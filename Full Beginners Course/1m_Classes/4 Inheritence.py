# Don't Repeat Yourself(DRY)
class Mammal:
    def walk(self):
        print("walk")


# class Dog:
#     def walk(self):
#         print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")


# class Cat:
#     def walk(self):
#         print("walk")
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()
