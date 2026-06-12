 # Se eu ganhasse 1 real

# Projeto criado a partir de uma piada interna 
# onde cada vez que determinadas coisas acontecem eu ganharia 1 real
# Uso de dicionario para armazenar as variaveis
# Input para inserir eventos que aconteceram e estão contidos no dicionario
# Atribuição de numeros as variaveis para tornar mais simples a sua referencia 
# Criação de um arquivo para salvar os dados
# Implantação de um arquivo de historico de acontecimentos 
# Looping de inserção de acontecimentos

eventos = {
    1: "internet caiu",
    2: "code sandbox me irritou",
    3: "ana não trancou o guidon da moto",
    4: "meu pai me irritou",
    5: "caiu a luz",
    6: "vacas me irritaram",
    7: "cachorros brigaram",
    8: "não tinha fruta",
    9: "meu pai falou bobagem",
    10: "tive que desentupir a privada",
    11: "fiz 10 minutos de esteira",
    12: "algum codigo ou trecho de codigo não funcionou",
    13: "Poly fez sujeira no chão",
    14: "Os gatos me estressaram "
}


# Lê o saldo salvo

with open("Ganhei 1 real/saldo.txt", "r") as arquivo:
    saldo = int(arquivo.read())

while True:

    print(f"\nSaldo atual: R$ {saldo}\n")

# Mostra o menu

    for codigo, descricao in eventos.items():
        print(f"{codigo} - {descricao}")

    evento = int(input("\nO que aconteceu? "))

    if evento in eventos:

        saldo += 1

        print("\nVocê ganhou 1 real! ")
        print(f"Evento registrado: {eventos[evento]}")


# Salva o novo saldo

        with open("Ganhei 1 real/historico.txt", "a", encoding="utf-8") as historico:
            historico.write(eventos[evento] + "\n")

        print(f"\nHistorico atualizado: {historico}")    

        with open("Ganhei 1 real/saldo.txt", "w") as arquivo:
            arquivo.write(str(saldo))

        print(f"\nSaldo atualizado: R$ {saldo}")

    else:

        print("\nEvento não encontrado.")

    continuar = input("\nRegistrar outro evento? (s/n): ").lower()

    if continuar != "s":
        break

print("\nSistema encerrado.")
