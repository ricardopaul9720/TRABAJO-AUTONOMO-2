INICIO

Definir lista de palabras
Seleccionar palabra aleatoria de la lista

Inicializar:
    letras_acertadas ← conjunto vacío
    letras_erradas ← conjunto vacío
    intentos_restantes ← 6

MIENTRAS el juego no haya terminado HACER:
    Mostrar estado actual:
        - palabra con guiones y letras acertadas
        - intentos restantes
        - letras erradas

    SI intentos_restantes = 0 ENTONCES
        Mostrar mensaje de derrota
        SALIR del bucle

    SI todas las letras de la palabra están en letras_acertadas ENTONCES
        Mostrar mensaje de victoria
        SALIR del bucle

    Solicitar entrada del usuario (letra o palabra)

    Validar entrada:
        SI no es alfabética ENTONCES
            Mostrar mensaje de error
            CONTINUAR al siguiente ciclo

    SI entrada tiene más de un carácter ENTONCES
        SI entrada = palabra_secreta ENTONCES
            letras_acertadas ← todas las letras de la palabra
            Mostrar mensaje de victoria parcial
        SINO
            Añadir entrada a letras_erradas
            Restar 1 a intentos_restantes
        CONTINUAR al siguiente ciclo

    SI entrada ya está en letras_acertadas o letras_erradas ENTONCES
        Mostrar mensaje de letra repetida
        CONTINUAR al siguiente ciclo

    SI entrada está en palabra_secreta ENTONCES
        Añadir entrada a letras_acertadas
        Mostrar mensaje de acierto
    SINO
        Añadir entrada a letras_erradas
        Restar 1 a intentos_restantes
        Mostrar mensaje de error

FIN MIENTRAS

FIN