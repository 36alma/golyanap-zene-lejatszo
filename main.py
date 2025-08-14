from playsound import playsound
import os
import random
import json
import pygame
import time
filesfolder = os.path.join(os.path.dirname(__file__), 'zene')
files = os.listdir(filesfolder)
RESET = "\033[0m"
BLUE = "\033[34m"
RED = "\033[31m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
class MusicPlayer:
    def __init__(self):
        self.files = files
        self.music = [

        ]
        
        self.team = []
    def forindex(self):
        for index in range(len(self.files)):
            item = self.files[index]
            classes = MusicClass().main(item)
            self.music.append(dict(
                    author=classes.music_author,
                    title=classes.music_title,
                    src=classes.music_src
                ))

    def play(self, file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    def stop(self):
        pygame.mixer.music.stop()
    def main(self):
        random.shuffle(self.music)
        choice = random.choice(self.music)
        self.play(choice['src'][0])
        print(f"Lejátszott zene: Cím:{choice['title'][0]} - Szerző:{choice['author'][0]}")
        time.sleep(20)
        self.stop()
        while True:
            choice_author = input("Sikerült eltalálni a szerzőt? (I/N)\n ").strip().lower()
            choice_title = input("Sikerült eltalálni a címet? (I/N)\n").strip().lower()
            if choice_author in ["i", "n"] and choice_title in ["i", "n"]:
                break
            else:
                print("Érvénytelen válasz. Kérlek, válaszolj 'I' vagy 'N'!")
        obj = AnswerClass(choice, choice_author, choice_title)
        classes = obj.main()
        self.team.append(dict(
            choice=classes.choice,
            choice_author=classes.choice_author,
            choice_title=classes.choice_title
        ))
        input("A következő nyomj egy entert!")
        index = self.music.index(choice)
        self.music.pop(index)

class AnswerClass:   
    def __init__(self, choice=None, choice_author=None, choice_title=None):
        self.choice = []
        self.choice_author = choice_author
        self.choice_title = choice_title
        if choice is not None:
            self.choice.append(choice)
    
    def main(self):
        if self.choice_author and self.choice_author[0] == "i":
            self.choice_author = True
        else:
            self.choice_author = False
            
        if self.choice_title and self.choice_title[0] == "i":
            self.choice_title = True
        else:
            self.choice_title = False
        return self

class PontClass:
    def __init__(self):
        self.pont = 0
    def pontcall(self,lista):
        self.pont = 0
        for item in lista:
            self.choice_author = item.choice_author
            self.choice_title = item.choice_title
            if self.choice_author == True and self.choice_title == True:
                self.pont += 2
            elif self.choice_author == True or self.choice_title == True:
                self.pont += 1
            else:
                self.pont += 0
        return self.pont

class MusicClass:
    def __init__(self):
        self.music_author = []
        self.music_title = []
        self.music_src = []
    def main(self,index):
        item = index
        item = item.strip("'")
        reszek = list(self.split(item, " - "))
        reszek.append(self.split(reszek[-1], "."))
        if len(reszek) == 3:
            reszek.pop(1)
            reszek[1].pop(1)
            self.music_author.append(reszek[0])
            self.music_title.append(str(reszek[1][0]))
            self.music_src.append(os.path.join(filesfolder, item))
            
            return self
        else:
            print("Hibás fájlformátum")
            return None
    def split(self, item,splite_id):
        reszek = item.split(splite_id)
        return reszek

class TeamClass:
    def __init__(self):
        self.team = ["Barna","Fehér","Fekete","Lila","Narancssárga","Piros","Rózsaszín","Sötétzöld","Világoskék"]
    def checkteam(self,inputteam):
        inputteam = self.team[int(inputteam)-1]
        if inputteam in self.team:
            Main.team_name = inputteam
            return True
        else:
            return False

class MainClass:
    def main(self):
        while True:
            self.menu()
            self.choice = input("Válassz egy lehetőséget: ").strip()
            if self.choice == "1":
                while len(Player.music) > 0:
                    Player.main()
            elif self.choice == "2":
                Pont.pontcall(Player.team)
            elif self.choice == "0":
                break
            else:
                print("Helytelen menü pont")
    def menu(self):
        print(f"{BOLD}{UNDERLINE}{CYAN}=== Főmenü ==={RESET}")
        print(f"{GREEN}1.{RESET} {BOLD}Indítás a zenéket.{RESET}")
        print(f"{YELLOW}2.{RESET} {UNDERLINE}Pontszámok megtekintése.{RESET}")
        print(f"{RED}0.{RESET} Kilépés.")

if __name__ == "__main__":
    Player = MusicPlayer()
    Music = MusicClass()
    Answer = AnswerClass()
    Pont = PontClass()
    Main = MainClass()
    Player.forindex()
    Main.main()