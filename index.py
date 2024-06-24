def dataTransfer(arqEntrada):
   
    codeQuant = []
    with open(arqEntrada, 'r') as file:
        for linha in file:
            codigo, quantidade = linha.strip().split(';')
            codeQuant.append((codigo, int(quantidade)))
    return codeQuant

def dataCreate(codeQuant, arqSaida):
    with open(arqSaida, 'w') as file:
        for codigo, quantidade in codeQuant:
            for _ in range(quantidade):
                file.write(f"{codigo}\n")

arqEntrada = 'input.txt'
arqSaida = 'output.txt'

codeQuant = dataTransfer(arqEntrada)

dataCreate(codeQuant, arqSaida)

print(f"Arquivo {arqSaida} criado com sucesso!")
