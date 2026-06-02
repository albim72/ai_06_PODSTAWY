import csv
import random
from faker import Faker


LICZBA_REKORDOW = 100_000
NAZWA_PLIKU = "dane_syntetyczne.csv"
SEED = 42

fake = Faker("pl_PL")
Faker.seed(SEED)
random.seed(SEED)


def generuj_wiek():
    """
    Generuje wiek zgodnie z zadanym rozkładem:

    1-15 lat    -> 15%
    16-30 lat   -> 30%
    31-55 lat   -> 30%
    56+ lat     -> 25%
    """

    grupa = random.choices(
        population=["dziecko", "mlody", "dorosly", "senior"],
        weights=[15, 30, 30, 25],
        k=1
    )[0]

    if grupa == "dziecko":
        return random.randint(1, 15)

    if grupa == "mlody":
        return random.randint(16, 30)

    if grupa == "dorosly":
        return random.randint(31, 55)

    return random.randint(56, 95)


def generuj_kolor():
    """
    Generuje kolor zgodnie z zadanym rozkładem:

    czerwony -> 60%
    zielony  -> 10%
    biały    -> 30%
    """

    return random.choices(
        population=["czerwony", "zielony", "biały"],
        weights=[60, 10, 30],
        k=1
    )[0]


def generuj_kwote():
    """
    Generuje kwotę z zakresu od 300 do 1600.
    """

    return random.randint(300, 1600)


def generuj_dane():
    """
    Generator rekordów syntetycznych.
    """

    for record_id in range(1, LICZBA_REKORDOW + 1):
        yield {
            "id": record_id,
            "imię": fake.first_name(),
            "nazwisko": fake.last_name(),
            "miasto": fake.city(),
            "wiek": generuj_wiek(),
            "kolor": generuj_kolor(),
            "kwota": generuj_kwote(),
        }


def zapisz_do_csv():
    """
    Zapisuje dane syntetyczne do pliku CSV.
    """

    pola = [
        "id",
        "imię",
        "nazwisko",
        "miasto",
        "wiek",
        "kolor",
        "kwota",
    ]

    with open(NAZWA_PLIKU, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=pola)
        writer.writeheader()

        for rekord in generuj_dane():
            writer.writerow(rekord)

    print(f"Utworzono plik: {NAZWA_PLIKU}")
    print(f"Liczba rekordów: {LICZBA_REKORDOW}")


if __name__ == "__main__":
    zapisz_do_csv()
