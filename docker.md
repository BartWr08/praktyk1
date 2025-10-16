# Docker na WSL 2
Docker to narzędzie, które pozwala uruchamiać aplikacje w kontenerach – lekkich, odizolowanych środowiskach, które zawierają wszystko, czego program potrzebuje do działania (kod, biblioteki, zależności).
Używa się go gdy potrzebna jest izolacja aplikacji, żeby każda działała niezależnie, uruchamia to samo środowisko na każdym komputerze, czy w chmurze, aplikacja działa "out of the box" czyli bez ręcznej konfiguracji.


**Instalacja i uruchomienie**

1. Ze [strony internetowej][1] pobierz instalator Docker desktop.
2. Uruchom instalator, pojawi się wybór trzech opcji:
   - Use WSL 2 instead of Hyper-V (recommended) - WSL 2 sprawdzi się lepiej w środowisku zwykłego użytkownika, a Hyper-V jest lepsze dla zastosowań korporacyjnych
   - Allow Windows Containers to be used with this installation - uruchamianie na jądrze Windows, powinno być nie zaznaczone przy korzystaniu z WSL 2
   - Add schortcut to desktop - to chyba wiedzą wszyscy, skrót na pulpicie
3. Kliknij *OK* i Docker przystąpi do instalacji. Potem trzeba kliknąć *Close and log out*, Docker wyloguje użytkownika, a po zalogowaniu się uruchomi, trzeba zaakceptować warunki korzystania i wybrać czy będzie to do użytku osobistego czy do pracy.





[1]: https://www.docker.com/get-started/
