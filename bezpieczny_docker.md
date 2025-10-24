# HTTP i HTTPS

**HTTP**

HTTP (Hypertext Transfer Protocol) jest protokołem bezstanowym i nieszyfrowanym, działającym na zasadzie żądanie–odpowiedź:
 - Przeglądarka wysyła żądanie (np. GET lub POST) do serwera.
 - Serwer przetwarza żądanie i odsyła odpowiedź (np. stronę HTML).

Cała komunikacja odbywa się w formie tekstowej. Brak szyfrowania oznacza, że dane mogą zostać:
 - podsłuchane,
 - zmodyfikowane po drodze,
 - wykorzystane przez osoby trzecie.

Domyślny port to :80.

**HTTPS**

HTTPS (HTTP Secure) to HTTP działające przez szyfrowany tunel TLS/SSL. Zapewnia trzy kluczowe właściwości:
 - Poufność danych dzięki szyfrowaniu.
 - Integralność, czyli ochronę przed modyfikacją danych w transmisji.
 - Uwierzytelnienie serwera poprzez certyfikat cyfrowy.

Podczas nawiązywania połączenia wykonywany jest tzw. TLS handshake, podczas którego:
 - przeglądarka weryfikuje certyfikat serwera,
 - uzgadniane są klucze szyfrujące,
 - ustanawiany jest zaszyfrowany kanał komunikacji.

Domyślny port to :443.
