from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def exportar_estoque_pdf(estoque, nome_oficina):
    arquivo = f"estoque_{nome_oficina}.pdf"
    c = canvas.Canvas(arquivo, pagesize=A4)
    largura, altura = A4

    y = altura - 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, f"Relatorio de Estoque - {nome_oficina}")
    y -= 30

    c.setFont("Helvetica", 10)

    if not estoque:
        c.drawString(40, y, "Estoque vazio.")
    else:
        for nome, dados in estoque.items():
            if y < 80:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = altura - 40

            c.drawString(40, y, f"Produto: {nome.title()}")
            y -= 15
            c.drawString(60, y, f"Marca: {dados['marca']}")
            y -= 15
            c.drawString(60, y, f"Quantidade: {dados['quantidade']}")
            y -= 15
            c.drawString(60, y, f"Localização: {dados['localizacao']}")
            y -= 25

    c.save()
    print(f"\n PDF gerado com sucesso: {arquivo}")

nome_oficina = "oficina_2B"

estoque = {
    "pastilha de freio": {
        "marca": "Brembo",
        "quantidade": 10,
        "localizacao": "F01"
    },
    "graxa": {
        "marca": "Bardhal",
        "quantidade": 15,
        "localizacao": "G01"
    },
    "amortecedor": {
        "marca": "Cofap",
        "quantidade": 25,
        "localizacao": "A01"
    },
    "disco de embreagem": {
        "marca": "Fiat",
        "quantidade": 9,
        "localizacao": "E01"
    }
}

while True:
    print("\n===========================================")
    print(f"Seja bem-vindo ao gestor inteligente de estoque da {nome_oficina}")
    print("O que você deseja fazer?")
    print("Digite: cadastrar produto | consultar produto | ver estoque | exportar para pdf | sair")
    print("===========================================")

    opcao = input(">> ").strip().lower()

    if opcao == "cadastrar produto":
        print("\n=== Cadastro de Produto ===")

        nome_produto = input("Nome do produto: ").strip().lower()

        if nome_produto in estoque:
            print("\n⚠️ Produto já cadastrado no estoque!")
            print("Use a opção de consulta para ver os dados.")
            continue

        marca = input("Marca: ").strip()
        quantidade = int(input("Quantidade em estoque: "))
        localizacao = input("Localização no estoque: ").strip().upper()

        estoque[nome_produto] = {
            "marca": marca,
            "quantidade": quantidade,
            "localizacao": localizacao
        }

        print("\n✅ Produto cadastrado com sucesso!")

    elif opcao == "consultar produto":
        print("\n=== Consulta de Produto ===")

        nome_produto = input("Digite o nome do produto: ").strip().lower()

        if nome_produto in estoque:
            produto = estoque[nome_produto]
            print("\nProduto encontrado:")
            print(f"Marca: {produto['marca']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Localização: {produto['localizacao']}")        
        else:
            print("\n❌ Produto não encontrado. Tente novamente.")

    elif opcao == "ver estoque":
        print("\n=== ESTOQUE ATUAL ===")

        if not estoque:
            print("O estoque esta vazio.")
        else:
            for nome, dados in estoque.items():
                print("\n---------------------")
                print(f"Produto: {nome.title()}")
                print(f"Marca: {dados['marca']}")
                print(f"Quantidade: {dados['quantidade']}")
                print(f"Localização: {dados['localizacao']}")    

    elif opcao == "exportar para pdf":
        exportar_estoque_pdf(estoque, nome_oficina)
        print("\n PDF Exportado com sucesso!")                    

    elif opcao == "sair":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\n❌ Opção inválida. Tente novamente.")