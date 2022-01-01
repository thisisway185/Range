from line1 import Line1
from line2 import Line2
from line3 import Line3
def rangee(x=1, y=10):
    """This program makes the range function more interesting."""
    print("Welcome to the program.")
    answer = True
    while answer:
         answ = input("\nDo you use default rangee? yes/mods or exit \n>>>")
         if answ=="exit":
            print("Thank you for using our program.")
            answer = False
         elif answ=="yes":
            Line1.line1()
         elif answ == "mods":
            ans = input("Switch to single line mode(L) or switch to single line mode without spaces?(Lws): ")
            if ans == "L":
               Line2.line2() 
               continue
            elif ans == "Lws":
               Line3.line3()
               continue
         else:
            print("No such command was found, the program started from scratch.")