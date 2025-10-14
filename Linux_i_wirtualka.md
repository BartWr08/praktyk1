# Hyper-V

### Instalowanie i uruchamianie Hyper-V na Windows 10
Zacząć trzeba od włączenia wirtualizacji procesora w BIOSie lub UEFI na nowszym sprzęcie.

Aby Hyper-V działało na Windowsie potrzebna jest wersja Pro lub Enterprise.

### Uruchamianie Hyper-V
Uruchom PowerShell jako administrator i wpisz poniższe polecenie. Funkcja zostanie uruchomiona i pojawi się zapytanie o restart systemu. Po restarcie Hyper-V będzie zainstalowane i wystarczy uruchomić menedżer funkcji Hyper-V i zacząć pracę z oprogramowaniem.

*Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All*

### Tworzenie maszyny wirtualnej
1. Wybierz w polu po lewej stronie komputer na którym ma być utworzona maszyna.
2. Następnie po prawej stronie szybkie tworzenie.
3. Wybierz system jaki chcesz zainstalować, a program zrobi resztę. Zalecam skontrolowanie parametrów jakie dostała maszyna, czy zgadzają się z możliwościami komputera i czy na pewno pozwolą na swobodną pracę wirtualnego systemu.
4. Potem wybierz połącz i uruchom maszynę.
5. Po uruchomieniu będzie potrzebna konfiguracja wstępna i instalacja.
6. System powinien działać poprawnie, z dostępem do internetu.

# Linux

Linux jest rodziną systemów operacyjnych opartych na jądrze Linux. Są one darmowe i otwartoźródłowe. Używane w serwerach, komputerach osobistych i urządzeniach mobilnych (Android).

**Główne distra Linuxa**
1. Debian - stawia na stabilność i bezpieczeństwo, ma wolniejsze ale dokładniejsze aktualizacje, jest popularny w serwerach i jako baza dla innych distr.
2. Arch Linux - rolling release (ciągłe aktualizacje), użytkownik sam składa system (dla doświadczonych osób), dokumentacja (Arch Wiki) jest bardzo rozbudowana.
3. openSUSE - ma dwa warianty: Leap jest stabilny i Tubleweed, który jest na rolling release, do zarządzania systemem używa się narzędzia YaST.
4. Red Hat Enterprise Linux (RHEL) / CentOS / AlmaLinux / Rocky Linux - Przeznaczony dla serwerów, ma zapewniony długi cykl wsparcia.
5. Ubuntu - najbardziej przyjazne dla początkujących, zbudowane na Debianie, ma duże wsparcie społeczności i firm.
6. Mint - oparty na Ubuntu, wygląd pulpitu częściowo podobny do Windowsa poprzez użycie nakładki graficznej (cinnamon), co powoduje że najłatwiej się na niego przesiąść z Windowsa.
7. Fedora - świerze oprogramowanie, wspierane przez Red Hat, dobry dla deweloperów i testowania nowości.


# Ubuntu 22.04 LTS z nakładką graficzną
LTS (Long-Term Support) oznacza długie wsparcie, dla tej wersji jest to do 2027 roku, która fuckcjonuje już od roku 2022.

Jest to system stabilny, nadający się jako system serwerowy lub konsumencki. Może on działać z nakładką graficzną (w tym przypadku GNOME 42), która ma tradycyjny wygląd pulpitu.

Ubuntu 22.04 jest dobrym rozwiązaniem dla osób zaczynających działania z Linuxem, dla osób które chcą mieć stabilny system bez częstych reinstalacji.

### Podstawowe komendy
- sudo su - nadaje użytkownikowi uprawnienia roota, czyli może on po tym zrobic absolutnie wszystko co da się zrobić z systemem
- cd / - przenosi do folderu domowego, cd/*nazwa folderu* przenosi do kolejnego katalogu
- ls, ls -l - pokazuje zawartość katalogu, pokazuje szczegółową zawartość katalogu z uprawnieniami
- pwd - pokazuje bierzący katalog
- mkdir *nazwa* tworzy katalog o określonej nazwie
- rm - usuwa pliki (rm *nazwa pliku*) lub katalogi wraz z ich zawartością (rm -r *nazwa katalogu*)
- cp - kopiowanie pliku lub katalogu (cp *źródło* *cel*), można też kopiować plik w tym samym katalogu (cp *nazwa pliku* *nowa nazwa pliku*)
- mv - przenoszenie plików lub katalogów (mv *źródło* *cel*), lub zmiana nazwy pliku lub katalogu (mv *nazwa pliku* *nowa nazwa pliku*)
- uname -a - pokazuje informacje o systemie
- df -h - pokazuje miejsce na dyskach w czytelny i przejrzysty sposób
- free -h - pokazuje użycie pamięci RAM
- top - monitor procesów w czasie rzeczywistym
- uptime - pokazuje obciążenie CPU i czas pracy systemu
- sudo apt update - odświeża listę pakietów do aktualizacji
- sudo apt upgrade/full-upgrade - aktualizuje zainstalowane pakiety
- sudo apt install *nazwa pakietu* - instaluje pakiet o określonej nazwie
- sudo apt remove *nazwa pakietu* - odinstalowywuje pakiet o określonej nazwie
- sudo apt autoremove - usuwa starsze wersje pakietu i pliki instalacyjne
- apt list --upgradable - wyświetla wszystkie pakiety które można zaktualizować
- man *komenda* - pokazuje instrukcję użycia danej komendy
- cat *nazwa pliku* - wyświetla zawartość pliku
- nano *nazwa pliku* - otwiera plik w prostym edytorze tekstu
- shutdown now - wyłącza system natychmiast

### Instalacja przykładowej aplikacji (VLC media player)
1. Wpisz komendę *sudo snap install VLC*
2. Poczekaj
3. Wpisz *vlc* i aplikacja się uruchomi.

Jest to prosta metoda instalowania wielu programów, np. VS Code wymaga odświeżenia pakietów, dodania klucza GPG od Microsoftu, dodania repozytorium VS Code, odświerzenia pakietów i wtedy da się instalować (standardowa metoda poporzez *sudo apt install*)

Za to *sudo snap install code --classic* pozwoli na łatwe i bezproblemowe zainstalowanie VS Code.

Na uruchomienie wystarczy tylko wpisać *code* i [będzie działać](./VSC_linux.png)

*sudo snap remove code* - odinstalowywuje VS Code

### Tworzenie, przenoszenie, edycja plików tekstowych.
1. Konemdą *cd /* udajemy się do katalodu głównego
2. Tam za pomocą *mkdir projekty* tworzymy katalog "projekty"
3. cd projekty przenosi nas do tego katalogu
4. Komendą *touch notatka.txt* tworzymy [plik tekstowy](przed_edycja.png)
5. *nano notatka.txt* otwiera plik w [edytorze tekstu](./edytor.png), zamyka się crtl+x, a potem trzeba potwierdzić zapisanie lub odrzucenie zmian w pliku



