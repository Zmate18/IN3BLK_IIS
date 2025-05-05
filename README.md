# Információs Rendszerek Integrálása féléves feladat
## Sorszám: 11
**Fény intenzitás monitorozó rendszer**

Készítsen egy alkalmazást, amely a beltéri fényszintet (lux) figyeli. A rendszer három külön kliensből áll: egy adatgenerátorból, egy feldolgozóból és egy riasztás-kezelő kliensből.

Komponens 1: Light Intensity Generation Client

Csatlakozás: A kliens a lightIntensityQueue pontról-pontra típusú (point-to-point) üzenetsorhoz csatlakozik.
Feladat: 3 másodpercenként véletlenszerű fényszint-adatokat (lux értékeket) küld, például 0 és 2000 lux között.
Példa: 300 lux, 1500 lux, stb.

Komponens 2: Light Intensity Processor

Üzenetfogadás: Egy processzor, amely kizárólag a lightIntensityQueue üzeneteit kapja meg (fényszint mérési adatok).
Feldolgozás: Meghatározza, hogy a fényerő értéke túl alacsony-e. Például dönthetünk úgy, hogy 100 lux alatti érték esetén „sötét” állapotot észlelünk.
Riasztás küldése: Ha 3 egymást követő mérés alatt marad 100 luxon, a processzor egy riasztásüzenetet küld a lightAlertQueue üzenetsorba azzal a szöveggel, hogy pl. “Low light alert: 3 consecutive readings below 100 lux.”

Komponens 3: Alert Reporting Client

Fogyasztás: A kliens a lightAlertQueue üzenetsorból olvassa a riasztásokat.
Kimenet: A kapott értesítéseket kiírja a konzolra, pl. “Low light alert: 3 consecutive readings below 100 lux.”

Működés tesztelése:

Üzenetküldés és -fogadás tesztelése: Ellenőrizd, hogy a fényszint-adatokat helyesen küldi és fogadja a rendszer.
Alacsony fényszint felismerése: Teszteld, hogy 3 egymást követő <100 lux érték esetén a riasztás helyesen továbbítódik.
Riasztási mechanizmus: Ellenőrizd, hogy a lightAlertQueue-ba kerül-e az üzenet, és a kliens kiírja-e a figyelmeztetést a konzolra.
