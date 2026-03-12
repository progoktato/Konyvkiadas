def get_TH(tartalom):
    return f"<th>{str(tartalom)}</th>"


def get_TD(tartalom):
    return f"<td>{str(tartalom)}</td>"


def get_TR(cellak):
    return f"<tr>\n\t{''.join(cellak)}\n</tr>\n"


def get_TABLE(sorok):
    return f"<table>\n{''.join(sorok)}</table>"


konyvek = list()
f = open("kiadas.txt", "r", encoding="utf-8")
for sor in f:
    mezok = sor.strip().split(";")

    konyv = dict()
    konyv["ev"] = int(mezok[0])
    konyv["n_ev"] = int(mezok[1])
    konyv["eredete"] = mezok[2]
    konyv["leiras"] = mezok[3]
    konyv["peldanyszam"] = int(mezok[4])

    konyvek.append(konyv)
f.close()

print("2. feladat:")

print("Szerző:", end="")
# szerzo = input()
szerzo = "Benedek Elek"  # teszteléshez
kiadasok_szama = 0
for konyv in konyvek:
    if konyv["leiras"].split(':')[0] == szerzo:
        # if konyv["leiras"].find(szerzo) != -1:  # ez sem az igazi, mert lehet, hogy a szerző neve egy másik szóban is benne van
        # if szerzo in konyv["leiras"]:     # nem mindig jó
        kiadasok_szama += 1

if kiadasok_szama == 0:
    print("Nem adtak ki!")
else:
    print(f'{kiadasok_szama} könyvkiadás')

print("3. feladat:")

seged_lista = list()
for konyv in konyvek:
    seged_lista.append(konyv["peldanyszam"])

max_peldanyszam = max(seged_lista)
print(
    f"Legnagyobb példányszám: {max_peldanyszam}, előfordult {seged_lista.count(max_peldanyszam)} alkalommal")

print("4. feladat:")
for konyv in konyvek:
    if konyv["peldanyszam"] > 40000 and konyv["eredete"] == "kf":
        print(f"{konyv['ev']}/{konyv['n_ev']}. {konyv['leiras']}")
        break

print("5a. feladat:")

evek = dict()
for ev in range(2020, 2024):
    # minden évhez egy újabb szótárat rendelünk, amiben majd a kiadásokat és példányszámokat tároljuk
    evek[ev] = dict()
    evek[ev]["magyar_kiadas"] = 0
    evek[ev]["magyar_peldanyszam"] = 0
    evek[ev]["kulfoldi_kiadas"] = 0
    evek[ev]["kulfoldi_peldanyszam"] = 0

for konyv in konyvek:
    if konyv["eredete"] == "ma":  # magyar kiadás
        # a magyar kiadás számát növeljük 1-gyel
        evek[konyv["ev"]]["magyar_kiadas"] += 1
        # a magyar példányszámot növeljük a könyv példányszámával
        evek[konyv["ev"]]["magyar_peldanyszam"] += konyv["peldanyszam"]
    else:
        evek[konyv["ev"]]["kulfoldi_kiadas"] += 1
        evek[konyv["ev"]]["kulfoldi_peldanyszam"] += konyv["peldanyszam"]

print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
for ev in range(2020, 2024):
    print(
        f"{ev}\t\t{evek[ev]['magyar_kiadas']}\t\t{evek[ev]['magyar_peldanyszam']}\t\t{evek[ev]['kulfoldi_kiadas']}\t\t{evek[ev]['kulfoldi_peldanyszam']}")

# Ez volt az ONLINE órai

# print("5a. feladat:")
# print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")

# for ev in range(2020, 2024):
#     magyar_kiadas = 0
#     magyar_peldanyszam = 0
#     kulfoldi_kiadas = 0
#     kulfoldi_peldanyszam = 0

#     for konyv in konyvek:
#         if konyv["ev"] == ev:
#             if konyv["eredete"] == "ma":
#                 magyar_kiadas += 1
#                 magyar_peldanyszam += konyv["peldanyszam"]
#             else:
#                 kulfoldi_kiadas += 1
#                 kulfoldi_peldanyszam += konyv["peldanyszam"]

#     print(
#         f"{ev}\t\t{magyar_kiadas}\t\t{magyar_peldanyszam}\t\t{kulfoldi_kiadas}\t\t{kulfoldi_peldanyszam}")

print("5b. feladat:")

sorok = list()  # a táblázat sorait fogjuk ebben a listában tárolni

# Első sor: a táblázat fejlécét tartalmazza
cellak = list()
cellak.append(get_TH("Év"))
cellak.append(get_TH("Magyar kiadás"))
cellak.append(get_TH("Magyar példányszám"))
cellak.append(get_TH("Külföldi kiadás"))
cellak.append(get_TH("Külföldi példányszám"))

sorok.append(get_TR(cellak))

# A táblázat többi sora: a kiadásokat és példányszámokat tartalmazza
for ev in range(2020, 2024):
    cellak = list()
    cellak.append(get_TD(ev))
    cellak.append(get_TD(evek[ev]["magyar_kiadas"]))
    cellak.append(get_TD(evek[ev]["magyar_peldanyszam"]))
    cellak.append(get_TD(evek[ev]["kulfoldi_kiadas"]))
    cellak.append(get_TD(evek[ev]["kulfoldi_peldanyszam"]))
    sorok.append(get_TR(cellak))

# A táblázatot tartalmazó HTML kódot egy fájlba írjuk
# Kicsit eltér a mintától, mert a fájlban egy kicsit szebben formázott HTML kódot szerettem volna!

iras = open("tabla.html", "w", encoding="utf-8")
iras.write(get_TABLE(sorok))
iras.close()


print("6. feladat:")
print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")

kiadasok_szama = dict()
elso_kiadas_peldanyszama = dict()

# a kiadásokat a leírásuk szerint csoportosítjuk, és megszámoljuk, hogy hány kiadás tartozik egy-egy leíráshoz
# a példányszámokat is összesítjük, hogy később ki tudjuk írni, hogy melyik könyvből hány példányt adtak ki összesen
for konyv in konyvek:
    if konyv["leiras"] not in kiadasok_szama:
        kiadasok_szama[konyv["leiras"]] = 0
        elso_kiadas_peldanyszama[konyv["leiras"]] = konyv["peldanyszam"]
    else:
        if konyv["peldanyszam"] > elso_kiadas_peldanyszama[konyv["leiras"]]:
            kiadasok_szama[konyv["leiras"]] += 1

for leiras in kiadasok_szama:
    if kiadasok_szama[leiras] >= 2:  # legalább kétszer újra kiadták

        print(f"{leiras}")
