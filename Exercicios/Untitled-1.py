
operador = input("Digite o operador (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if operador == "+":
        resultado = num1 + num2 
elif operador == "-":
        resultado = num1 - num2
elif operador == "*":
        resultado = num1 * num2
elif operador == "/":
        resultado = num1 / num2
else :  
        print("es gay meu")
print (f"O resultado de {num1} {operador} {num2} é: {round(resultado, 2)}")