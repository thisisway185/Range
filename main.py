def rangee(x=1, y=10):
    """This program makes the range function more interesting."""
    print("Welcome to the program.")
    answer = True
    while answer:
       x = int(input("\nWrite the first index: "))
       y = int(input("Write the second index: "))
       while x<y:
           x += 1
           print(x)
       answer = input("Do you use rangee again? yes/no: ")
       if answer=="yes" or "y" or "ye" or "yeah":
           continue
       elif answer =="no" or "n" or "not":
           print("Thank you for using our program.")
           answer = False
       else:
            print("No such command was found, the program started from scratch.")
       return x
rangee()
