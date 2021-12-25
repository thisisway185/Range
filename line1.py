class Line1:
    def __init__(self, te):
        self.te1 = te

    def line1():
        final1 = True
        while final1:
            x = int(input("\nWrite the first index: "))
            x -= 1
            y = int(input("Write the second index: "))
            while x<y:
                x += 1
                print(x)
                if x==y:
                    final1 = False
                elif x<y:
                    continue