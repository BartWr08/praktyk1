# Docker przez Portainer

### Tworzenie prostego kontenera

1. Menu -> Containers -> Add container.

![menu główne](./prosta_metoda1.png)

2. Podaj Name (np. my-nginx), w polu Image wpisz nginx:latest.

![nazwa i silnik](./prosta_metoda2.png)

3. W Advanced container settings -> Ports -> dodaj mapping, np. Host: 8080 -> Container: 80.

![port sieci](./prosta_metoda3.png)

4. Kliknij Deploy the container.
5. Otwarte http://<IP_VM>:8080 pokaże Nginx.

![działający kontener](./nginx(4).png)
