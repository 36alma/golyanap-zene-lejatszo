# Gólyanap Zene Lejátszó

Ez a projekt egy interaktív, csapat-alapú zene felismerő játék, amelyet Pythonban készítettem. A program célja, hogy zenéket játsszon le, a játékosoknak pedig ki kell találniuk a dal címét és szerzőjét, miközben pontokat gyűjtenek. A játék támogatja a csapatválasztást, pontszámok számítását, valamint az eredmények API-n keresztüli továbbítását.

---

## Tartalomjegyzék

- [Funkciók](#funkciók)
- [Telepítés](#telepítés)
- [Használat](#használat)
- [Konfiguráció](#konfiguráció)
- [API és Biztonság](#api-és-biztonság)
- [Technikai részletek](#technikai-részletek)
- [Hibaelhárítás](#hibaelhárítás)
- [Fejlesztői információk](#fejlesztői-információk)
- [Licenc](#licenc)
- [Gyakori kérdések (FAQ)](#gyakori-kérdések-faq)
- [Kapcsolat](#kapcsolat)

---

## Funkciók

- **Zenelejátszás**: A `zene/` mappában található MP3 fájlokból véletlenszerűen választ zenét, és lejátssza azt.
- **Csapatválasztás**: Több csapat közül lehet választani, a pontszámok csapathoz kötöttek.
- **Interaktív menü**: Nyilakkal navigálható, Enterrel választható menü, színes, grafikus felület.
- **Zene felismerés**: Minden lejátszott dal után a játékos eldöntheti, felismerte-e a szerzőt és a címet, választhat billentyűzettel.
- **Pontszámítás**: A helyes válaszok után pontokat kap a csapat, százalékos eredmény is megjelenik.
- **API kommunikáció**: Az eredmények titkosítva, biztonságosan elküldhetők egy szervernek, JSON formátumban.
- **Biztonság**: RSA és AES titkosítás, tanúsítvány alapú kommunikáció, titkosított jelszavak.
- **Hibakezelés**: Részletes hibaüzenetek, naplózás.
- **Könnyen bővíthető**: Új zenék, csapatok, API végpontok egyszerűen hozzáadhatók.

---

## Telepítés

### Előfeltételek

- Python 3.8 vagy újabb
- Windows operációs rendszer (bash, cls parancs támogatott)
- Ajánlott: virtuális környezet

### Könyvtárak telepítése

```bash
pip install -r requirements.txt
```

### Fájlstruktúra

- `main.py` – fő program
- `zene/` – MP3 zenék
- `keys/` – SSL tanúsítványok, publikus kulcsok
- `.env` – konfigurációs változók
- `requirements.txt` – függőségek
- `LICENSE.txt` – licenc

---

## Használat

```bash
python main.py
```

1. **Csapat kiválasztása**: A menüben válassz csapatot a nyilakkal, Enterrel.
2. **Játék indítása**: Indítsd el a zenéket, minden dal után válaszolj a kérdésekre.
3. **Pontszámok megtekintése**: A menüben bármikor megnézheted a csapatod pontszámát.
4. **Eredmények küldése**: Az API-nak titkosítva elküldheted az eredményeket.
5. **Kilépés**: A menüben választható.

### Fő menü

- Indítás a zenéket
- Pontszámok megtekintése
- Csapat kiválasztás
- Kilépés

---

## Konfiguráció

A `.env` fájlban adhatod meg az API eléréséhez szükséges adatokat:

```
API_URL=https://sajatapi.hu
API_KEY=valami_kulcs
API-USER=felhasznalo
API-PASSWORD=jelszo
API_SSL=True
AES_KEY=valami_aes_kulcs
```

A `keys/` mappában legyenek a tanúsítványok:

- `client-key.pem`, `client.crt`, `public_key.pem`

---

## API és Biztonság

- **Adatküldés**: Az eredmények JSON formátumban, titkosítva kerülnek elküldésre.
- **Titkosítás**: RSA (publikus kulcs) + AES (Fernet) kombináció.
- **SSL**: Tanúsítvány alapú kommunikáció, biztonságos adatátvitel.
- **Hibakezelés**: Minden API hívásnál részletes hibaüzenet, timeout védelem.

---

## Technikai részletek

- **Könyvtárak**: playsound, pygame, cryptography, requests, dotenv, readchar, urllib3
- **Fő osztályok**:
  - `MusicPlayer`: zenelejátszás, válaszok kezelése
  - `MusicClass`: zene metaadatok feldolgozása
  - `AnswerClass`: válaszok tárolása
  - `PontClass`: pontszámítás
  - `TeamClass`: csapatok kezelése
  - `ApiClass`: API kommunikáció, titkosítás
  - `MainClass`: menü, vezérlés
- **Platform**: Windows (bash, cls parancs)
- **Színes terminál**: ANSI kódokkal
- **Interaktív input**: readchar, billentyűzet események

---

## Hibaelhárítás

- **Nem indul el a program**: Ellenőrizd a Python verziót, függőségeket.
- **API hiba**: Ellenőrizd a `.env` fájlt, tanúsítványokat, internetkapcsolatot.
- **Zene nem játszható le**: Ellenőrizd, hogy a `zene/` mappában vannak-e MP3 fájlok.
- **Billentyűzet input nem működik**: Próbáld meg másik terminálban futtatni.
- **Hibás fájlformátum**: Csak a `Szerző - Cím.mp3` formátumot támogatja.

---

## Fejlesztői információk

- **Bővíthetőség**: Új zenék hozzáadása: másold a `zene/` mappába, a formátum legyen: `Szerző - Cím.mp3`.
- **Új csapat hozzáadása**: A `TeamClass` osztályban bővíthető a lista.
- **API végpontok módosítása**: A `.env` fájlban módosítható.
- **Kódstílus**: PEP8, docstringek, magyar nyelvű kommentek.
- **Tesztelés**: Manuális tesztelés, hibakezelés minden fő funkciónál.

---

## Licenc

A projekt rootjában található `LICENSE.md` fájl fontos információkat tartalmaz a használatról, érdemes elolvasni, és mindenki tudomásul veszi a feltételeket, ha használja vagy felhasználja a projektet.  

A projekt **AI-elemeket is tartalmaz**.


---

## Gyakori kérdések (FAQ)

**Hogyan adhatok hozzá új zenét?**

- Másold a zenét a `zene/` mappába, a fájlnév legyen: `Szerző - Cím.mp3`.

**Miért nem indul el az API kommunikáció?**

- Ellenőrizd a `.env` fájlt, tanúsítványokat, internetkapcsolatot.

**Hogyan lehet új csapatot hozzáadni?**

- A `TeamClass` osztályban bővítsd a listát.

**Milyen titkosítás van?**

- RSA publikus kulcs, AES (Fernet), SSL tanúsítvány.

**Milyen operációs rendszeren fut?**

- Windows támogatott, bash/cls parancsokkal.

---

## Kapcsolat

Szerző: **36alma**

Kérdés, engedélykérés: [36alma@vaultdrive.eu](mailto:36alma@vaultdrive.eu)

---

> Ez a projekt egyedi, oktatási célú fejlesztés, minden jog fenntartva!

</div>
