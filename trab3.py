from datetime import datetime


class Veiculos(object):
    def __init__(self, marca="", modelo="", ano=0, valor=0):
        self.codigo = ""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.status = "DISPONÍVEL"

Alu=0
Atras=0
Cad=0
Codigos = []
Marca = []
Modelo = []
Ano = []
Valor = []
Status = []


SttsI = []
SttsF = []
Locatario = []
Dias = []
Obj = []
aux = 0
Atual = datetime.now()
Dia = Atual.day
Mes = Atual.month
Anos = int(Atual.year)

while aux != 7:
    
    print(" {} \ {} \ {}\n".format(Dia, Mes, Anos))
    print("Cadastrados: {}\n".format(Cad))
    print("Alugados: {}\n".format(Alu))
    print("Atrasados: {}\n".format(Atras))
    print("escolha uma das opções abaixo:\n")
    print("1 Adicionar veículos")
    print("2 consultar veículos")
    print("3 Alugar/reservar veículos")
    print("4 devolver/liberar veículos")
    print("5 Excluir veículos")
    print("6 Avançar data atual")
    print("7 sair \n")
    aux = int(input(" "))
    print("\n")
    if aux == 1:
        print("_________________________________________")
        a = input("marca:")
        b = input("modelo:")
        c = input("ano:")
        d = input("diária:")
        print("_________________________________________\n")
        Marca.append(a)
        Modelo.append(b)
        Ano.append(c)
        Valor.append(d)
        e = len(Modelo)
        Codigos.append("00"+str(e))
        obj = Veiculos()
        obj.codigo = e
        obj.Valor = float(d)
        obj.Ano = int(c)
        obj.Modelo = b
        obj.Marca = a
        Obj.append(obj)
        Status.append(obj.status)
        SttsI.append(str(Dia)+str(Mes)+str(Anos))
        SttsF.append("")
        Locatario.append("")
        Dias.append(0)
        Cad=Cad+1
        print("\n")
    if aux == 2:
        print("")
        
        Cad=len(Codigos)
        aux2 = 0
        print("_________________________________________")
        while aux2 < Cad:
            print("Codigo: {}\n{}\n{}\n".format(Codigos[aux2], Modelo[aux2], Status[aux2]))
            aux2 = aux2 + 1
            print("_________________________________________")
        print("\nDigite 0 para ver mais detalhes")
        
        print("Digite 1 para voltar a tela Inicial")
        aux3 = int(input(" "))
        print("")
        if aux3 == 0:
            print("_________________________________________\n")
            aux2 = 0
            while aux2 < Cad:
                print("{}\n {}\n{}\n{}\nValor: R${},00 \n{}".format(Codigos[aux2], Marca[aux2], Modelo[aux2], Ano[aux2], Valor[aux2], Status[aux2]))
                aux2 = aux2 + 1
                print("_________________________________________\n")

        print("")
    if aux == 3:
        
        print("Digite 1 para alugar um veículo.")
        print("Digite 2 para reservar um veículo.")
        aux4 = input(" ")
        Alu=Alu+1
        print("")
        if aux4 == "1":
            nl = input("Nome do locatário:")
            prazo = int(input("Prazo da locação:"))
            if prazo > 30:
                print("Prazo passa dos limites.")
                prazo = input("Digite um prazo menor:")
            cd = input("Código do veículo:")
            if str(Status[int(cd)-1]) == "DISPONÍVEL":
                Dias[int(cd)-1] = prazo
                Status[int(cd)-1] = "ALUGADO"
                Locatario[int(cd)-1] = nl
                SttsI[int(cd)-1] = str(str(Dia)+str(Mes)+str(Anos))
                d = Dia + prazo
                m = Mes
                a = Anos
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                SttsF[int(cd) - 1] = str(str(d) + str(m) + str(a))
            elif str(Status[int(cd)-1]) == "ALUGADO":
                print("veículo indisponivel")
                cd = input("digite outro codigo: ")
                if str(Status[int(cd) - 1]) == "DISPONÍVEL":
                    Status[int(cd) - 1] = "ALUGADO"
                    Locatario[int(cd) - 1] = nl
                    SttsI[int(cd) - 1] = str(str(Dia) + str(Mes) + str(Anos))
                    d = Dia + prazo
                    m = Mes
                    a = Anos
                    if d > 30:
                        d = d - 30
                        m = m + 1
                        if m > 12:
                            m = m - 12
                            a = a + 1
                    SttsF[int(cd) - 1] = str(str(d) + str(m) + str(a))
                if str(Status[int(cd) - 1]) == "RESERVADO":
                    print("há sobreposição de datas e deve ser escolhido outro carro em ou outra data")
        elif aux4 == "2":
            nl = input("Nome do locatário:")
            prazo = int(input("Prazo de locação:"))
            if prazo > 30 - Dia:
                print("Prazo muito grande.")
                prazo = input("Digite um prazo menor:")
            cd = input("Código do veículo:")
            if str(Status[int(cd)-1]) == "DISPONÍVEL":
                Dias[int(cd) - 1] = prazo
                Status[int(cd)-1] = "RESERVADO"
                Locatario[int(cd)-1] = nl
                ini = (input("digite a data do inicio do aluguel sem caracteres especiais... ex: 13122017 :"))
                d = int(ini[0] + ini[1])
                m = int(ini[2] + ini[3])
                a = int(ini[4] + ini[5] + ini[6] + ini[7])
                d = d + prazo
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                SttsF[int(cd) - 1] = str(str(d) + str(m) + str(a))
        print("\n")
    if aux == 4:
        print("\n_________________________________________")
        a = len(Codigos)
        b = 0
        Alu=Alu-1
        while b < a:
            if Status[b] != "DISPONÍVEL":
                print(str(Codigos[b])+"--"+str(Modelo[b])+"--"+str(Status[b]))
                print("_________________________________________")
            b = b + 1
        print("\nDigite 1 para Devolver Veículo")
        print("Digite 2 para Liberar Veículo")
        aqw = int(input("Digite a operação desejada:"))
        print("")
        if aqw == 1:
            print("_________________________________________")
            cod = int(input("Digite o Código do veículo:"))
            Atras=Atras-1
            print("\nLocatários: ", Locatario[cod - 1])
            val = int(SttsI[cod - 1])//1000000
            d = val
            m = (int(SttsI[cod - 1]) - d*1000000) // 10000
            a = (int(SttsI[cod - 1]) - d*1000000) % 10000
            if a == Anos:
                if m > Mes:
                    print("Total a pagar: R$", (((30-d)+Dia) * float(Valor[cod - 1])))
                    Status[cod - 1] = "DISPONÍVEL"
                elif m == Mes:
                    if Dia == d:
                        print("Total a pagar: R$", (float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif Dia > d:
                        print("Total a pagar: R$", ((Dia - d) * float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif d > Dia:
                        Status[cod - 1] = "DISPONÍVEL"
            elif a < Anos:
                print("Total a pagar: R$", ((Dia + (30 - d)) * float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
            elif a > Anos:
                Status[cod - 1] = "DISPONÍVEL"
        print("_________________________________________\n")
        if aqw == 2:
            cod = int(input("Digite o Código do veículo:"))
            print("Locatários: ", Locatario[cod - 1])
            val = int(SttsI[cod - 1]) // 1000000
            d = val
            m = (int(SttsI[cod - 1]) - d * 1000000) // 10000
            a = (int(SttsI[cod - 1]) - d * 1000000) % 10000
            if a > Anos:
                Status[cod - 1] = "DISPONÍVEL"
            elif a < Anos:
                val = Dia + (30 - d)
                print("Total a pagar: R$", (val * float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
            elif a == Anos:
                if m == Mes:
                    if d == Dia:
                        print("Total a pagar: R$", (float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif d > Dia:
                        Status[cod - 1] = "DISPONÍVEL"
                    else:
                        val = Dia - d
                        print("Total a pagar: R$", (val * float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
    if aux == 5:
        vei = int(input("Digite o Código do veículo: "))
        Cad=Cad-1
        if Status[vei - 1] == "DISPONÍVEL":
            del Codigos[vei - 1]
            del Marca[vei - 1]
            del Modelo[vei - 1]
            del Ano[vei - 1]
            del Valor[vei - 1]
            del Status[vei - 1]
            del SttsI[vei - 1]
            del SttsF[vei - 1]
            del Locatario[vei - 1]
            del Obj[vei - 1]
        ve = len(Status)
        y = 1
        x = 0
        while x < ve:
            Codigos[x] = "00" + str(y)
            x = x + 1
            
    if aux == 6:
        Dia = Dia + 1
        if Dia > 30:
            Dia = Dia - 30
            Mes = Mes + 1
            if Mes > 12:
                Mes = Mes - 12
                Anos = Anos + 1
        cod = len(Status)
        while cod > 0:
            d = (int(SttsI[cod - 1])) // 1000000
            m = (int(SttsI[cod - 1]) - d * 1000000) // 10000
            a = (int(SttsI[cod - 1]) - d * 1000000) % 10000
            if Status[cod - 1] == "DISPONÍVEL":
                print()
            elif a == Anos:
                if m > Mes:
                    if ((30 - d) + Dia) > Dias[cod - 1]:
                        Status[cod - 1] = "ATRASADO"
                        Atras=Atras+1
                elif m == Mes:
                    if Dia == d:
                        Status[cod - 1] = "ALUGADO"
                    elif Dia > d:
                        if (Dia - d) > Dias[cod - 1]:
                            Status[cod - 1] = "ATRASADO"
                            Atras=Atras+1
            elif a < Anos:
                if (Dia + (30 - d)) > Prazo[cod - 1]:
                    Status[cod - 1] = "ATRASADO"
                    Atras=Atras+1
            cod = cod - 1
        print("")
       
        if aux == 7:
            break
