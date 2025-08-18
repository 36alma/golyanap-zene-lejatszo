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
STRIKETHROUGH = "\033[9m"
WAITTIME = 20

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
        time.sleep(WAITTIME)
        self.stop()
        while True:
            choice_author = input("Adja meg a szerzőt el a taláták. (I/N) ").lower()
            choice_title = input("Adja meg a címet el a taláták. (I/N) ").lower()
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
        self.pontja = 0
        self.szazalek = 0
        self.maxpont = int(len(Player.team)*2)

    def pontcall(self,lista):
        self.pont = 0
        x = 0
        for item in lista:
            self.choice_author = item["choice_author"]
            self.choice_title = item["choice_title"]
            if self.choice_author == True and self.choice_title == True:
                self.pont += 2
            elif self.choice_author == True or self.choice_title == True:
                self.pont += 1
            else:
                self.pont += 0
            x += 1
        self.szazalek = self.pont / self.maxpont * 100
        self.pontja = int(self.szazalek * 0.2)
        return self.pontja

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
class ApiClass:
    def __init__(self):
        self.url = os.getenv("API_URL", "YOUR_API_URL")
        self.api_key = os.getenv("API_KEY", "your_api_key_here")
        
        with open("keys/public_key.pem", "rb") as f:
            self.public_key = serialization.load_pem_public_key(f.read())
        self.token = None
        if self.token:
            self.headers = {
                "Authorization": f"Bearer {self.token}"
            }
        else:
            self.headers = {}

    def main_handel(self):
        data = {
            "team": Main.team_name,       
            "point": Main.pont,
            "startime": Main.startime,
            "endtime": datetime.datetime.now().isoformat(),
            "zenevalaszok": Player.team
        }
        return data

    def auth(self):
        user = os.getenv("API-USER", "YOUR_API_USER")
        password = os.getenv("API-PASSWORD", "YOUR_API_PASSWORD")
        
        # AES kulcs generálása
        original_key = os.getenv("AES_KEY", "your_aes_key_here").encode()
        fernet_key = base64.urlsafe_b64encode(hashlib.sha256(original_key).digest())
        cipher_suite = Fernet(fernet_key)

        # Felhasználói adatok titkosítása
        data = {"username": user, "password": password}
        data_str = json.dumps(data, ensure_ascii=False)
        encrypted_data = cipher_suite.encrypt(data_str.encode('utf-8'))

        # AES kulcs titkosítása RSA-val
        encrypted_aes_key = self.public_key.encrypt(
            fernet_key,   
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_aes_key_b64 = base64.b64encode(encrypted_aes_key).decode('utf-8')
        encrypted_data_b64 = base64.b64encode(encrypted_data).decode('utf-8')

        try:
            response = requests.post(
                f"{self.url}/api/auth",
                json={
                    "key": encrypted_aes_key_b64,
                    "data": encrypted_data_b64
                },
                timeout=30
            )
            if response.status_code == 200:
                response_data = response.json()
                self.headers = {
                "Authorization": f"Bearer {response_data.get("token")}"
            }
                return response_data.get("token")
            else:
                print(f"❌ Hiba: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Hiba: {e}")
        return None

    def senddata(self):
        self.token = self.auth()
        data = self.main_handel()
        try:
            response = requests.post(
                f"{self.url}/api/json",
                headers=self.headers,
                json=data,
                timeout=30
            )
            return response
        except Exception as e:
            print(f"❌ Hiba: {e}")
            return None
class MainClass:
    def __init__(self):
        self.use_play_music = True
        self.use_pont = False
        self.use_pont_cache = True
        self.team_name = None
        self.team_select = False
        self.pont: int = None
        self.startime = datetime.datetime.now().isoformat()
    
        
    def main(self):
        self.menu_options = [
            "Indítás a zenéket",
            "Pontszámok megtekintése",
            "Csapat kiválasztás",
            "Kilépés"
        ]
        self.current_idx = 0
        while True:
            self.menu()
            self.choice = int(input("Válassz egy lehetőséget: ").strip())
            if self.choice == 1 and self.team_select == True:
                while len(Player.music) > 0 and self.use_play_music == True:
                    Player.main()
                self.use_play_music = False
            elif self.choice == 1 and self.use_play_music == False:
                print("Sajnos a funkció elindításához újra kell inditani a szofvert.")
            elif self.choice == 2 and self.use_pont == True and self.team_select == True:
                pont = Pont.pontcall(Player.team)
                print(f"Pontszám: {pont}")
                self.use_pont = False
            elif self.choice == 2 and self.use_pont == False:
                print(f"Pontszám: {pont}")
            elif self.choice == 3:
                print("Csapatok:")
                for i in range(len(Team.team)):
                    print(f"{i+1}. {Team.team[i]}")
                self.team_select = Team.checkteam(input("Adja meg a csapatot."))
                print(f"A kiválasztott csapat: {Main.team_name}")
            elif self.choice == 0:
                break
            elif self.team_select != True:
                print("Nincs kiválasztott csapat.")
            else:
                print("Helytelen menü pont")
                continue
    def menu(self):
        whiler = True
        self.availability = [
            self.team_select,
            self.use_pont,
            True,
            True
        ]
        selected = 0
        current_idx = 0
            
        while whiler:
            # Menü kirajzolása 
            print("\033c", end="")  # képernyő törlése
            print("Használd a nyilakat a navigációhoz, Enter a választáshoz.\n")
            for i, option in enumerate(self.menu_options):
                if not self.availability[i] and i == current_idx:
                    print(f"> {RED}{option} (lezárt){RESET}")
                elif not self.availability[i] and i != current_idx:
                    print(f" {RED}{option} (lezárt){RESET}")
                elif i == current_idx:
                    print(f"> {GREEN}{option}{RESET}")
                else:
                    print(f"  {option}")
                
            key = readchar.readkey()
            if key == readchar.key.UP:
                current_idx = (current_idx - 1) % len(self.menu_options)
            elif key == readchar.key.DOWN:
                current_idx = (current_idx + 1) % len(self.menu_options)
            elif key == readchar.key.ENTER:
                whiler = False
                return current_idx
                

    def select_team(self):
        whiler = True
        current_idx = 0
        while whiler:
            # Menü kirajzolása 
            print("\033c", end="")  # képernyő törlése
            print("Használd a nyilakat a navigációhoz, Enter a választáshoz.\n")
            for i, option in enumerate(Team.team):
                if i == current_idx:
                    print(f"> {GREEN}{option}{RESET}")
                else:
                    print(f"  {option}")
                
            key = readchar.readkey()
            if key == readchar.key.UP:
                current_idx = (current_idx - 1) % len(Team.team)
            elif key == readchar.key.DOWN:
                current_idx = (current_idx + 1) % len(Team.team)
            elif key == readchar.key.ENTER:
                whiler = False
                Main.team_select = Team.checkteam(current_idx+1)
                print(Main.team_select)

            
            
if __name__ == "__main__":
    try:
        Player = MusicPlayer()
        Music = MusicClass()
        Answer = AnswerClass()
        Pont = PontClass()
        Main = MainClass()
        Team = TeamClass()
        Player.forindex()
        Main.main()
    except Exception as e:
        print(f"Hiba történt: {e}")