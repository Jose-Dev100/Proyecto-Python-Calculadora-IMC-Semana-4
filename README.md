# Calculadora de I.M.C.

Proyecto final del módulo **Fundamentos de Python** (M1S4) – Ucamp.

## Descripción del programa

Programa de consola que calcula el **Índice de Masa Corporal (IMC)** de una persona y lo clasifica según las categorías de la OMS.

El programa solicita:

- **Nombre**
- **Edad** (años)
- **Peso** (kg)
- **Estatura** (metros, por ejemplo `1.70`)

### Validaciones implementadas

- **Campos vacíos:** si el usuario presiona Enter sin escribir nada, se muestra un mensaje de error y se vuelve a pedir el dato.
- **Entradas no numéricas:** si en edad, peso o estatura se escriben letras u otros caracteres, el programa captura el error con `try/except ValueError` y no se cierra (no hay *crash*).
- **Rangos razonables:** edad (1–120), peso (1–500 kg) y estatura (0.5–2.5 m), para evitar divisiones erróneas o resultados absurdos.
- Se aceptan decimales con punto o con coma (`1.70` o `1,70`).

### Estructura del código

| Función | Responsabilidad |
|---|---|
| `pedir_texto()` | Pide un texto y rechaza campos vacíos |
| `pedir_numero()` | Pide un número, valida que sea numérico y esté en rango |
| `calcular_imc()` | Aplica la fórmula `peso / estatura²` |
| `clasificar_imc()` | Devuelve la categoría de peso |
| `main()` | Coordina el flujo del programa |

### Clasificación

| IMC | Categoría |
|---|---|
| Menor a 18.5 | Bajo peso |
| 18.5 – 24.9 | Peso normal |
| 25 – 29.9 | Sobrepeso |
| 30 o más | Obesidad |

## Instrucciones de ejecución

1. Instala [Python 3.8 o superior](https://www.python.org/downloads/).
2. Clona el repositorio:
   ```bash
   git clone <URL-DE-TU-REPOSITORIO>
   cd <NOMBRE-DEL-REPOSITORIO>
   ```
3. Ejecuta el programa:
   ```bash
   python calculadora_imc.py
   ```
4. Sigue las indicaciones en pantalla.

### Ejemplo de uso

```
=== Calculadora de I.M.C. ===
Nombre: Ana
Edad (años): treinta
Error: debes ingresar solo cifras numéricas (sin letras).
Edad (años): 30
Peso (kg): 65,5
Estatura (m, ejemplo 1.70): 1.7

Resultado para Ana (30 años):
IMC: 22.66 -> Peso normal
```

> Nota: el IMC es una referencia general y no sustituye una valoración médica.

## Reflexiones personales sobre mi aprendizaje en el bootcamp


Al comenzar el bootcamp, Python me parecía bastante interesa y a lo largo de las semanas aprendí a trabajar con el

