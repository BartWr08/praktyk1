# Hyper-V

### Instalowanie i uruchamianie Hyper-V na Windows 10
Zacząć trzeba od włączenia wirtualizacji procesora w BIOSie lub UEFI na nowszym sprzęcie.

Aby Hyper-V działało na Windowsie potrzebna jest wersja Pro lub Enterprise.

### Uruchamianie Hyper-V
Uruchom PowerShell jako administrator i wpisz poniższe polecenie. Funkcja zostanie uruchomiona i pojawi się zapytanie o restart systemu. Po restarcie Hyper-V będzie zainstalowane i wystarczy uruchomić menedżer funkcji Hyper-V i zacząć pracę z oprogramowaniem.

*Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All*

### Tworzenie maszyny wirtualnej
1. Wybierz w polu po lewej stronie komputer na którym ma być utworzona maszyna
2. Następnie po prawej stronie szybkie tworzenie
3. Wybierz system jaki chcesz zainstalować, a program zrobi resztę. Zalecam skontrolowanie parametrów jakie dostała maszyna, czy zgadzają się z możliwościami komputera i czy na pewno pozwolą na swobodną pracę wirtualnego systemu


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


# Ubuntu 22.04
