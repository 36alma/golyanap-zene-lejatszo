# Gólyanap Zene Lejátszó

Ez a projekt egy interaktív, csapat-alapú zene felismerő játék, amelyet Pythonban készítettem. A program célja, hogy zenéket játsszon le, a játékosoknak pedig ki kell találniuk a dal címét és szerzőjét, miközben pontokat gyűjtenek. A játék támogatja a csapatválasztást, pontszámok számítását, valamint az eredmények API-n keresztüli továbbítását.

---

## Tartalomjegyzék

* Funkciók
* Telepítés
* Használat
* Konfiguráció
* API és Biztonság
* Technikai részletek
* Hibaelhárítás
* Fejlesztői információk
* Licenc
* Gyakori kérdések (FAQ)
* Kapcsolat

---

## Funkciók

* **Zenelejátszás**: A [zene](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) mappában található MP3 fájlokból véletlenszerűen választ zenét, és lejátssza azt.
* **Csapatválasztás**: Több csapat közül lehet választani, a pontszámok csapathoz kötöttek.
* **Interaktív menü**: Nyilakkal navigálható, Enterrel választható menü, színes, grafikus felület.
* **Zene felismerés**: Minden lejátszott dal után a játékos eldöntheti, felismerte-e a szerzőt és a címet, választhat billentyűzettel.
* **Pontszámítás**: A helyes válaszok után pontokat kap a csapat, százalékos eredmény is megjelenik.
* **API kommunikáció**: Az eredmények titkosítva, biztonságosan elküldhetők egy szervernek, JSON formátumban.
* **Biztonság**: RSA és AES titkosítás, tanúsítvány alapú kommunikáció, titkosított jelszavak.
* **Hibakezelés**: Részletes hibaüzenetek, naplózás.
* **Könnyen bővíthető**: Új zenék, csapatok, API végpontok egyszerűen hozzáadhatók.

---

## Telepítés

### Előfeltételek

* Python 3.8 vagy újabb
* Windows operációs rendszer (bash, cls parancs támogatott)
* Ajánlott: virtuális környezet

### Könyvtárak telepítése

### Fájlstruktúra

* [main.py](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – fő program
* [zene](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – MP3 zenék
* [keys](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – SSL tanúsítványok, publikus kulcsok
* [.env](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – konfigurációs változók
* [requirements.txt](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – függőségek
* [LICENSE.txt](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – licenc

---

## Használat

1. **Csapat kiválasztása**: A menüben válassz csapatot a nyilakkal, Enterrel.
2. **Játék indítása**: Indítsd el a zenéket, minden dal után válaszolj a kérdésekre.
3. **Pontszámok megtekintése**: A menüben bármikor megnézheted a csapatod pontszámát.
4. **Eredmények küldése**: Az API-nak titkosítva elküldheted az eredményeket.
5. **Kilépés**: A menüben választható.

### Fő menü

* Indítás a zenéket
* Pontszámok megtekintése
* Csapat kiválasztás
* Kilépés

---

## Konfiguráció

A [.env](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) fájlban adhatod meg az API eléréséhez szükséges adatokat:

A [keys](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) mappában legyenek a tanúsítványok:

* `client-key.pem`, `client.crt`, `public_key.pem`

---

## API és Biztonság

* **Adatküldés**: Az eredmények JSON formátumban, titkosítva kerülnek elküldésre.
* **Titkosítás**: RSA (publikus kulcs) + AES (Fernet) kombináció.
* **SSL**: Tanúsítvány alapú kommunikáció, biztonságos adatátvitel.
* **Hibakezelés**: Minden API hívásnál részletes hibaüzenet, timeout védelem.

---

## Technikai részletek

* **Könyvtárak**: playsound, pygame, cryptography, requests, dotenv, readchar, urllib3
* **Fő osztályok**:
  * `MusicPlayer`: zenelejátszás, válaszok kezelése
  * `MusicClass`: zene metaadatok feldolgozása
  * `AnswerClass`: válaszok tárolása
  * `PontClass`: pontszámítás
  * `TeamClass`: csapatok kezelése
  * `ApiClass`: API kommunikáció, titkosítás
  * `MainClass`: menü, vezérlés
* **Platform**: Windows (bash, cls parancs)
* **Színes terminál**: ANSI kódokkal
* **Interaktív input**: readchar, billentyűzet események

---

## Hibaelhárítás

* **Nem indul el a program**: Ellenőrizd a Python verziót, függőségeket.
* **API hiba**: Ellenőrizd a [.env](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) fájlt, tanúsítványokat, internetkapcsolatot.
* **Zene nem játszható le**: Ellenőrizd, hogy a [zene](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) mappában vannak-e MP3 fájlok.
* **Billentyűzet input nem működik**: Próbáld meg másik terminálban futtatni.
* **Hibás fájlformátum**: Csak a `Szerző - Cím.mp3` formátumot támogatja.

---

## Fejlesztői információk

* **Bővíthetőség**: Új zenék hozzáadása: másold a [zene](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) mappába, a formátum legyen: `Szerző - Cím.mp3`.
* **Új csapat hozzáadása**: A `TeamClass` osztályban bővíthető a lista.
* **API végpontok módosítása**: A [.env](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) fájlban módosítható.
* **Kódstílus**: PEP8, docstringek, magyar nyelvű kommentek.
* **Tesztelés**: Manuális tesztelés, hibakezelés minden fő funkciónál.

---

## Licenc

Ez a projekt kizárólag oktatási célokra használható, kereskedelmi felhasználás tilos! Részletek a LICENSE.txt-ben.

---

## Gyakori kérdések (FAQ)

**Hogyan adhatok hozzá új zenét?**

* Másold a zenét a [zene](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) mappába, a fájlnév legyen: `Szerző - Cím.mp3`.

**Miért nem indul el az API kommunikáció?**

* Ellenőrizd a [.env](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) fájlt, tanúsítványokat, internetkapcsolatot.

**Hogyan lehet új csapatot hozzáadni?**

* A `TeamClass` osztályban bővítsd a listát.

**Milyen titkosítás van?**

* RSA publikus kulcs, AES (Fernet), SSL tanúsítvány.

**Milyen operációs rendszeren fut?**

* Windows támogatott, bash/cls parancsokkal.

---

## Kapcsolat

Szerző: **36alma**

Kérdés, engedélykérés: [36alma@vaultdrive.eu](vscode-file://vscode-app/c:/Users/Tak%C3%A1cs%20D%C3%A1vid/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)

---

> Ez a projekt egyedi, oktatási célú fejlesztés, minden jog fenntartva!
>
