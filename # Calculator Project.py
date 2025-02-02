"""
Calculator Project - A simple calculator program that can perform basic arithmetic operations.
"""

def add(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtract(a, b):
    """Retorna a subtração de b de a."""
    return a - b

def multiply(a, b):
    """Retorna o produto de a e b."""
    return a * b

def divide(a, b):
    """Retorna a divisão de a por b. Levanta ValueError se b for zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_number(prompt):
    """Solicita ao usuário um número e trata possíveis erros de conversão."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    while True:
        print("\nWelcome to the calculator program!")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Exiting the program.")
            break  # Sai do loop principal

        # Obter números com validação
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid input. Please select a valid option.")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
# End of # Calculator Project.py