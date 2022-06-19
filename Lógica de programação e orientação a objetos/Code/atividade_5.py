# Elabore um algoritmo que possa descobrir, através de perguntas e respostas, qual meio de transporte o usuário está pensando.
# O usuário deverá escolher uma das seguintes opções:
 
# - Trator (terrestre, peso pesado, cabe só 1 pessoa)
# - Moto (terrestre, peso leve, não tem pedal)
# - Bicicleta (terrestre, peso leve, tem pedal)
# - Trem (terrestre, peso pesado, 4 rodas ou mais, propósito: transporte de muitas pessoas e muitas cargas, ferroviário)
# - Carro (terrestre, peso pesado, máximo 4 rodas)
# - Caminhão (terrestre, peso pesado, 4 rodas ou mais, propósito: transporte de muita carga, rodoviário)
# - Ônibus (terrestre, peso pesado, 4 rodas ou mais, propósito: transporte de pessoas)
# - Paraquedas (aéreo, cabe até 2 pessoas, peso leve, não tem propulsão)
# - Balão (aéreo, cabe até 6 pessoas, propulsão a gases, peso leve)
# - Avião (aéreo, cabe várias pessoas, propulsão a combustão de querosene, peso pesado)
# - Helicóptero (aéreo, cabe até 6 pessoas, peso médio, )
# - Submarino (aquático, pesado, pode ficar submerso)
# - Barco (aquático, leve)
# - Navio (aquático, pesado, transporta centenas de pessoas)
# - Lancha (aquático, pesado, transporta dezenas de pessoas)
 
# Para chegar ao resultado, só devem ser usadas perguntas que retornem "Sim" ou "Não".
 
# Exemplo:
# É terrestre? Sim.
# Cabe apenas uma pessoa? Sim.
# É pesado? Não.
# Tem pedal? Sim.
# Então, o transporte escolhido foi a bicicleta.
 
# Para chegar ao resultado de cada uma das opções, use o modelo ilustrado na imagem em anexo. 
entrada = 1
while entrada: 
    print("Responda com 1 para sim e 0 para não.")
    entrada = int(input("É um transporte terrestre? "))
    if (entrada): # terrestre
        print("Terrestre.")
        entrada = int(input("É de peso leve? "))
        if (entrada): # peso leve
            print("Peso leve.")
            entrada = int(input("Tem pedal? "))
            if(entrada): # tem pedal
                print("BICICLETA.")
            else:# não tem pedal
                print("MOTO")
        else: # peso pesado
            print("Peso pesado.")
            entrada = int(input("Cabe só uma pessoa? "))
            if (entrada): # só cabe uma pessoa
                print("TRATOR.")
            else: # cabe mais de uma pessoa
                entrada = int(input("Tem no máximo 4 rodas? "))
                if (entrada): # tem no máximo 4 rodas
                    print("CARRO.")
                else: # tem 4 rodas ou mais
                    print("Tem 4 ou mais rodas")
                    entrada = int(input("Seu propósito é apenas transporte de pessoas? "))
                    if (entrada): # transporta apenas pessoas
                        print("ÔNIBUS.")
                    else: # transporta pessoas e cargas
                        print("Transporta pessoas e cargas.")
                        entrada = int(input("É um transporte ferroviário? "))
                        if (entrada): # ferroviário
                            print("TREM.")
                        else: # rodoviário
                            print("CAMINHÃO.")
    else: # aéreo
        entrada = int(input("É um transporte aéreo? "))
        if (entrada):
            print("Transporte aéreo.")
            entrada = int(input("É de peso leve? "))
            if (entrada): # peso leve
                print("Peso leve.")
                entrada = int(input("Comporta no máximo duas pessoas? "))
                if (entrada): # duas pessoas
                    print("PARAQUEDAS.")
                else: # mais de duas pessoas
                    print("BALÃO.")
            else: # peso pesado
                print("Peso pesado.")
                entrada = int(input("Faz pouso e decolagem verticalmente? "))
                if (entrada): # faz pouso e decolagem na vertical
                    print("HELICÓPTERO.")
                else: # não faz pouso e decolagem na vertical
                    print("AVIÃO.")
        else: # aquático
            print("Transporte aquático.")
            entrada = int(input("É de peso leve? "))
            if (entrada): # peso leve
                print("BARCO.")
            else: # peso pesado
                print("Peso pesado.")
                entrada = int(input("Pode ficar completamente submerso? "))
                if (entrada): # fica submerso
                    print("SUBMARINO.")
                else: # não fica submerso
                    print("Fica na superfície.")
                    entrada = int(input("Transporta centenas de pessoas e muitas cargas? "))
                    if (entrada): # embarcação de grande porte
                        print("NAVIO.")
                    else: # embarcação de pequeno porte
                        print("LANCHA.")
    entrada = int(input("Deseja jogar novamente? "))