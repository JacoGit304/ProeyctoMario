import pyxel
import constantes


class Camion:
    def __init__(self):
        self.x, self.y = constantes.POS_CAMION
        self.paquetes = 0
        self.en_reparto = False
        self.tiempo_salida = 0
        self.paquetes_necesarios = 8

    def recibir(self):
        self.paquetes += 1
        # Si llega a 8 paquetes, se va a reparto
        if self.paquetes >= self.paquetes_necesarios:
            self.en_reparto = True
            self.tiempo_salida = pyxel.frame_count

    def update(self):
        if self.en_reparto:
            # Lógica de movimiento: se mueve a la izquierda para "irse"
            self.x -= 2

            # Reparto de 4 segundos (240 frames) [cite: 59]
            if pyxel.frame_count - self.tiempo_salida > 240:
                self.en_reparto = False
                self.paquetes = 0
                self.x = constantes.POS_CAMION[0]  # Vuelve a posición original
                return True  # Retorna True para sumar los +10 puntos en Tablero
        else:
            # Asegura que esté en posición esperando
            self.x = constantes.POS_CAMION[0]
        return False


    def draw(self):
        # Solo dibujar si no se ha ido demasiado lejos (si no está muy avanzado en el reparto)
        if self.x > -50:
            b, u, v, w, h, k = constantes.SPRITE_CAMION
            # Ajuste visual para que la caja parezca caer en la plataforma del camión
            pyxel.blt(self.x, self.y, b, u, v, w, h, k)

        # Muestra el contador de paquetes
        if not self.en_reparto:
            pyxel.text(self.x + 15, self.y + 10, f"{self.paquetes}/8", 7)