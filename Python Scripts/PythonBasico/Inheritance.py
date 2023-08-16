
class Mammal: 
     def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def miar(self):
        print("miar")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1= Cat()
cat1.miar()
