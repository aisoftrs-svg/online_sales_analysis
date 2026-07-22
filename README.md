# Online Sales Analysis

Ovaj projekat predstavlja sistem za analizu i upravljanje prodajnim podacima u online prodavnici, razvijen u Pythonu uz korišćenje OOP koncepata i Git-a za verzionisanje koda.

## Struktura i Klase

* **`Product`** (`product.py`): Modeluje pojedinačni proizvod sa atributima (naziv, cena, količina) i metodama za prikaz i ažuriranje količine.
* **`ProductManager`** (`product_manager.py`): Upravlja listom svih proizvoda u inventaru (dodavanje, uklanjanje, prikaz i izračunavanje ukupne vrednosti inventara).
* **`Cart`** (`cart.py`): Modeluje kupčevu korpu, omogućava dodavanje proizvoda, prikaz sadržaja i izračunavanje ukupnog iznosa za naplatu.
* **`main.py`**: Glavna skripta koja demonstrira rad svih funkcionalnosti.

## Podešavanje i Pokretanje

Pokretanje glavne skripte:
```bash
python main.py