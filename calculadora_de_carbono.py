resposta = "NÃO"
alternativaEscolhida = ""
totalDePontos = 0

while (resposta == "NÃO"):
    print("---------------CALCULADORA DE PEGADA ECOLÓGICA---------------")
    resposta = input("Quer descobrir o quanto suas ações impactam o meio ambiente ? \n(SIM ou NÃO):").upper()
    print("Entendido, te esperamos aqui  ;)")

if (resposta =="SIM"):
    print("Ótimo !!\nAgora basta responder as perguntas abaixo. Elas são divididas por categorias ! :)")

    alternativaEscolhida = input("ENERGIA------------------------------\n 1. Como é o consumo de energia elétrica na sua casa?\na) Uso moderado, com eletrodomésticos eficientes e desligo o que não uso. \nb) Uso normal, sem muitos cuidados com economia.\nc) Uso alto, deixo muitos aparelhos ligados e uso ar-condicionado frequentemente. ").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    "\n"

    alternativaEscolhida = input("2. Você usa energia renovável (como solar)?\na) Sim, em grande parte da energia consumida.\nb) Apenas uma pequena parte da energia é renovável.\nc) Não utilizo energia renovável.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    print(totalDePontos)

    alternativaEscolhida = input("TRANSPORTE------------------------------\n3. Como você se locomove no dia a dia? \na) Caminho ou uso bicicleta.\nb) Uso transporte público.\nc) Uso carro particular todos os dias.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    alternativaEscolhida = input("4. Seu veículo é elétrico ou híbrido?\na) Sim.\nb) Não, é a combustão.\nc) Não tenho carro.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    alternativaEscolhida = input("LIXO------------------------------\n5. Você separa o lixo para reciclagem?\na) Sim, separo corretamente.\nb) Às vezes separo.\nc) Não separo.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    alternativaEscolhida = input("6. Com que frequência você gera lixo orgânico e reciclável?\na) Produzo pouco, reutilizo o que posso.\nb) Produzo uma quantidade média.\nc) Produzo muito lixo.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    alternativaEscolhida = input("ALIMENTAÇÃO------------------------------\n7. Qual seu padrão alimentar?\na) Sou vegetariano(a) ou vegano(a).\nb) Como carne algumas vezes por semana.\nc) Consumo carne todos os dias.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    alternativaEscolhida = input("8. Consome alimentos orgânicos ou de produtores locais?\na) Sempre que possível.\nb) Às vezes.\nc) Quase nunca.").upper()
    if(alternativaEscolhida == "A"):
        totalDePontos = totalDePontos + 1
    elif(alternativaEscolhida == "B"):
        totalDePontos = totalDePontos + 2
    else: 
        totalDePontos = totalDePontos + 3

    print("SEU RESULTADO É....")
    if(totalDePontos >= 8 and totalDePontos <= 12):
        print("#####SUSTENTÁVEL(✿◠‿◠)#####")
        print("Seu estilo de vida mostra grande consciência ambiental. Continue assim!")
    elif(totalDePontos <= 13 and totalDePontos <= 18):
        print("#####MODERADO (•◡•) /#####")

    else:
        print("#####ALTO IMPACTO( ˘︹˘ )#####")
        print("Seu estilo de vida tem impacto ambiental significativo. Que tal repensar alguns hábitos?")


   
