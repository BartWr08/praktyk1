## pierwszy problem
![reset połączenia](./connection_reset.png)

Udało się określić że występuje gdy port jest ustawiony na inny niż 8080:80.

Po ustawieniu takiego portu pojawia się standardowe powitanie Nginx:

![](./powitanie.png)

## Web Editor.
Web Editor to wbudowany edytor tekstowy w interfejsie Portainera, który służy do wprowadzania (pisania lub wklejania) pliku docker-compose.yml, czyli definicji całej aplikacji (stacka). Pozwala na:
   - napisać lub wkleić kod docker-compose.yml, który opisuje, jakie kontenery mają się uruchomić, z jakich obrazów, na jakich portach, z jakimi zmiennymi środowiskowymi itp.
   - następnie po kliknięciu Deploy the stack, Portainer:
      1. odczytuje ten plik YAML,
      2. uruchamia wszystkie kontenery i sieci zgodnie z definicją,
      3. monitoruje je jako jeden stack (czyli grupę usług).
   - w skrócie Web Editor to miejsce w którym się definiuje aplikacje złożone z jednego lub wielu kontenerów.

## Tworzenie Stack w Web Editor
Objaśnienia pod zdjęciem.


Ucięte na samej górze kodu: *version: "3.8"*
![](./create_stack.png)

**version: "3.8"**

To wersja składni docker-compose. 3.8 to nowoczesna wersja kompatybilna z większością aktualnych Dockerów i Portainerów. Nie wpływa na działanie, ale określa dostępne funkcje (np. depends_on, volumes, networks).

**services:**

Sekcja services definiuje, jakie kontenery będą uruchamiane w ramach aplikacji.

Każdy service = jeden kontener (lub replika).

W tym przykładzie są dwa serwisy:
 - web (Nginx) - obraz sieci
 - db (PostgreSQL) - baza danych



