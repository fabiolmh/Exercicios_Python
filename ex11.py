"""11. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar."""
#importação de bibliotecas
# Importação de bibliotecas
import os

# Funções
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def divisao(x: float, y: float) -> float | None:
    try:
        # Verifica se o divisor não é zero para evitar o erro ZeroDivisionError.
        if x == 0 or y == 0:
            raise ZeroDivisionError

        if y > x:
            res = y / x
        else:
            res = x / y
        return res
    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")
        return None
    except TypeError:
        print("A divisão não pode ser realizada. Por favor, informe números válidos!")
        return None

# Main
def main():
    limpar()
    try:
        dividendo = float(input("Informe o dividendo: "))
        divisor = float(input("Informe o divisor: "))
    except ValueError:
        print("Digite números válidos.")
        input("Aperte qualquer tecla para seguir:")
        return main()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        input("Aperte qualquer tecla para seguir:")
        return main()

    resultado = divisao(dividendo, divisor)
    
    # Verifica se o resultado da função de divisão não é None antes de imprimir.
    if resultado is not None:
        limpar()
        print("--- CÁLCULO DA DIVISÃO ---")
        print(f"Dividendo: {dividendo:.1f}")
        print(f"Divisor:   {divisor:.1f}")
        print("_" * 25)
        print(f"Resultado: {resultado:.1f}")
        print("_" * 25)

if __name__ == "__main__":
    main()