class Hello:
    def __init__(self):
        self.name = 'Mayank'
        self.__age = 29
    def __get_age(self):
        return self.__age
    def now_get_age(self):
        return self.__get_age()
hello = Hello()
print(hello.now_get_age())