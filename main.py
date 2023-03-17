class Carta:
    def __init__(self, valor, figura):
        self.valor = valor
        self.figura = figura

class Baraja:
    def __init__(self):
        self.cartas = []

    def mezclar(self):
        pass

    def repartir_carta(self):
        pass

class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        pass

    def obtener_valor(self):
        pass

class Jugador:
    def __init__(self, nombre, fichas):
        self.nombre = nombre
        self.fichas = fichas
        self.mano = Mano()

    def apostar(self, fichas):
        pass

    def obtener_apuesta(self):
        pass

    def solicitar_jugada(self):
        pass

    def seleccionar_jugada(self):
        pass

    def obtener_mano(self):
        return self.mano

class Casa:
    def __init__(self):
        self.mano = Mano()

    def destapar_carta_oculta(self):
        pass

    def calcular_valor_mano(self):
        pass

    def repetir_carta(self):
        pass

    def finalizar_juego(self):
        pass

class Blackjack:
    def __init__(self):
        self.baraja = Baraja()
        self.jugador = Jugador("Jugador", 100)
        self.casa = Casa()

    def jugar(self):
        pass

    def pedir_carta(self, jugador):
        pass

    def evaluar_mano(self, mano):
        pass

    def comparar_manos(self):
        pass

    def doblar_fichas(self):
        pass

    def restar_fichas(self):
        pass

    def devolver_fichas(self):
        pass

    def solicitar_jugada(self):
        pass

    def jugador_planta(self):
        pass

    def jugar_casa(self):
        pass
