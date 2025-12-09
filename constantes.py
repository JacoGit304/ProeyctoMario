import pyxel

# --- CONFIGURACIÓN DE PANTALLA ---
ANCHO_PANTALLA = 256
ALTO_PANTALLA = 256
TITULO = "Mario Bros Game & Watch"
COLOR_FONDO = 0

# --- GAMEPLAY ---
# 6 cintas crean el ciclo perfecto de 3 pisos (Suelo, Medio, Arriba)
NUM_CINTAS = 6
VELOCIDAD_PAQUETE = 1.5 # Un poco más rápido para que no sea aburrido
FALLOS = 3
FRECUENCIA_APARICION = 180

# --- COORDENADAS ---
# Definimos alturas fijas para que se vea ordenado
# Piso 0 (Abajo), Piso 1 (Medio), Piso 2 (Arriba)
ALTURAS_CINTAS = [200, 175, 145, 115, 85, 55]
# Nota: Las cintas van en pares visuales.
# Cinta 0 (Abajo-Mario), Cinta 1 (Abajo-Luigi)
# Cinta 2 (Medio-Mario), Cinta 3 (Medio-Luigi)
# Cinta 4 (Arriba-Mario), Cinta 5 (Arriba-Luigi -> Camión)

# Posición del camión (Arriba a la Izquierda, donde Luigi termina)
POS_CAMION = (10, 45)

# --- SPRITES (Basado en tu elbueno.pyxres) ---
# Formato: (banco, u, v, w, h, colkey)
SPRITE_MARIO = (0, 0, 0, 16, 16, 0)   # Ajusté altura a 24
SPRITE_LUIGI = (0, 16, 0, 16, 16, 0)
SPRITE_CAJA  = (0, 32, 0, 16, 16, 0)
SPRITE_CINTA = (0, 0, 24, 16, 8, 0)   # Segmento de cinta
SPRITE_CAMION= (0, 0, 28, 22, 18, 0)  # Camión grande
POS_CAMION = (15, 35)
SPRITE_SUELO = (0, 0, 0, 0, 0, 0)     # Opcional si usas
SPRITE_FONDO_UNICO = (0, 0, 80, 256, 176, 0)