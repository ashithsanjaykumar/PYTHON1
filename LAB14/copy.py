class point:
    pass
class rectangle:
    def __init__(self,h,w):
        self.h = h
        self.w = w
    def printdata(self,name):
        print(f"{name:8} -> height: {self.h}, width: {self.w}, corner x:{self.coener.x}corner y: {self.corner.y}")
box = rectangle(200,500)
box.corner = point()
box.corner.x = 0
box.corner.x = 0
print("---initial state---")
box.printdata("box")
box = copy.copy(box)
print("\n---after shallow copy(values match)")
box.printdata("box")
