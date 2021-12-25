from line1 import Line1
from line2 import Line2
from line3 import Line3
def rangee(x=1, y=10):
    """This program makes the range function more interesting."""
    print("Welcome to the program.")
    answer = True
    while answer:
        answer = input("\nDo you use default rangee? yes/no or mods \n>>>")
        if answer=="yes":
           Line1.line1()
        elif answer =="no":
           print("Thank you for using our program.")
           answer = False
        elif answer == "mods" or "Mods":
            ans = input("Switch to single line mode(L) or switch to single line mode without spaces?(Lws): ")
            if ans == "l" or "L":
               Line2.line2() 
            elif ans == "lws" or "Lws":
               Line3.line3()
        else:
            print("No such command was found, the program started from scratch.")

rangee()
