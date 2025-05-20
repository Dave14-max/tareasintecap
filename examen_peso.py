def obtener_dato_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"PORFAVOR, INGRESA UN NUMERO ENTRE {minimo} Y {maximo}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def obtener_dato_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número decimal válido.")

def seleccionar_departamento(departamentos):
    print("Seleccione el departamento:")
    for i, depto in enumerate(departamentos, 1):
        print(f"{i}. {depto}")
    while True:
        try:
            opcion = int(input("Número del departamento: "))
            if 1 <= opcion <= len(departamentos):
                return departamentos[opcion - 1]
            else:
                print("Número fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def obtener_sexo(mensaje):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ["niño", "niña"]:
            return valor
        else:
            print("Entrada inválida. Por favor, ingresa 'niño' o 'niña'.")

estandares_oms = {
    0: {"peso": (2.5, 4.5), "talla": (45.0, 55.0), "perimetro": (32.0, 38.0)},
    1: {"peso": (3.0, 5.5), "talla": (47.0, 57.0), "perimetro": (33.0, 39.0)},
    2: {"peso": (3.5, 6.0), "talla": (49.0, 59.0), "perimetro": (34.0, 40.0)},
    # ... completar para cada mes hasta 24
}

def obtener_estandares_por_edad(edad):
    if edad in estandares_oms:
        return estandares_oms[edad]
    else:
        meses_disponibles = sorted(estandares_oms.keys())
        menor = max([m for m in meses_disponibles if m <= edad], default=0)
        return estandares_oms[menor]

def clasificar_valor(valor, rango):
    min_val, max_val = rango
    if valor < min_val:
        return "Por debajo del promedio"
    elif valor > max_val:
        return "Por encima del promedio"
    else:
        return "Dentro del promedio"

def mostrar_registros(registros):
    if not registros:
        print("No hay registros ingresados.")
        return
    print("\nDatos de todos los pacientes ingresados:")
    for i, reg in enumerate(registros, 1):
        print(f"\nPaciente {i}:")
        for clave, valor in reg.items():
            print(f"  {clave}: {valor}")

def main():
    departamentos_guatemala = [
        "Alta Verapaz", "Baja Verapaz", "Chimaltenango", "Chiquimula", "Guatemala",
        "El Progreso", "Escuintla", "Huehuetenango", "Izabal", "Jalapa",
        "Jutiapa", "Petén", "Quetzaltenango", "Quiché", "Retalhuleu",
        "Sacatepéquez", "San Marcos", "Santa Rosa", "Sololá", "Suchitepéquez",
        "Totonicapán", "Zacapa"
    ]

    registros = []

    print("SISTEMA DE MONITOREO DE CRECIMIENTO INFANTIN EN GUATEMALA")

    while True:
        print("\nMenú:")
        print("1. Ingresar datos de un niño o niña")
        print("2. Mostrar datos de todos los pacientes")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == '1':
            print("\nIngrese los datos del niño o niña:")

            nombre = input("Nombre: ").strip()
            sexo = obtener_sexo("Sexo (niño/niña): ")
            edad = obtener_dato_entero("Edad (meses, 0-24): ", 0, 24)
            peso = obtener_dato_decimal("Peso (kg): ")
            talla = obtener_dato_decimal("Talla (cm): ")
            perimetro_craneal = obtener_dato_decimal("Perímetro craneal (cm): ")
            departamento = seleccionar_departamento(departamentos_guatemala)

            estandares = obtener_estandares_por_edad(edad)

            clasificacion_peso = clasificar_valor(peso, estandares["peso"])
            clasificacion_talla = clasificar_valor(talla, estandares["talla"])
            clasificacion_perimetro = clasificar_valor(perimetro_craneal, estandares["perimetro"])

            registro = {
                "Nombre": nombre,
                "Sexo": sexo,
                "Edad (meses)": edad,
                "Peso (kg)": peso,
                "Talla (cm)": talla,
                "Perímetro craneal (cm)": perimetro_craneal,
                "Departamento": departamento,
                "Clasificación Peso": clasificacion_peso,
                "Clasificación Talla": clasificacion_talla,
                "Clasificación Perímetro": clasificacion_perimetro
            }
            registros.append(registro)

            print("\nRegistro guardado con clasificaciones:")
            for clave, valor in registro.items():
                print(f"{clave}: {valor}")

        elif opcion == '2':
            mostrar_registros(registros)

        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("OPCIÓN INVÁLIDA. PORFAVOR, SELECCIONE 1, 2 o 3.")

    # Informe final por departamento al salir
    if registros:
        print("\n----------Informe por departamento----------")
        for depto in departamentos_guatemala:
            registros_depto = [r for r in registros if r["Departamento"] == depto]
            total = len(registros_depto)
            if total == 0:
                continue
            print(f"\nDepartamento: {depto}")
            print(f"Número total de niños evaluados: {total}")

            for indicador in ["Peso", "Talla", "Perímetro"]:
                debajo = sum(1 for r in registros_depto if r[f"Clasificación {indicador}"] == "Por debajo del promedio")
                dentro = sum(1 for r in registros_depto if r[f"Clasificación {indicador}"] == "Dentro del promedio")
                encima = sum(1 for r in registros_depto if r[f"Clasificación {indicador}"] == "Por encima del promedio")

                print(f"\nIndicador: {indicador}")
                print(f"Por debajo del promedio: {debajo} ({debajo/total*100:.1f}%)")
                print(f"Dentro del promedio: {dentro} ({dentro/total*100:.1f}%)")
                print(f"Por encima del promedio: {encima} ({encima/total*100:.1f}%)")

if __name__ == "__main__":
    main()