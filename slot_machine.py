import random
from colorama import Fore, Style
import time
import subprocess
Money = float(75000)

def reset_console():
  subprocess.call('clear', shell=True)
reset_console()
symbol = ["☹︎","☹︎","☹︎","☹︎","☹︎","☃︎","☃︎","☃︎","☃︎","⛷︎","⛷︎","⛷︎","☆","☆","7"]
def slot():
    
    print("          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("      ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("      ⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀")
    print("      ⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇      ⣤⣄")
    print("      ⢸⣿⠀⢸⣿ ⣿⡇⢸⣿ ⣿⡇⢸⣿ ⣿⡇     ⠛⠛")
    print("      ⢸⣿⠀⢸",Fore.YELLOW + a + Style.RESET_ALL,"⡇⢸",Fore.YELLOW + b + Style.RESET_ALL,"⡇⢸",Fore.YELLOW + c + Style.RESET_ALL,"⡇    ⣷⣷")
    print("      ⢸⣿⠀⢸⣿ ⣿⡇⢸⣿ ⣿⡇⢸⣿ ⣿⡇   ⣾⡇")
    print("      ⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇  ⣿⡿")
    print("      ⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁ ⠃⠃")
    print("    ⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⡀⡀")
    print("    ⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡀")
    print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀")
    print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉")
    print("    ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉")
while True:
    while True:
        print("College funds : $",Fore.GREEN + str(Money) + Style.RESET_ALL)
        gamble = float(input("How much money do you want to gamble?"))
        if gamble <= Money:
            break
        else:
            reset_console()
            print("Please Retry")
        

        
    for i in range(0,13):
        
        reset_console()
        a = symbol[random.randint(0,14)]
        b = symbol[random.randint(0,14)]
        c = symbol[random.randint(0,14)]
        slot()
        time.sleep(0.13)
    time.sleep(1.5)
    if a == "☹︎" and b == "☹︎" and c == "☹︎":
        print("You won ",gamble*2.5)
        Money += gamble*1.5
    if a == "☃︎" and b == "☃︎" and c == "☃︎":
        print("You won ",gamble*3)
        Money += gamble*3
    if a == "⛷︎" and b == "⛷︎" and c == "⛷︎":
        print("You won ",gamble*7)
        Money += gamble*7
    if a == "☆" and b == "☆" and c == "☆":
        print("You won ",gamble*10)
        Money += gamble*10
    if a == "7" and b == "7" and c == "7":
        print("You won ",gamble*21)
        Money += gamble*21
    else:
        Money -= gamble
