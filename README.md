# TRABAJO-AUTONOMO-2
import random

# Lista de palabras
palabras = ["computadora", "teclado", "monitor", "camara", "mouse", "parlantes", "tarjeta", "cargador", "laptop", "impresora"]

# Seleccion de palabra aleatoria
palabra_secreta = random.choice(palabras)
letras_acertadas = set()
letras_erradas = set()
intentos_restantes = 6

# COntador de palabra
def mostrar_estado():
    estado_visible = " ".join([letra if letra in letras_acertadas else "_" for letra in palabra_secreta])
    print("\nPalabra:", estado_visible)
    print("Intentos restantes:", intentos_restantes)
    print("Letras erradas:", ", ".join(sorted(letras_erradas)))

# Bucle principal del juego
while True:
    mostrar_estado()

    # Verificar condiciones de palabra
    if intentos_restantes == 0:
        print("\n¡Has perdido! La palabra era:", palabra_secreta)
        break
    if all(letra in letras_acertadas for letra in palabra_secreta):
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break

    intento = input("\nIngresa una letra o la palabra completa: ").lower().strip()

    # Validación de letraa
    if not intento.isalpha():
        print("Entrada inválida. Solo se permiten letras.")
        continue

    # Adivinar palabra completa
    if len(intento) > 1:
        if intento == palabra_secreta:
            letras_acertadas.update(palabra_secreta)
            print("\n¡Adivinaste la palabra completa!")
        else:
            print("Palabra incorrecta.")
            letras_erradas.add(intento)
            intentos_restantes -= 1
        continue

    # Adivinar letra
    if intento in letras_acertadas or intento in letras_erradas:
        print("Ya intentaste esa letra.")
        continue

    if intento in palabra_secreta:
        letras_acertadas.add(intento)
        print("¡Letra correcta!")
    else:
        letras_erradas.add(intento)
        intentos_restantes -= 1
        print("Letra incorrecta.")
