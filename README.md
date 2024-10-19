# Transformador de Registros de Alunos

Este projeto transforma dados de alunos, a partir de um arquivo de texto, em um formato específico para ser utilizado em outras aplicações. O programa lê o arquivo de entrada contendo a matrícula e o nome dos alunos, gera um registro formatado para cada aluno, e salva os resultados em um novo arquivo de saída.

# Funcionalidades

- Leitura de um arquivo de texto (`.txt`) com matrícula e nome dos alunos.
- Geração de registros formatados em um padrão específico.
- Salvamento dos registros transformados em um novo arquivo de saída.
- 
## Formato do Arquivo de Entrada

O arquivo de entrada deve ter o formato:
matricula, nome
2345678, João Silva

87654321, Maria Souza


Os registros gerados seguirão o seguinte padrão:
4+1+I[[000000000000{matricula}[[[1[1[1[[[[[2[[[[[0[{nome}[[[[[

## Como Usar

1. Clone o repositório para o seu ambiente local.
2. Crie um arquivo de texto (`.txt`) com as informações dos alunos, conforme o formato especificado.
3. Execute o programa:

   ```bash
   python nome_do_arquivo.py
