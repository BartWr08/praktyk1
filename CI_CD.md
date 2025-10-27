# CI/CD

### Modele
1. CI - integracja
2. CD - dostarczanie
3. CD - wdrażanie

**Inne modele, niebędące formalnymi modelami CI/CD, istniejące w praktyce**
1. Blue-Green Deployment - to dwie identyczne produkcje, ruch jest przełączany między nimi, minimalizuje przestoje.
2. Canary Releases - wdrażanie do małej grupy użytkowników, stopniowe testowanie zmian.
3. Feature Flags - funkcje ukryte do czasu aktywacji, częste wdrożenia bez ujawniania niedokończonych funkcji.
4. Progressive Delivery - połączenie canary + feature flags, kontrolowane ryzyko, skalowalne wydania.


### CI (Continuous Integration — ciągła integracja)
Jest to praktyka polegająca na częstym scalaniu zmian w projekcie i automatycznym ich testowaniu. Umożliwia to wczesne wychwytywanie błędów.
Każda zmiana, którą programista wysyła do repozytorium, może zostać automatycznie:
 - sprawdzona pod kątem poprawności (testy jednostkowe, analiza jakości kodu)
 - zbudowana (np. kompilacja projektu)
 - zweryfikowana, czy nie psuje istniejących funkcjonalności

**Główny cel to zapobieganie kumulacji błędów i utrzymywanie stabilności projektu.**


### CD (Continuous Delivery/Continuous Deployment — ciągłe dostarczanie / wdrażanie)
To etap po CI, odpowiadający za dostarczanie oprogramowania na środowiska testowe lub produkcyjne.

W tym przypadku mogą być dwa podejścia do działań:
 - Continuous Delivery	- po zatwierdzeniu zmian i przejściu testów, kod jest przygotowany do wdrożenia, ale to człoiek podejmuje decyzję o publikacji
 - Continuous Deployment - każda poprawna zmiana jest automatycznie wdrażana na produkcję, bez ręcznej ingerencji

**Główny cel: skracać drogę od napisania kodu do działania u użytkownika.**


### CI/CD na GitHubie
GitHub dostarcza własną platformę automatyzacji: GitHub Actions.

Pozwala ona na tworzenie przepływów pracy (workflow), które uruchamiają się automatycznie przy określonych zdarzeniach, np.:
 - push do repozytorium
 - pull request
 - publikacja wydania (release)
 - zaplanowany czas (np. codziennie o północy)

Workflowy działają na podstawie tzw. akcji, czyli gotowych lub własnych kroków automatyzacji.


### Przykłady zastosowania CI/CD na GitHubie

1. Projekt webowy / aplikacja frontendowa:
   - Każda zmiana w kodzie Reacta jest testowana
   - automatycznie budowana wersja podglądowa
   - po zatwierdzeniu kodu — strona jest publikowana na hostingu (np. GitHub Pages, Vercel)

Taki zestaw działań umożliwia wykrycie błędów zanim trafią do użytkowników.

2. Biblioteka lub pakiet open-source:
   - Gdy nowa wersja jest „wydana” (release)
   - automatycznie generowane są pakiety instalacyjne
   - publikacja w repozytoriach takich jak npm, PyPI czy Maven Central

Dzięki temu użytkownicy mają od razu dostęp do najnowszej wersji.

3. Aktualizacja dokumentacji:
   - Zmiana dokumentacji
   - automatyczna generacja przez system nowej strony dokumentacji
   - automatyczna jej publikacja

Zapewnia to stałą aktualność dokumentacji


