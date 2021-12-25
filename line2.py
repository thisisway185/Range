class Line2:
    def __init__(self, te):
        self.te2 = te
        
    def line2():
        final2 = True
        while final2:
            x = int(input("\nWrite the first index: "))
            x -= 1
            y = int(input("Write the second index: "))
            while x<y:
                x += 1
                print (x, end=" ")
                if x==y:
                    final2 = False
                elif x<y:
                    continue