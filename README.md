# 🎮 Juego 2D en Pygame con Patrón Decorator

Este proyecto es un juego 2D desarrollado en **Pygame** que implementa el **patrón de diseño Decorator** para gestionar modificadores dinámicos sobre un personaje.

El jugador puede moverse, saltar, recoger potenciadores y experimentar efectos visuales avanzados como partículas, animaciones y feedback visual en tiempo real.

---

## 🚀 Características

* 🧍‍♂️ Personaje con animaciones:

  * Idle (inactivo)
  * Walk (caminar)
  * Run (correr con boost)
  * Jump (salto)

* ⚡ Sistema de modificadores (Decorator):

  * Velocidad
  * Salto
  * Escudo

* 🎨 Efectos visuales:

  * Sistema de partículas dinámico
  * Efectos en los pies del personaje
  * Colores suaves y desvanecimiento (fade out)

* 🟩 Interfaz (HUD):

  * Barras de duración de modificadores
  * Colores según el tipo de potenciador

* 🎁 Items:

  * Aparición aleatoria en el mapa
  * Animación flotante (movimiento senoidal)
  * Activación por colisión

* 🌍 Mundo:

  * Plataforma única
  * Movimiento horizontal con "wrap-around" (sale por un lado y entra por el otro)

---

## 🧠 Patrón Decorator

El patrón Decorator permite añadir funcionalidades al jugador dinámicamente sin modificar su clase base.

Ejemplo:

* `VelocidadBoost` aumenta la velocidad
* `SaltoBoost` modifica el salto
* `Escudo` agrega efectos visuales y protección

Cada modificador:

* Tiene duración
* Se aplica en tiempo real
* Se elimina automáticamente al expirar

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Pygame

---

## 📁 Estructura del proyecto

```
proyecto/
│
├── main.py
├── assets/
│   ├── player/
│   │   ├── Idle.png
│   │   ├── Walk.png
│   │   ├── Run.png
│   │   └── Jump.png
│   │
│   ├── items/
│   │   ├── vel.png
│   │   ├── salto.png
│   │   └── escudo.png
│   │
│   └── background/
│       └── fondo.png
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
```

2. Instala Pygame:

```bash
pip install pygame
```

3. Ejecuta el juego:

```bash
python main.py
```

---

## 🎮 Controles

* ⬅️ Flecha izquierda → Moverse a la izquierda
* ➡️ Flecha derecha → Moverse a la derecha
* ␣ Espacio → Saltar

---

## ✨ Mejoras implementadas

* Sistema de partículas realista
* Animaciones con spritesheets (8 frames)
* Items con movimiento flotante
* HUD dinámico con colores
* Código modular y escalable

---

## 🚧 Posibles mejoras futuras

* 👾 Enemigos con IA
* 🎵 Sonido y música
* 🌄 Fondo con parallax
* 🎮 Menú de inicio y pausa
* 💥 Efectos avanzados (humo, fuego)

---

## 📸 Demo

*(Puedes agregar aquí un GIF o imagen del juego)*

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.

---

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje aplicando:

* Programación en Python
* Desarrollo de videojuegos 2D
* Patrones de diseño (Decorator)

---
