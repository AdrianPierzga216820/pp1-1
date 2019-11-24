tabela = [32, 16, 5, 8, 24, 7]
with open('tabelka.txt','w') as file:
    for x in tabela:
        file.write(str(x) + '\n')