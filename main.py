feltétel: bool = True
ciklus_feltétel: bool = True
bejárandó: list[int] = [3, 2, 1]


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
class classname(object):
    # ú class(method) snippet:
    def metódus_neve(self, p1: int) -> int:
        return p1

    # def(__init__) snippet:
    def __init__(self, p1: str) -> None:
        pass


# ídef snippet:
def fg_neve(par1: int, par2: int) -> int:
    return par1 + par2


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
for ciklus_változója in bejárandó:
    pass

# ífor-range() snippet
for ciklus_változója in range(0, 11):  # 0 - 10
    pass

# ítry/except snippet:
try:
    # védett blokk
    pass
except ValueError as ex:
    print(ex)

# íopen() snippet:
with open("file_neve.txt", "r", encoding="utf-8") as file:
    for sor in file.read().splitlines()[1:]: # [1:] - első sor kihagyása
        pass

# ílist snippet:
lista_neve: list[int] = [1, 2, 3]

# ímain() snippet:
def main() -> None:
    pass


if __name__ == "__main__":
    main()
