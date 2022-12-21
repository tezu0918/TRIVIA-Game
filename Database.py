from colorama import Fore

from utility import *

class General(Datas):
    def __abs__(self):
        super().__init__()

    def run_general(self):

        X = 'SELECT Question,A,B,C,D ,Answer FROM dbo.Generals'
        self.cursor.execute(X)
        score = 0
        for i in self.cursor:
            print(i[0])
            print("A", i[1], "\n", "B", i[2], "\n", "C", i[3], "\n", "D", i[4])
            print(Fore.RED + "The  Choose letter should be Capital" + Fore.RESET)
            Answer = input(Fore.LIGHTYELLOW_EX + "Choose the best  answer:" + Fore.RESET)
            if Answer == i[5]:
                score += 1
                print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
            else:
                print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
        print("yor final score is :", score, "/5")

        PersonID = int(input("\33[1m\33[34m\t\t Enter your id number\33[0m"))
        FirstName = input("\33[1m\33[34m\t\t Enter your firstname\33[0m ")
        LastName = input("\33[1m\33[34m\t\t Enter your lastname\33[0m ")
        Result = score
        self.cursor.execute("INSERT INTO Datas (PersonID, FirstName,  LastName, score ) VALUES (?, ?, ?, ?)",
                            (PersonID, FirstName, LastName, Result))
        self.join.commit()


class Sport(General):

    def run_sport(self):

        Y = 'SELECT Question,A,B,C,D,Answer FROM dbo.Sports'
        self.cursor.execute(Y)
        score = 0
        for i in self.cursor:
            print(i[0])
            print(i[1], "\n", i[2], "\n", i[3], "\n", i[4])
            print(Fore.RED + "The  Choose letter should be Capital letter" + Fore.RESET)

            Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
            if Answer == i[5]:
                score += 1
                print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
            else:
                print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
        print("yor final score is :", score, "/7")

        PersonID = int(input("\33[1m\33[34m\t\t Enter your id number\33[0m"))
        FirstName = input("\33[1m\33[34m\t\t Enter your firstname\33[0m ")
        LastName = input("\33[1m\33[34m\t\t Enter your lastname\33[0m ")
        Result = score
        self.cursor.execute("INSERT INTO Datas (PersonID, FirstName,  LastName, score ) VALUES (?, ?, ?, ?)",
                            (PersonID, FirstName, LastName, Result))
        self.join.commit()


class Maths(General):
    def run_maths(self):

        Z = 'SELECT Q_number,Question,Answer FROM Funny'
        self.cursor.execute(Z)
        score = 0
        for i in self.cursor:
            # print(i[0])
            print(i[0], i[1])
            print(Fore.RED + "The answer should be start with capital letter" + Fore.RESET)
            Answer = input(Fore.LIGHTYELLOW_EX + "Enter Short answer:" + Fore.RESET)

            if Answer == i[2]:
                score += 1
                print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
            else:
                print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)

            print("yor final score is :", score, "/8")

        else:
            print("Thank you good by")
            exit()

        PersonID = int(input("\33[1m\33[34m\t\t Enter your id number\33[0m"))
        FirstName = input("\33[1m\33[34m\t\t Enter your firstname\33[0m ")
        LastName = input("\33[1m\33[34m\t\t Enter your lastname\33[0m ")

        Result = score
        self.cursor.execute("INSERT INTO Datas (PersonID, FirstName,  LastName, score ) VALUES (?, ?, ?, ?)",
                            (PersonID, FirstName, LastName, Result))
        self.join.commit()
