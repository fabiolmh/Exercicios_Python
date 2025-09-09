"""9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"""
import os

def limparTela():
    os.system('clear')    

def apresentacao():
    limparTela()
    print("=" * 60)
    print("1: SALVADOR-BA")
    print("2: FORTALEZA-CE")
    print("3: NATAL-RN")
    print("4: ARACAJU-SE")
    print("=" * 60)

##Inicio da iteração com o usuário
apresentacao()
escolha = int(input("INFORME A CIDADE NA QUAL DESEJA VIAJAR: "))
dias = int(input("Informe a quantidade de dias que deseja ficar: "))

dHotel = 150
cidade = ["Salvador", "Fortaleza", "Natal", "Aracaju"]
custodiario = [200, 400, 250, 300]
distancia = [850, 800, 300, 550]

destino = cidade[escolha - 1]
gastosHotel = dHotel * dias
gastosGasolina = (14 * (distancia[escolha - 1] * 2)) / 5
gasotsPasseio = custodiario[escolha - 1] * dias

gastoTotal = gastosHotel + gasotsPasseio + gastosGasolina
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {destino} saindo de Recife custaria R$ {gastoTotal:.2f}.")