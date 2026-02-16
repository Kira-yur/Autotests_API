class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow (self):
        self.age = self.age + 1

    def rename (self, new_name):
        self.name = new_name

    def info (self):
        print("User:", self.name, "Age:", self.age)

user_1 = User("Kirill", 29)
user_1.info()

user_1.grow()
user_1.info()

user_1.rename("Kira")
user_1.info()

user_2 = User("Ничита", 15)
user_2.info()

user_2.grow()
user_2.info()

user_2.rename("Никита")
user_2.info()