class dog:
    def __init__(self,name , age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name + " says bhau")
    def bark2(self ):
        print(self.name + " namaskar")
    def eat(self):
        print(self.name + " is eating")
dog1 = dog("rambo",10)
dog2 = dog("shadow",5)

dog2.eat()

class cat:
    def __init__(self,name, color):
        self.name= name
        self.color=color

    def meow(self):
        print(self.name + "mewowwwww")

cat1 = cat("mani",2)

cat1.meow()


