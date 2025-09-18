import os

os.system('clear')

idade = int(input("Qual é a tua idade? "))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Acabaste de fazer 18 anos")
else:
    print("Maior de idade")