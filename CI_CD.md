# CI/CD

## CI (Continuous Integration — ciągła integracja)
Jest to praktyka polegająca na częstym scalaniu zmian w projekcie i automatycznym ich testowaniu. Umożliwia to wczesne wychwytywanie błędów.
Każda zmiana, którą programista wysyła do repozytorium, może zostać automatycznie:
 - sprawdzona pod kątem poprawności (testy jednostkowe, analiza jakości kodu),
 - zbudowana (np. kompilacja projektu),
 - zweryfikowana, czy nie psuje istniejących funkcjonalności.

**Główny cel to zapobieganie kumulacji błędów i utrzymywanie stabilności projektu.**


## CD (Continuous Delivery/Continuous Deployment — ciągłe dostarczanie / wdrażanie)
To etap po CI, odpowiadający za dostarczanie oprogramowania na środowiska testowe lub produkcyjne.

W tym przypadku mogą być dwa podejścia do działań:
 - Continuous Delivery	- po zatwierdzeniu zmian i przejściu testów, kod jest przygotowany do wdrożenia, ale to człowiek podejmuje decyzję o publikacji.
 - Continuous Deployment - każda poprawna zmiana jest automatycznie wdrażana na produkcję, bez ręcznej ingerencji.

**Główny cel: skracać drogę od napisania kodu do działania u użytkownika.**


