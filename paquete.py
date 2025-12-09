import pyxel
import constantes


class Paquete:
    def __init__(self):
        # El paquete nace en la cinta 0 (Piso 0, lado Mario)
        self.cinta_actual = 0
        self.activo = True
        self.configurador_paquetes()

    def configurador_paquetes(self):
        # Determinar dirección y posición Y según la cinta actual
        self.y = constantes.ALTURAS_CINTAS[self.cinta_actual]

        # Lógica de Zig-Zag:
        # Pares (0, 2, 4) -> Van a la DERECHA (hacia Mario)
        # Impares (1, 3, 5) -> Van a la IZQUIERDA (hacia Luigi)
        if self.cinta_actual % 2 == 0:
            self.x = 20  # Empieza a la izquierda, va a derecha
            self.direccion = 1
        else:
            self.x = constantes.ANCHO_PANTALLA - 30  # Empieza derecha, va a izq
            self.direccion = -1

    def subir(self):
        # Pasa a la siguiente cinta
        self.cinta_actual += 1
        self.configurador_paquetes()

    def update(self):
        self.x += (constantes.VELOCIDAD_PAQUETE * self.direccion)

        # Matar paquete si se sale de pantalla (por seguridad)
        if self.x > 270 or self.x < -20:
            self.activo = False

    def draw(self):
        if self.activo:
            b, u, v, w, h, k = constantes.SPRITE_CAJA
            pyxel.blt(self.x, self.y, b, u, v, w, h, k)