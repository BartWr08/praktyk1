# Hyper-V

### Instalowanie i uruchamianie Hyper-V na Windows 10
Zacząć trzeba od włączenia wirtualizacji procesora w BIOSie lub UEFI na nowszym sprzęcie.

Aby Hyper-V działało na Windowsie potrzebna jest wersja Pro lub Enterprise.

### Uruchamianie Hyper-V
Uruchom PowerShell jako administrator i wpisz poniższe polecenie. Funkcja zostanie uruchomiona i pojawi się zapytanie o restart systemu. Po restarcie Hyper-V będzie zainstalowane i wystarczy uruchomić menedżer funkcji Hyper-V i zacząć pracę z oprogramowaniem.

*Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All*

### Tworzenie maszyny wirtualnej
1. Pobierz .iso wybranego systemu
2. W menedżerze Hyper-V w okienku po lewej stronie wybierz komputer, następnie wejdź w pasku na górze w akcja, nowa i maszyna wirtualna. Otworzy się kreator nowej maszyny wirtualnej
3. "Dalej", następnie należy nazwać swoją maszynę wirtualną i wybrać folder dla niej, lub zostawić domyślny.
[Hyper-V krok 2 i 3](./hiper1_2.png)
4. Następnie "Dalej" i pojawi się wybór generacji maszyny. Wybierz 1 jeśli system gościa, czyli ten wirtualny, nie obsługuje UEFI, Secure Boot i/lub wymaga MBR. Jeśli sytuacja jest przeciwna to wybierz generację 2, bo szybciej działa, następnie "Dalej".
5. Przydzielanie pamięci początkowej. Pamięć początkowa to ilość pamięci RAM jaką maszyna dostanie przy jej uruchamianiu. Dynamiczna pamięć to przydzielanie z ustawionego zakresu pamięci minimalnej i maksymalnej, wybierz co się podoba, następnie "Dalej".
[Hyper-V krok 4 i 5](./hiper4_5.png)
6. 



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
