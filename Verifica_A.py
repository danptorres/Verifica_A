def verifica_a(texto):
    texto_minusculo = texto.lower() #Aplica o texto minúsculo em uma variável
    qtd_a = texto_minusculo.count('a')  #Conta a quantida de 'a' no texto


    if 'a' in texto_minusculo:
        print(f"A letra 'a' esta presente no texto, e aparece {qtd_a} de vezes")
    else:
        print("A letra 'a' não esta presente no texto!")

texto_entrada = input("Digite um texto: ")
verifica_a(texto_entrada)