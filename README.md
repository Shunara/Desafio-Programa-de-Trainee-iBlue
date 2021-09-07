# Introdução
Uma startup chamada Sparkify quer analisar os dados que eles vêm coletando em
músicas e atividades do usuário em seu novo aplicativo de streaming de música.
A equipe de análise está particularmente interessada em entender quais músicas os
usuários estão ouvindo. Atualmente, eles não têm uma maneira fácil de consultar seus
dados, que reside em um diretório de registros JSON sobre a atividade do usuário no
aplicativo, bem como um diretório com metadados JSON nas músicas em seu aplicativo.
Eles gostariam que um engenheiro de dados criasse um banco de dados postgres com
tabelas projetadas para otimizar consultas na análise de reprodução de músicas e trazêlo no projeto. Sua função é criar um esquema de banco de dados e um pipeline ETL para
esta análise. Você poderá testar seu banco de dados e pipeline ETL executando
consultas dadas a você pela equipe de análise da Sparkify e comparar seus resultados
com os resultados esperados.

# Descrição do projeto
Para concluir o projeto, você precisará definir tabelas de fatos e dimensões para um
esquema estelar para um determinado foco analítico e escrever um pipeline ETL que
transfere dados de arquivos em dois diretórios locais para essas tabelas em Postgres
usando Python e SQL.

# Modelo de projeto
O projeto inclui seis arquivos:
1. test.ipynb exibe as primeiras linhas de cada tabela para que você verifique seu
banco de rq
2. create_tables.py drop e crie suas tabelas. Você executa este arquivo para
redefinir suas tabelas antes de cada vez que você executar seus scripts ETL.
3. etl.ipynb lê e processa um único arquivo e carrega os dados em suas tabelas.
Este notebook contém instruções detalhadas sobre o processo ETL para cada uma
das tabelas. song_datalog_data
4. etl.py lê e processa arquivos e os carrega em suas tabelas. Você pode preencher
isso com base no seu trabalho no notebook ETL. song_datalog_data
5. sql_queries.py contém todas as suas consultas sql, e é importado para os últimos
três arquivos acima.
6. README.md fornece discussão sobre o seu projeto

# Scripts em python:
* create_tables.py = Exclui eventos anteriores e cria novas tabelas
* sql_queries.py = Todas as consultas feitas no processo ETL
* etl.py = Ler todos os arquivos .json e carrega-os nas tabelas

# Tabelas existentes no Banco de Dados

* songplays = Valores no banco de dados associados às músicas reproduzidas pelos usuários
* usuários = usuários do app
* músicas = músicas existentes no banco de dados
* artistas = artistas existentes no banco de dados
* tempo = valores de tempo existentes no banco de dados

