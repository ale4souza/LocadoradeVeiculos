# Lista global de carros alugados
alu = []
while True:
    print("Bem Vindo à locadora de carros!")
    print("==============================")
    print("O que deseja fazer?")
    print("0 - Mostrar Portfólio")
    print("1 - Alugar um carro")
    print("2 - Devolver um carro")

    # Pega a escolha do usuário
    opc = int(input("Escolha uma opção: "));  # 'input()' pede ao usuário que insira um valor
    portfolio = [
            '[0] Chevrolet Tracker - R$120 /dia',
            '[1] Chevrolet Onix - R$90 /dia',
            '[2] Hyundai HB20 - R$85 /dia',
            '[3] Hyundai Tucson - R$120 /dia',
            '[4] Fiat Mobi - R$70 /dia',
            '[5] Fiat Pulse - R$130 /dia'
                                ]
    precos = [120, 90, 85, 120, 70, 130]  # Lista com os preços diários correspondentes aos carros
    
    #Opção 0 (Exibir Portfolio)
    if opc == 0:
        print("Você escolheu ver o Portfólio!")
    
        for i in range(len(portfolio)):
            print(portfolio[i]);
            
        print("========================");
        print("0 - Continuar | 1 - Sair");
        esc = int(input("Escolha a sua opção: "));
        if esc == 1:
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa
        elif esc == 0:
            continue  # Volta ao início do loop sem repetir o código
# Opção 1 (Alugar um carro)
    elif opc == 1:
        print("Você escolheu alugar um carro!")
        for i in range(len(portfolio)):
            print(portfolio[i]);
        cod_carro = int(input("Informe o código do carro: "));
        if 0 <= cod_carro < len(portfolio):
            dias = int(input("Por quantos dias deseja alugar o carro? "))
            valor_total = precos[cod_carro] * dias  # Calcula o valor total com base no preço por dia
            print(f"O valor total para {dias} dias de aluguel do {portfolio[cod_carro]} será: R${valor_total}");
            confirmar = input("Deseja confirmar o aluguel? (s/n): ").lower();
            if confirmar == 's':
                alu.append(portfolio[cod_carro]);# Adiciona o carro à lista de alugados
                print(f"Parabéns! Você alugou o {portfolio[cod_carro]} por {dias} dias.");
            else: 
                print("Aluguel cancelado.")
        else:
            print("Código de carro inválido. Tente novamente.")