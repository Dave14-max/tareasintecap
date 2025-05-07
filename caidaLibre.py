import math

class ExperimentoFisico:
    def __init__(self):
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad):
        super().__init__()
        self.altura = altura
        self.gravedad = gravedad

    def calcular_tiempo_caida(self):
        if self.altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if self.gravedad == 0:
            raise ValueError("La gravedad no puede ser cero.")
        
        tiempo_caida = math.sqrt((2 * self.altura) / self.gravedad)
        return tiempo_caida

def obtener_numero(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor válido.")

def main():
    altura = obtener_numero("Ingrese la altura en metros: ")
    gravedad = obtener_numero("Ingrese la gravedad en m/s^2: ")

    try:
        experimento = CaidaLibre(altura, gravedad)
        tiempo = experimento.calcular_tiempo_caida()
        print(f"El tiempo de caída es: {tiempo:.2f} segundos")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()