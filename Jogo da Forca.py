import random
def palavra():
    abert = open("Palavras.txt","r")
    pala = []
    for linha in abert:
        linha = linha.strip()
        pala.append(linha)

    palavra = random.choice(pala)
    tam = ["_"]*len(palavra)
    figurinha(7)
    print(tam,"\n")
    abert.close()
    return palavra

def dica(v):
    palavra = v
    dic = open("Dica.txt","r")
    Dica = []
    for linha in dic:
        linha = linha.strip()
        Dica.append(linha)
    if palavra == "BRASIL" or palavra == "PORTUGAL" or palavra == "CHINA":
        print("A dica é :",Dica[1])
    elif palavra == "GATO" or palavra == "BOI" or palavra == "BALEIA" or palavra == "TIGRE":
        print( "A dica é :", Dica[0])
    else:
        print( "A dica é :", Dica[2])
    dic.close()

def figurinha(vid):
    if vid == 7:
        print("________")
        print("|      |")
        print("|      ")
        print("|")
        print("|")
        print("|")
        
    elif vid == 6:
        print("________")
        print("|      |")
        print("|      0")
        print("|")
        print("|")
        print("|")
        
    elif vid == 5:
        print("________")
        print("|      |")
        print("|      0")
        print("|      |")
        print("|")
        print("|")
        
    elif vid == 4:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|")
        print("|")
        print("|")
        
    elif vid == 3:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|")
        print("|")
        
        
    elif vid == 2:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|")
        print("|")
        
    elif vid == 1:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     /")
        print("|")
        
    elif vid == 0:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     / \ ")
        print("|")







def pergunta(v):
    vida = 7
    palavra = v
    palavra = list(palavra)
    tam = ["_"]*len(palavra)
    print("\n")
    cert = len(palavra)
    while vida >= 1 :
        if cert == 0:
            print("Voce acertou a palavra","\n")
            break
        perg = input("Digite qual letra deseja chutar : ")
        perg = perg.upper()
        if perg not in v:
            print("Voce perdeu um ponto de vida ")
            vida -= 1
            figurinha(vida)
            print(tam)
        for i in range((len(palavra))):
            if perg in palavra[i]:
                i = i
                print('\n',"Voce acertou uma letra")
                tam[i] = perg
                figurinha(vida)
                print(tam)
                cert -= 1
                print(f"Faltam {cert} letras para acertar a palavra")
                
            else:
                i += 1
    return vida

def celeb(vi):
    if vi > 0:
        print("Parabens, voce ganhou o jogo")
    else:
        print("Infelizmente voce nao conseguiu acertar a palavra")
    print("digite um numero")
    print("1 - Sim")
    print("2 - Não")
    esco = input("Voce gostaria de jogar de novo?")
    esco = esco.upper()
    while (esco != "1") and (esco != "2"):
        esco = input("Voce gostaria de jogar de novo?(S/N)")
        esco = esco.upper()
    if esco == "1":
        print("======== O Jogo iniciou ========","\n")
        print("Voce tem que acertar antes que o boneco fique completo","\n")
        x = palavra()
        dica(x)
        y = pergunta(x)
        celeb(y)
    else:
        print("Obrigado por jogar")
        quit()
def iniciar(): 
    print("=============  Bem vindo ao jogo da forca  =============")
    print(" Digite o numero para suas respectivas funções")
    print(" 1 - iniciar")
    print(" 2 - regras")
    print(" 3 - sair")
    inic = int(input("Digite o numero: "))
    while inic < 0 or inic > 3:
        print("comando invalido por favorr digite novamente: ")
        inic = int(input("Digite o numero: "))
    if inic == 1:
        print("======== O Jogo iniciou ========","\n")
        print("Voce tem que acertar antes que o boneco fique completo","\n")
        x = palavra()
        dica(x)
        y = pergunta(x)
        celeb(y)
    elif inic == 2:
        print("O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra","\n" ,"proposta, tendo como dica o número de letras e o tema ligado à palavra. A cada letra errada, é desenhada uma parte do corpo do enforcado.")   
        print(" Digite o numero para suas respectivas funções")
        print(" 1 - voltar")
        print(" 2 - sair")
        inic1 = int(input("digite o numero: "))
        while inic1 < 1 or inic1 > 2:
            print("comando invalido por favorr digite novamente: ")
            inic1 = int(input("digite o numero: "))
        if inic1 == 1:
            iniciar()
        else:
            print("Obrigado por jogar")
            quit()
    elif inic == 3:
        print("Obrigado por jogar")
        quit()
iniciar()
