---
## 🔍 C’est quoi MicroPython ?

**MicroPython** est une version **allégée de Python 3**, conçue pour tourner sur des **microcontrôleurs** : des petits ordinateurs comme l’ESP32, l’ESP8266, le Raspberry Pi Pico, etc.

✅ Avantages :
- On code en Python, pas en C !
- Léger, rapide, interactif
- Super pour des projets embarqués, IoT, robotique…

---

## ⚙️ Matériel de base

### Tu peux démarrer avec :
- **ESP32** ou **ESP8266** (cartes Wi-Fi)
- **Raspberry Pi Pico** (USB, pas de Wi-Fi mais très stable)
- Câble USB (données, pas juste recharge !)
- Une LED + une résistance pour ton premier test

---

## 💻 Installer MicroPython

### 1. **Flasher MicroPython sur ta carte**
Le firmware MicroPython est un `.uf2` ou `.bin`.

- Pour un **Raspberry Pi Pico** :
  1. Appuie sur BOOTSEL et branche-le en USB
  2. Glisse le fichier `.uf2` [depuis le site officiel](https://micropython.org/download/rp2-pico/) dessus

- Pour un **ESP32/ESP8266** :
  - Télécharge le firmware `.bin` sur [https://micropython.org/download](https://micropython.org/download/)
  - Utilise `esptool` :
    ```bash
    pip install esptool
    esptool.py --port /dev/ttyUSB0 erase_flash
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmware.bin
    ```

---

## 🧪 Écrire ton premier programme

Tu peux utiliser :
- **Thonny IDE** (ultra simple, recommandé pour débuter)
- Ou des outils comme `mpremote` :
  ```bash
  mpremote connect /dev/ttyUSB0 repl
  ```

### Code de base (LED clignotante) :

```python
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)  # Pour Raspberry Pi Pico

while True:
    led.toggle()
    sleep(0.5)
```

---

## 🛠️ Quelques modules de base

| Module         | Utilité                         |
|----------------|----------------------------------|
| `machine`      | Accès au matériel (GPIO, PWM…)   |
| `time`         | Delais, timing                   |
| `network`      | Gérer le Wi-Fi                   |
| `urequests`    | Requêtes HTTP                    |
| `dht`          | Capteur de température/humidité  |
| `ssd1306`      | Écran OLED I2C                   |

---

Tu veux que je t’aide à :
- Choisir une carte pour commencer ?
- Préparer ton environnement ?
- Faire un premier petit projet (genre serveur web, LED, capteur) ?
