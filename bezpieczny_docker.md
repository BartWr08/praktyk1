# HTTP i HTTPS

**HTTP**

HTTP (Hypertext Transfer Protocol) jest protokołem bezstanowym i nieszyfrowanym, działającym na zasadzie żądanie–odpowiedź:
 - Przeglądarka wysyła żądanie (np. GET lub POST) do serwera.
 - Serwer przetwarza żądanie i odsyła odpowiedź (np. stronę HTML).

Cała komunikacja odbywa się w formie tekstowej. Brak szyfrowania oznacza, że dane mogą zostać:
 - podsłuchane,
 - zmodyfikowane po drodze,
 - wykorzystane przez osoby trzecie.

Użycie HTTP może być korzystniejsze w:
 - Lokalnych środowiskach developerskich - aplikacja testowa na localhost bez dostępu do internetu, brak wymogu certyfikatów upraszcza konfigurację.
 - Urządzeniach o bardzo ograniczonych zasobach - niektóre stare moduły IoT lub mikrokontrolery, które nie obsługują TLS z powodu braku mocy obliczeniowej.
 - Sieciach zamkniętych z pełnym zaufaniem - systemy działające wyłącznie w prywatnych, odseparowanych sieciach bez ryzyka podsłuchu (np. część intranetów).
 - Usługach nieprzetwarzających żadnych wrażliwych danych - dostęp do publicznej dokumentacji lub zasobu, do którego każdy i tak ma pełny wgląd.

Domyślny port to :80

**HTTPS**

HTTPS (HTTP Secure) to HTTP działające przez szyfrowany tunel TLS/SSL. Zapewnia trzy kluczowe właściwości:
 - Poufność danych dzięki szyfrowaniu.
 - Integralność, czyli ochronę przed modyfikacją danych w transmisji.
 - Uwierzytelnienie serwera poprzez certyfikat cyfrowy.

Podczas nawiązywania połączenia wykonywany jest tzw. TLS handshake, podczas którego:
 - przeglądarka weryfikuje certyfikat serwera,
 - uzgadniane są klucze szyfrujące,
 - ustanawiany jest zaszyfrowany kanał komunikacji.

Użycie HTTPS będzie korzystniejsze we wszystkich niewymienionych dla HTTP przypadkach, ponieważ jest to preferowana metoda przesyłu danych w sieci, jako bezpieczniejsza i obecnie lepiej optymalizowana. 
Skutkuje to często szybszym działaniem pomimo dodatkowego narzutu szyfrowania i przesyłu certyfikatów

Domyślny port to :443
