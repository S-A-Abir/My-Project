from functools import reduce
import math

class Calculator:
    @staticmethod
    def add_sub_mul_div():
        opt = input("Enter operation (+, -, *, /): ").strip()
        if opt not in ["+", "-", "*", "/"]:
            return "Invalid operation! Use +, -, *, or /."
        
        if opt == "/":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if b == 0:
                    return "Undefined: Division by zero!"
                return f"Result: {a / b}"
            except ValueError:
                return "Invalid number input!"
        
        num = []
        while True:
            user_input = input("Enter number (or 'quit' to finish): ")
            if user_input.lower() == "quit":
                break
            try:
                num.append(float(user_input))
                print("Current list:", num)
            except ValueError:
                print("Invalid input! Enter a number or 'quit'.")
        
        if not num:
            return "List is empty, result is 0."
        
        try:
            if opt == "+":
                total = reduce(lambda x, y: x + y, num)
                return f"Sum: {total}"
            elif opt == "-":
                total = reduce(lambda x, y: x - y, num)
                return f"Difference: {total}"
            elif opt == "*":
                total = reduce(lambda x, y: x * y, num)
                return f"Product: {total}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def power():
        try:
            x = float(input("Enter base number: "))
            n = float(input("Enter exponent: "))
            if x == 0 and n == 0:
                return "Undefined"
            return f"Result: {x ** n}"
        except ValueError:
            return "Invalid number input!"

    @staticmethod
    def conversion():
        base = input("Enter base (binary, decimal, hex, octal): ").strip().lower()
        number = input(f"Enter {base} number (e.g., -1010 for binary, -1a for hex): ").strip()
        try:
            # Handle negative numbers
            is_negative = number.startswith('-')
            num_str = number.lstrip('-').lower().replace('0b', '').replace('0x', '').replace('0o', '')
            
            # Convert to decimal
            if base == "binary":
                decimal = int(num_str, 2)
            elif base == "decimal":
                decimal = int(num_str)
            elif base == "hex":
                decimal = int(num_str, 16)
            elif base == "octal":
                decimal = int(num_str, 8)
            else:
                return "Invalid base! Use binary, decimal, hex, or octal."
            
            decimal = -decimal if is_negative else decimal
            
            # Convert decimal to other bases
            sign = "-" if decimal < 0 else ""
            abs_decimal = abs(decimal)
            return (f"Decimal: {decimal}\n"
                    f"Binary: {sign}0b{bin(abs_decimal)[2:]}\n"
                    f"Hex: {sign}0x{hex(abs_decimal)[2:]}\n"
                    f"Octal: {sign}0o{oct(abs_decimal)[2:]}")
        except ValueError:
            return f"Invalid {base} number! Use valid digits for {base}."

    @staticmethod
    def logarithm():
        try:
            number = float(input("Enter number to calculate its logarithm: "))
            base = float(input("Enter base of logarithm (e.g., 10, 2): "))
            result = math.log(number, base)
            return f"Logarithm of {number} with base {base}: {result:.4f}"
        except ValueError as e:
            return "Error: Ensure number is positive and base is positive, not 1."

    @staticmethod
    def run():
        while True:
            print("\nCalculator Menu")
            print("1. Add/Subtract/Multiply/Divide")
            print("2. Power")
            print("3. Base Conversion")
            print("4. Logarithm")
            print("5. Exit")
            
            choice = input("Choose function (1-5): ").strip()
            if choice == "5":
                print("====!!THANK YOU!!====")
                break
            
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice!")
                continue
            
            calc = Calculator()
            if choice == "1":
                print(calc.add_sub_mul_div())
            elif choice == "2":
                print(calc.power())
            elif choice == "3":
                print(calc.conversion())
            elif choice == "4":
                print(calc.logarithm())

if __name__ == "__main__":
    Calculator.run()