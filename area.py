class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return (22/ 7) * (self.r ** 2)
    
shapes = [Circle(3), Rectangle(6, 7)]
for s in shapes:
    print(s.area())  

class Team:
    def __init__(self, members):
        self.members = members   # store members in a list

    def __len__(self):
        return len(self.members)  # delegate to list’s len()

# Usage
t = Team(["Alice", "Bob", "Sayan"])
print(len(t))   # 3