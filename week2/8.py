''' Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	'''
class Animal:
    def speak(self):
        print('All animals are speachless but actionfull!!')
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat says meow")

cat=Cat()
cat.speak()

dog=Dog()
dog.speak()