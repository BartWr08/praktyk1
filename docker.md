# Docker na WSL (Ubuntu 20.04)
**1. Instalacja:** Wpisz polecenie *sudo apt install docker.io* i Enter, czasem trzeba potwierdzenia (y i Enter), a czasem nie.

**2. Uruchamianie:** Dockera: *sudo dockerd* lub *sudo dockerd $* żeby pracował w tle.
![docker uruchamiany w tle](./docker_WSL_uruch_w_tle.png)
**3. Sprawdzenie:** polecenie *docker run hello-world* pozwala na sprawdzenie czy docker jest poprawnie zainstalowany i działa.
![odpowiedź dockera](./docker_odpowiedź_WSL.png)


# Docker na Ubuntu 22.04 w trybie graficznym w Hyper-V
**1. Instalacja:** Wpisz polecenie *sudo apt install docker.io* i Enter, czasem trzeba potwierdzenia (y i Enter), a czasem nie.

**2. Uruchamianie:** Dockera: *sudo systemctl enable --now docker*, Docker zostanie uruchomiony.

**3. Sprawdzenie:** polecenie *docker run hello-world* pozwala na sprawdzenie czy docker jest poprawnie zainstalowany i działa.

**4. Instalacja pakietu gaficznego:** 
