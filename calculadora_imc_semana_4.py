"""Calculadora de I.M.C. (Índice de Masa Corporal) con validación de entradas."""


def pedir_texto(mensaje):
    """Pide un texto al usuario y repite la pregunta si algun campo llega a quedar vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: este campo no puede estar vacío. Inténtalo de nuevo.")
        else:
            return valor


def pedir_numero(mensaje, minimo, maximo):
    """Pide un número (acepta decimales con punto o coma) dentro de un rango.

    Repite la pregunta si el campo está vacío, contiene letras u otros
    caracteres no numéricos, o si el valor queda fuera del rango permitido.
    """
    while True:
        valor = pedir_texto(mensaje).replace(",", ".")
        try:
            numero = float(valor)
        except ValueError:
            print("Error: debes ingresar solo cifras numéricas (sin letras).")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"Error: el valor debe estar entre {minimo} y {maximo}.")


def calcular_imc(peso, estatura):
    """Calcula el IMC: peso (kg) dividido entre estatura (m) al cuadrado."""
    return peso / (estatura ** 2)


def clasificar_imc(imc):
    """Devuelve la categoría de peso según la clasificación de la OMS."""
    if imc < 18.5:
        return "Bajo peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidad"


def main():
    """Flujo principal: captura datos, valida, calcula y muestra el resultado."""
    print("=== Calculadora de I.M.C. ===")

    nombre = pedir_texto("Nombre: ")
    edad = pedir_numero("Edad (años): ", 1, 120)
    peso = pedir_numero("Peso (kg): ", 1, 500)
    estatura = pedir_numero("Estatura (m, ejemplo 1.70): ", 0.5, 2.5)

    imc = calcular_imc(peso, estatura)

    print(f"\nResultado para {nombre} ({edad:.0f} años):")
    print(f"IMC: {imc:.2f} -> {clasificar_imc(imc)}")


if __name__ == "__main__":
    main()
