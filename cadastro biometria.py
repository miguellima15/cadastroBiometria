def gerar_registro(matricula, nome):
    return f"4+1+I[[000000000000{matricula}[[[1[1[1[[[[[2[[[[[0[{nome}[[[[["

def processar_arquivo(arquivo_entrada, arquivo_saida):
    alunos = []
    try:
        with open(arquivo_entrada, "r") as arquivo:
            for linha in arquivo:
               
                matricula, nome = linha.strip().split(", ")
            
                registro = gerar_registro(matricula, nome)
                alunos.append(registro)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")
        return
    
   
    with open(arquivo_saida, "w") as arquivo:
        for aluno in alunos:
            arquivo.write(aluno + "\n")
    
    print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

# Execução do programa
arquivo_entrada = input("Digite o nome do arquivo de entrada (ex: alunos.txt): ")
arquivo_saida = "registros_alunos.txt"
processar_arquivo(arquivo_entrada, arquivo_saida)
