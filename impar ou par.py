from random import randint

nome = input(f"Digite seu nome: ")
print("olá,",nome, "vamos jogar impar ou par!")

numeros = (0,10)
numero_pc = randint(*numeros)

if numero_pc %2 != 0:
    escolha_pc = "Ímpar"
else:
    escolha_pc = "Par"

while True:
    escolha_usuario = str(input("Par ou ímpar?[P/I]: ")).strip().upper()
    num_usuario = int(input('Escolha um número de 0 a 10: '))
    soma = num_usuario + numero_pc

    if not ('P' in escolha_usuario or 'I' in escolha_usuario):
        print("Opção inválida. Tente novamente.")
        
    elif escolha_usuario == 'P':
        if soma % 2 ==  0:
            print(f"\nVocê jogou {num_usuario} e eu joguei {numero_pc}.\nO resultado deu {soma} que é Par.\nPortanto você ganhou!\n")
            break
        else:
            print(f"Perdeu! A soma é {soma}, que é ímpar. Você perdeu.")
            break
            
    elif escolha_usuario == 'I':
        if soma % 2 !=  0:
            print(f"\nVoce jogou {num_usuario} e eu joguei {numero_pc}. \no resultado deu {soma} que é ímpar. \nVocê ganhou!\n")
            break
        else:
            print(f"Perdeu! A soma é {soma}, que é par. Você perdeu.")
            break
