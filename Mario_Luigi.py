import pyxel
import constantes

class Personaje:
    def __init__(self, x, y, teclas, nombre):
        self.x = x
        self.y = y
        self.teclas = teclas
        self.nombre = nombre
        # Sprites
        if nombre == "Mario":
            self.sprite = constantes.SPRITE_MARIO
            self.direccion = -1 # Mira a izq
        else:
            self.sprite = constantes.SPRITE_LUIGI
            self.direccion = 1 # Mira a der

    @property
    def piso_actual(self):
        # Definimos zonas de altura
        # Arriba (Piso 2) aprox Y=70-80
        # Medio (Piso 1) aprox Y=130-140
        # Abajo (Piso 0) aprox Y=190-200
        if self.y < 100: return 2
        if self.y < 160: return 1
        return 0

    def update(self):
        # Movimiento entre pisos (saltos de 60px)
        if pyxel.btnp(self.teclas[0]): # ARRIBA
            if self.piso_actual < 2:
                self.y -= 60
        if pyxel.btnp(self.teclas[1]): # ABAJO
            if self.piso_actual > 0:
                self.y += 60

    def draw(self):
        b, u, v, w, h, k = self.sprite
        # Espejo si es necesario
        ancho = w if self.direccion == 1 else -w
        pyxel.blt(self.x, self.y, b, u, v, ancho, h, k)