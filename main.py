változó: str = "változó"
feltétel: bool = True
ciklus_feltétel: bool = True
bejárandó: list[int] = [3, 2, 1]
sorok_lista: list[str] = ["fejlécsor", "1. adatsor", "2. adatsor"]


# ítypes snippet:
# adattípusok súgó:
# int -> egész típus - 18
# float -> valós (tört) típus - 20.5
# str -> szöveges típus - "kilincs"
# bool -> logikai típus - True, vagy False
# list -> lista típus - ["alma", "körte", "alma"]
# tuple -> tuple típus - ("János", 35, 1.75, True)
# dict -> szótár típus - {"Jenő": 36, "Béla": 13}
# set -> halmaz típus - {"Jupiter", "Vénusz"}
# példák:
# my_tuple: tuple[str, int, float, bool] = ("János", 35, 1.75, True)
# my_set: set[str] = {"Jupiter", "Vénusz"}
# my_dict: dict[str, int] = {"Jenő": 36, "Béla": 13}


# íclass snippet:
class osztály_neve(object):
    # íproperty snippet:
    @property
    def jellemző_neve(self) -> int:
        return 0

    # def(__init__) snippet:
    def __init__(self, állomány_neve: str) -> None:
        pass

    # íclass(metódus) snippet:
    def metódus_neve(self, p1: int, p2: int) -> int:
        return p1 + p2


# ídef snippet:
def függvény_neve(p1: int, p2: int) -> int:
    return p1 + p2


# íif snippet:
if feltétel:
    pass

# íif/else snippet:
if feltétel:
    pass
else:
    pass

# íwhile snippet
while ciklus_feltétel:
    pass

# ífor snippet
for cilkus_változója in bejárandó:
    pass

# ífor-range() snippet
for cilkus_változója in range(0, 11):  # 0-10
    pass

# ítry/except snippet:
try:
    # védett blokk
    pass
except ValueError as ex:
    print(ex)

# íopen() - olvasás snippet:
with open("file_neve.txt", "r", encoding="utf-8") as file:
    for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
        pass

# íopen() - írás snippet:
with open("file_neve.txt", "w", encoding="utf-8") as file:
    file.writelines(sorok_lista)

# ílist snippet:
lista_neve: list[int] = [1, 2, 3]

# íset snippet:
halmaz_neve: set[str] = {"Szaturnusz", "Vénusz"}

# ídict snippet:
szótár_neve: dict[str, int] = {"Jenő": 36, "Béla": 13}

# íprint(f) snippet:
print(f"Példa: {változó}", end="")


# ímain() snippet:
def main() -> None:
    pass  # Kezd a kódolást itt!


if __name__ == "__main__":
    main()
