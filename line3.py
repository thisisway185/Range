class Line3:
    def __init__(self, te):
        self.te3 = te

    def line3():
        final3 = True
        while final3:
            x = int(input("\nWrite the first index: "))
            x -= 1
            y = int(input("Write the second index: "))
            while x<y:
                x += 1
                print (x, end="")
                if x==y:
                    final3 = False
                elif x<y:
                    continue