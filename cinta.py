import pyxel
import constantes


class Cinta:
    def __init__(self, x, y, longitud):
        self.x = x
        self.y = y
        self.longitud = longitud

    def draw(self):
        # Dibujar sprite repetido
        b, u, v, w, h, k = constantes.SPRITE_CINTA
        num_bloques = self.longitud // 8

        for i in range(num_bloques):
            pyxel.blt(self.x + (i * 8), self.y, b, u, v, w, h, k)