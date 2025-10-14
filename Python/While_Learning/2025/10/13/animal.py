class Animal:
    def __init__(self, name):
        self.name = name
        self.iss_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):#对于有共性的类，可以继承自一个父类来缩短代码
    def speak(self):
        print("Woof")

class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("MouseMiky")

print(dog.name)
print(dog.eat())
print(dog.sleep())
print(dog.speak())