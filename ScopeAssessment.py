__author__ = 'Mica'

rainbowColors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
for i in range (7):
    print rainbowColors[i]

def foo(x):
    x = x
    global y
    y = x * x

for i in range (7):
    print i
    foo(i)
    for j in range (i):
        print '***'
    print y

class IceCream(object):
    def __init__(self, flavor):
        self.flavor = flavor

favoriteFlavor = "chocolate"
scoop1 = IceCream("vanilla")
scoop2 = IceCream(favoriteFlavor)