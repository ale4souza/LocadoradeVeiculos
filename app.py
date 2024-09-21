# Lista global de carros alugados
alu = []
# Lista de portfólio e preços fora do loop
portfolio = [
    'Chevrolet Tracker',
    'Chevrolet Onix',
    'Hyundai HB20',
    'Hyundai Tucson',
    'Fiat Mobi',
    'Fiat Pulse'
]
precos = [120, 90, 85, 120, 70, 130]  # Lista com os preços diários correspondentes aos carros

while True:
    print("Bem Vindo à locadora de carros!")
    print("==============================")
    print("O que deseja fazer?")
    print("0 - Mostrar Portfólio")
    print("1 - Alugar um carro")
    print("2 - Devolver um carro")

    # Pega a escolha do usuário
    opc = int(input("Escolha uma opção: "))

    # Opção 0 (Exibir Portfólio)
    if opc == 0:
        print("Você escolheu ver o Portfólio!")
        for i in range(len(portfolio)):
            print(f"[{i}] {portfolio[i]} - R${precos[i]} /dia")
            
        print("========================")
        print("0 - Continuar | 1 - Sair")
        esc = int(input("Escolha a sua opção: "))
        if esc == 1:
            print("Encerrando o programa...")
            break
        elif esc == 0:
            continue

    # Opção 1 (Alugar um carro)
    elif opc == 1:
        print("Você escolheu alugar um carro!")
        for i in range(len(portfolio)):
            print(f"[{i}] {portfolio[i]} - R${precos[i]} /dia")
        cod_carro = int(input("Informe o código do carro: "))
        if 0 <= cod_carro < len(portfolio):
            dias = int(input("Por quantos dias deseja alugar o carro? "))
            valor_total = precos[cod_carro] * dias
            print(f"O valor total para {dias} dias de aluguel do {portfolio[cod_carro]} será: R${valor_total}")
            confirmar = input("Deseja confirmar o aluguel? (s/n): ").lower()
            if confirmar == 's':
                carro_alugado = portfolio.pop(cod_carro)
                valor_alugado = precos.pop(cod_carro)
                alu.append((carro_alugado, valor_alugado))  # Armazena o carro e seu valor
                print(f"Parabéns! Você alugou o {carro_alugado} por {dias} dias.")
                continue
            else: 
                print("Aluguel cancelado.")
        else:
            print("Código de carro inválido. Tente novamente.")

    # Opção 2 (Devolver um carro)  
    elif opc == 2:
        if not alu:
            print("Nenhum carro alugado atualmente.")
            continue
        
        print("Segue a lista de carros que estão alugados, qual deseja devolver?")
        for i in range(len(alu)):
            print(f"[{i}] {alu[i][0]} - R${alu[i][1]} /dia")  # Exibe carro e seu valor
        cod_devolve = int(input("Informe o código do carro que deseja devolver: "))
    
        if (0 <= cod_devolve < len(alu)):
            carro_devolvido = alu.pop(cod_devolve)
            portfolio.append(carro_devolvido[0])  # Adiciona o carro de volta ao portfolio
            precos.append(carro_devolvido[1])  # Adiciona o preço de volta
            print(f"Você devolveu o {carro_devolvido[0]}")
            opc_aluguel = input("Deseja alugar um novo carro? (s/n): ").lower()  
            if opc_aluguel == 's':
                continue
            else:
                print("Obrigado por alugar conosco!")
        else:
            print("Escolha uma opção válida.")