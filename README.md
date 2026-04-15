Juego 2D en Pygame (Patrón Decorator)
integrantes:

Sebastián Jaramillo Hernández - 20241020002
Jhoe Luis Jeanpaul Miranda Alvarez - 20241020022

Este programa implementa un juego 2D desarrollado en Python utilizando la librería Pygame y el patrón de diseño Decorator para aplicar modificadores dinámicos a un personaje.

El jugador puede moverse, saltar y recoger potenciadores que alteran su comportamiento en tiempo real, como aumento de velocidad, mejora de salto o activación de un escudo. El sistema permite que estos efectos se apliquen y se eliminen automáticamente después de cierto tiempo sin modificar la estructura base del personaje.

El juego incluye animaciones con spritesheets, partículas dinámicas, efectos visuales, interfaz gráfica con barras de duración y objetos interactivos que aparecen aleatoriamente en el mapa.

Cómo usarlo:
Ejecuta python main.py.
Usa la flecha izquierda y derecha para moverte.
Presiona la barra espaciadora para saltar.
Recoge los objetos que aparecen en el mapa para activar modificadores.
Observa las barras en la parte superior para ver la duración de cada efecto.

Controles:
Flecha izquierda → mover a la izquierda
Flecha derecha → mover a la derecha
Espacio → saltar

Características principales:

* Animaciones del personaje (idle, caminar, correr y salto) usando spritesheets de 8 frames
* Sistema de modificadores implementado con el patrón Decorator
* Potenciadores:

  * Velocidad (aumenta movimiento y activa animación de correr)
  * Salto (incrementa la altura del salto)
  * Escudo (efecto visual de protección)
* Sistema de partículas dinámico:

  * Partículas en los pies del personaje
  * Colores suaves con desvanecimiento progresivo
  * Movimiento realista (dirección y gravedad)
* Interfaz (HUD):

  * Barras de duración de cada modificador
  * Colores según el tipo de potenciador
* Items:

  * Aparición aleatoria en el mapa
  * Animación flotante (movimiento senoidal)
  * Activación mediante colisión
* Mundo:

  * Plataforma única en el suelo
  * Movimiento horizontal continuo (wrap-around)

Estructura del proyecto:
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

Tecnologías utilizadas:

* Python 3
* Pygame

Patrón de diseño utilizado:
El patrón Decorator permite añadir funcionalidades al personaje de forma dinámica sin modificar su clase base. Cada modificador actúa como una extensión temporal que cambia atributos como velocidad o salto y añade efectos visuales, manteniendo el código modular y escalable.

Cómo ejecutar el proyecto:

1. Clona el repositorio
2. Instala Pygame con pip install pygame
3. Ejecuta python main.py

Posibles mejoras futuras:

* Enemigos con inteligencia artificial
* Sonido y música
* Fondo con efecto parallax
* Menú de inicio y pausa
* Efectos visuales avanzados (humo, fuego, partículas con imágenes)

Este proyecto fue desarrollado con fines académicos para aplicar conceptos de programación orientada a objetos, desarrollo de videojuegos 2D y patrones de diseño.

---
