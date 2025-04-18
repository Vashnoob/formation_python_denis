

## 🔧 STM32 + MicroPython : l’essentiel

### ✅ Ce que tu peux faire :
- Piloter les **GPIO, PWM, ADC**, etc.
- Faire de la **communication série** (UART, I2C, SPI)
- Gérer des **capteurs** et **afficheurs**
- Créer un petit **système embarqué** très réactif, sans écrire une ligne de C

### ❗ À savoir :
MicroPython **n’est pas préinstallé** sur les cartes STM32. Il faut **compiler ou flasher un firmware compatible**.

---

## 🧩 Matériel compatible

MicroPython supporte **officiellement** plusieurs cartes STM32, comme :
- STM32F405 / STM32F407 (ex : Pyboard v1.x)
- STM32F746
- STM32L476 (ultra basse consommation)
- Nucleo boards (selon le MCU)
- Certaines Discovery boards

La plus simple pour commencer : **Pyboard** (créée par les devs de MicroPython)

---

## 🧪 Étapes pour démarrer

### 1. **Télécharge le firmware adapté**

Va sur 👉 [https://micropython.org/download](https://micropython.org/download)  
Choisis **"STM32"**, puis télécharge le `.dfu` ou `.bin` selon ta carte.

---

### 2. **Flashe le firmware**

#### Méthode 1 : avec DFU (si ta carte a un bootloader USB DFU)
```bash
sudo apt install dfu-util
dfu-util -a 0 -D firmware.dfu
```

#### Méthode 2 : avec un ST-Link (et `st-flash`)
```bash
st-flash write firmware.bin 0x08000000
```

> 💡 Les Nucleo boards ont souvent un **ST-Link intégré**, ce qui facilite la tâche.

---

### 3. **Connexion REPL (console interactive)**

- Utilise un terminal série comme `screen`, `minicom`, ou `mpremote`
```bash
mpremote connect /dev/ttyACM0
```

---

### 4. **Ton premier code (GPIO)**

```python
from pyb import Pin
import time

led = Pin('LED', Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
```

> `pyb` est le module spécifique aux cartes STM32 (remplace `machine` dans beaucoup de cas)

---

## 🚀 Quoi faire avec cela ?

- Faire un **petit serveur série** ?
- Lire un capteur analogique ?
- Utiliser les **timers, watchdog, interruptions** ?
- Monter une interface avec écran OLED ou I2C ?
- Compiler ton propre firmware avec des modules spécifiques ?

