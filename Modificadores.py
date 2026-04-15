import pygame
import sys
import time
import random
import os
import math

pygame.init()

ANCHO, ALTO = 800, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

PLAYER_W, PLAYER_H = 80, 120

# =========================
# PARTICULAS
# =========================
class Particula:
    def __init__(self, x, y, color, tipo=None):
        self.x = x
        self.y = y
        self.tipo = tipo

        if tipo == "vel":
            self.dx = random.uniform(-3, -1)
            self.dy = random.uniform(-1, 1)
        else:
            self.dx = random.uniform(-1, 1)
            self.dy = random.uniform(-2, 0)

        self.vida = random.randint(20, 40)
        self.tam = random.randint(3, 6)
        self.color = color

    def actualizar(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.05
        self.vida -= 1

    def dibujar(self, pantalla):
        alpha = int(150 * (self.vida / 40))
        surf = pygame.Surface((self.tam*2, self.tam*2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*self.color, alpha), (self.tam, self.tam), self.tam)
        pantalla.blit(surf, (self.x, self.y))


particulas = []

# =========================
# SPRITES
# =========================
def cortar_spritesheet(img):
    frames = []
    ancho_frame = img.get_width() // 8
    alto_frame = img.get_height()

    for x in range(0, img.get_width(), ancho_frame):
        frame = pygame.Surface((ancho_frame, alto_frame), pygame.SRCALPHA)
        frame.blit(img, (0, 0), (x, 0, ancho_frame, alto_frame))
        frame = pygame.transform.scale(frame, (PLAYER_W, PLAYER_H))
        frames.append(frame)

    return frames

def cargar_animacion(ruta):
    return cortar_spritesheet(pygame.image.load(ruta).convert_alpha())

# =========================
# FONDO
# =========================
fondo = pygame.image.load("assets/background/fondo.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# =========================
# ITEMS IMAGENES
# =========================
img_vel = pygame.transform.scale(pygame.image.load("assets/items/vel.png").convert_alpha(), (40,40))
img_salto = pygame.transform.scale(pygame.image.load("assets/items/salto.png").convert_alpha(), (40,40))
img_escudo = pygame.transform.scale(pygame.image.load("assets/items/escudo.png").convert_alpha(), (40,40))

# =========================
# JUGADOR
# =========================
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vel = 5
        self.vel_base = 5
        self.salto = -12
        self.salto_base = -12

        self.dy = 0
        self.gravedad = 0.5
        self.en_suelo = True

        self.rect = pygame.Rect(x, y, PLAYER_W, PLAYER_H)

        base = os.path.dirname(__file__)

        self.animaciones = {
            "idle": cargar_animacion(os.path.join(base, "assets/player/Idle.png")),
            "walk": cargar_animacion(os.path.join(base, "assets/player/Walk.png")),
            "run": cargar_animacion(os.path.join(base, "assets/player/Run.png")),
            "jump": cargar_animacion(os.path.join(base, "assets/player/Jump.png"))
        }

        self.estado = "idle"
        self.frame = 0
        self.tiempo_anim = 0
        self.vel_anim = 0.2

        self.flip = False
        self.corriendo = False

    def mover(self, teclas):
        moviendo = False

        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
            self.flip = True
            moviendo = True

        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
            self.flip = False
            moviendo = True

        if self.x > ANCHO:
            self.x = -PLAYER_W
        if self.x < -PLAYER_W:
            self.x = ANCHO

        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.dy = self.salto
            self.en_suelo = False

        if not self.en_suelo:
            self.estado = "jump"
        elif moviendo:
            self.estado = "run" if self.corriendo else "walk"
        else:
            self.estado = "idle"

    def actualizar(self):
        self.dy += self.gravedad
        self.y += self.dy

        if self.y >= ALTO - PLAYER_H:
            self.y = ALTO - PLAYER_H
            self.dy = 0
            self.en_suelo = True

        self.rect.topleft = (self.x, self.y)

        self.tiempo_anim += self.vel_anim
        if self.tiempo_anim >= 1:
            self.tiempo_anim = 0
            self.frame = (self.frame + 1) % len(self.animaciones[self.estado])

    def dibujar(self, pantalla):
        img = self.animaciones[self.estado][self.frame]
        if self.flip:
            img = pygame.transform.flip(img, True, False)
        pantalla.blit(img, (self.x, self.y))

# =========================
# MODIFICADORES
# =========================
class Modificador:
    def __init__(self, duracion):
        self.inicio = time.time()
        self.duracion = duracion
        self.color = (255,255,255)

    def activo(self):
        return time.time() - self.inicio < self.duracion

    def aplicar(self, jugador):
        pass


class VelocidadBoost(Modificador):
    def __init__(self, duracion):
        super().__init__(duracion)
        self.color = (120,220,120)

    def aplicar(self, jugador):
        jugador.vel += 4
        jugador.corriendo = True

        for _ in range(3):
            px = jugador.x + PLAYER_W // 2
            py = jugador.y + PLAYER_H
            particulas.append(Particula(px, py, self.color, "vel"))


class SaltoBoost(Modificador):
    def __init__(self, duracion):
        super().__init__(duracion)
        self.color = (120,170,255)

    def aplicar(self, jugador):
        jugador.salto -= 5

        for _ in range(2):
            px = jugador.x + PLAYER_W // 2
            py = jugador.y + PLAYER_H
            particulas.append(Particula(px, py, self.color))


class Escudo(Modificador):
    def __init__(self, duracion):
        super().__init__(duracion)
        self.color = (255,255,150)

    def aplicar(self, jugador):
        for _ in range(2):
            px = jugador.x + random.randint(0, PLAYER_W)
            py = jugador.y + random.randint(0, PLAYER_H)
            particulas.append(Particula(px, py, self.color))


# =========================
# ITEMS FLOTANTES
# =========================
class Item:
    def __init__(self, x, y, tipo):
        self.tipo = tipo
        self.img = img_vel if tipo == "vel" else img_salto if tipo == "salto" else img_escudo

        self.base_y = y
        self.x = x
        self.tiempo = random.uniform(0, 2)

        self.rect = self.img.get_rect(topleft=(x, y))

    def actualizar(self):
        self.tiempo += 0.1
        offset = 5 * math.sin(self.tiempo)
        self.rect.topleft = (self.x, self.base_y + offset)

    def dibujar(self):
        pantalla.blit(self.img, self.rect.topleft)


def generar_item(jugador):
    while True:
        x = random.randint(0, ANCHO - 40)
        y = ALTO - 40
        rect = pygame.Rect(x, y, 40, 40)

        if not rect.colliderect(jugador.rect):
            return Item(x, y, random.choice(["vel", "salto", "escudo"]))


# =========================
# UI BARRAS
# =========================
def dibujar_barras(mods):
    x = 10
    for m in mods:
        tiempo = max(0, m.duracion - (time.time() - m.inicio))
        ancho = int((tiempo / m.duracion) * 100)

        pygame.draw.rect(pantalla, (255,255,255), (x, 10, 100, 10), 1)
        pygame.draw.rect(pantalla, m.color, (x, 10, ancho, 10))

        x += 120


# =========================
# MAIN
# =========================
jugador = Jugador(100, 300)
mods = []
items = []

tiempo_spawn = 0
intervalo_spawn = 3
max_items = 5

ejecutando = True

while ejecutando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    jugador.vel = jugador.vel_base
    jugador.salto = jugador.salto_base
    jugador.corriendo = False

    mods = [m for m in mods if m.activo()]
    for m in mods:
        m.aplicar(jugador)

    jugador.mover(teclas)
    jugador.actualizar()

    ahora = time.time()
    if ahora - tiempo_spawn > intervalo_spawn:
        if len(items) < max_items:
            items.append(generar_item(jugador))
        tiempo_spawn = ahora

    pantalla.blit(fondo, (0, 0))

    jugador.dibujar(pantalla)

    # PARTICULAS
    for p in particulas[:]:
        p.actualizar()
        if p.vida <= 0:
            particulas.remove(p)
        else:
            p.dibujar(pantalla)

    # ITEMS
    for item in items[:]:
        item.actualizar()

        if jugador.rect.colliderect(item.rect):
            if item.tipo == "vel":
                mods.append(VelocidadBoost(5))
            elif item.tipo == "salto":
                mods.append(SaltoBoost(5))
            elif item.tipo == "escudo":
                mods.append(Escudo(5))
            items.remove(item)

        item.dibujar()

    dibujar_barras(mods)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()