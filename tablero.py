import pyxel
import constantes
from cinta import Cinta
from Mario_Luigi import Personaje
from paquete import Paquete
from camion import Camion  # Asegúrate de importar esto


class Tablero:
    def __init__(self):
        pyxel.init(constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA, title=constantes.TITULO)
        pyxel.load("lienzo_definitivo.pyxres")

        # Generar Cintas visuales
        self.cintas = []
        for i in range(constantes.NUM_CINTAS):
            y = constantes.ALTURAS_CINTAS[i] + 16  # Ajuste visual bajo la caja
            # Dibujamos cintas largas
            nueva_cinta = Cinta(0, y, constantes.ANCHO_PANTALLA)
            self.cintas.append(nueva_cinta)

        # Personajes
        teclas_mario = [pyxel.KEY_UP, pyxel.KEY_DOWN]
        teclas_luigi = [pyxel.KEY_W, pyxel.KEY_S]

        # Posiciones iniciales (Piso 0)
        self.mario = Personaje(220, 190, teclas_mario, "Mario")
        self.luigi = Personaje(20, 190, teclas_luigi, "Luigi")
        self.camion = Camion()

        self.paquetes = []
        self.puntos = 0
        self.fallos = 0
        self.muerto = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): pyxel.quit()

        if not self.muerto:
            self.mario.update()
            self.luigi.update()

            # El camión se va y vuelve
            puntos_camion = self.camion.update()
            if puntos_camion:
                self.puntos += 10  # Bonus por camión lleno

            # Generar paquetes solo si el camión NO está repartiendo
            if not self.camion.en_reparto:
                if pyxel.frame_count % constantes.FRECUENCIA_APARICION == 0:
                    self.paquetes.append(Paquete())

            for paquete in self.paquetes:
                if paquete.activo:
                    paquete.update()
                    self.verificar_colision(paquete)

            # Limpiar paquetes inactivos
            self.paquetes = [p for p in self.paquetes if p.activo]

            if self.fallos >= constantes.FALLOS:
                self.muerto = True

    def verificar_colision(self, paquete):
        # 1. Detectar si llegó al final de su cinta
        llego_final = False
        personaje_encargado = None

        # Si la cinta es PAR (0, 2) -> Va hacia Mario (Derecha)
        if paquete.cinta_actual % 2 == 0:
            if paquete.x > 210:  # Limite derecho
                llego_final = True
                personaje_encargado = self.mario

        # Si la cinta es IMPAR (1, 3, 5) -> Va hacia Luigi (Izquierda)
        else:
            if paquete.x < 30:  # Limite izquierdo
                llego_final = True
                personaje_encargado = self.luigi

        if llego_final:
            # Calcular en qué piso está el paquete (0, 1 o 2)
            piso_paquete = paquete.cinta_actual // 2

            # CASO ESPECIAL: Última cinta (5) -> Va al Camión
            if paquete.cinta_actual == 5:
                if self.luigi.piso_actual == 2 and not self.camion.en_reparto:
                    self.camion.recibir()
                    self.puntos += 1
                    paquete.activo = False
                else:
                    self.registrar_fallo(paquete)
                return

            # CASO NORMAL: Intercambio entre cintas
            # Si el personaje está en el mismo piso
            if personaje_encargado.piso_actual == piso_paquete:
                paquete.subir()  # Pasa a la siguiente cinta
                self.puntos += 1
            else:
                self.registrar_fallo(paquete)

    def registrar_fallo(self, paquete):
        paquete.activo = False
        self.fallos += 1
        # Aquí puedes poner sonido de error

        if paquete.cinta_actual == 5:
            # Luigi debe estar en Piso 2 (piso superior)
            if self.luigi.piso_actual == 2 and not self.camion.en_reparto:
                self.camion.recibir()
                self.puntos += 1  # +1 punto por entrega correcta [cite: 75]
                paquete.activo = False
            else:
                self.registrar_fallo(paquete)
            return

    def draw(self):
        pyxel.cls(constantes.COLOR_FONDO)

        if self.muerto:
            pyxel.text(100, 120, "GAME OVER", 8)
            pyxel.text(100, 130, f"Puntos: {self.puntos}", 7)
        else:
            # Dibujar escenario
            for cinta in self.cintas: cinta.draw()

            pyxel.blt(0, 0, *constantes.SPRITE_FONDO_UNICO)

            self.camion.draw()

            # Estructura central (Decoración)
            pyxel.rect(124, 40, 8, 180, 5)

            # Pisos (Lineas guia)
            pyxel.line(0, 85, 256, 85, 4)  # Techo piso 2
            pyxel.line(0, 145, 256, 145, 4)  # Techo piso 1

            self.mario.draw()
            self.luigi.draw()
            for p in self.paquetes: p.draw()

            # UI
            pyxel.text(10, 10, f"PUNTOS: {self.puntos}", 7)
            pyxel.text(180, 10, f"MISS: {self.fallos}", 8)