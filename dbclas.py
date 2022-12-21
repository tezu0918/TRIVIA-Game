from Database import General, Sport, Maths
from colorama import Fore

class final():
    def app(self):
        print(Fore.LIGHTBLUE_EX + '\n\t\t\t\U0001f600~~~~~~~WELCOME TO TRIVIA GAME~~~~~~~\U0001f600\n' + Fore.RESET)
        request = input(Fore.LIGHTMAGENTA_EX + '\n\t\t\t \t DO YOU WANT PLAY THE GAME (yes/no): '+Fore.RESET)
        while True:
            if request == "yes":
                print(Fore.LIGHTCYAN_EX + '\t\t\t********************************************\n' + Fore.RESET)

                user = int(input(Fore.LIGHTBLUE_EX + "\t\t\t\t\t\U0001f600CHOOSE YOU WANT TO PLAY\U0001f600\n\n" + Fore.RESET +
                    Fore.LIGHTMAGENTA_EX + '\t\t\t\t\t  FOR GENERAL KNOWLEDGE PRESS "1"\n\n' + Fore.RESET +
                    Fore.LIGHTYELLOW_EX + '\t\t\t\t\t  FOR SPORT QUESTIONS PRESS "2"\n\n' + Fore.RESET +
                    Fore.LIGHTRED_EX + '\t\t\t\t \t  FOR MATHS QUESTIONS PRESS "3"\n' + Fore.RESET +
                    Fore.LIGHTCYAN_EX + '\t\t\t********************************************* \n' + Fore.RESET+
                    Fore.LIGHTCYAN_EX + 'Click here: ' + Fore.RESET))
                if user == 1:
                    obc = General()
                    obc.run_general()

                elif user == 2:
                    obc = Sport()
                    obc.run_sport()

                elif user == 3:
                    obc = Maths()
                    obc.run_maths()
                else:
                    print(Fore.LIGHTRED_EX + " PLEASE ENTER CORRECT CATEGORY NUMNBER" + Fore.RESET)

                # user = input("do you want to play? (yes/no):")
                if user == 'yes':
                    continue
                else:
                    break
            print(Fore.LIGHTRED_EX + " GOOD BY THANK YOU" + Fore.RESET)
            exit(0)
            print(Fore.LIGHTRED_EX + " GOOD BY THANK YOU" + Fore.RESET)
