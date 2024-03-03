class Addition:
    @staticmethod
    def static_method(x,y):
        return x+y

p1 = Addition()
print(p1.static_method(2,3))
print(Addition.static_method(10,3))