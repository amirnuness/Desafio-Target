
#5) Escreva um programa que inverta os caracteres de um string.

print("Olá! Vamos inverter uma string hoje?")
string_original = input("Por favor, digite uma frase ou palavra: ")

caracteres = list(string_original)

tamanho = len(caracteres)

for i in range(tamanho // 2):

    temp = caracteres[i]
    caracteres[i] = caracteres[tamanho - 1 - i]
    caracteres[tamanho - 1 - i] = temp


string_invertida = ''

for char in caracteres:
    string_invertida += char

print("A string invertida é:", string_invertida)
