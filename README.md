# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Farm Sense

## IARS

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Tiago Martins</a>
- <a href="https://www.linkedin.com/in/lucas-castro-32263bb5 ">Lucas Costa dos Santos Castro</a>
- <a href="https://www.linkedin.com/in/mauricio-cortes-5488a61a9/">Mauricio Cortes</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

A temperatura e a umidade são fatores cruciais no cultivo de uvas, influenciando diretamente a qualidade e a produtividade da colheita. Visando otimizar a irrigação e auxiliar os produtores na tomada de decisões, desenvolvemos um sistema que analisa as condições da fazenda nesses quesitos. O objetivo é compreender melhor a necessidade de irrigação, contribuindo para práticas agrícolas mais eficientes e sustentáveis.

Nosso sistema permite a inserção de informações provenientes de sensores de temperatura e umidade, que são armazenadas de forma persistente em um banco de dados Oracle. As principais funcionalidades incluem:

- **Análise Imediata**: Oferece uma indicação em tempo real do status da plantação com base nas últimas informações adicionadas, permitindo ações rápidas diante de mudanças climáticas.
- **Análise Mensal Completa**: Gera relatórios detalhados de todos os meses do ano, identificando quais períodos apresentam menor necessidade de irrigação. Isso fornece uma visão ampla para previsão de custos e planejamento do momento ideal para o plantio.
- **Relatórios em JSON**: Utiliza dicionários para estruturar os dados em formato JSON, facilitando a integração com outras ferramentas e sistemas.
- **Registro de Log**: Grava todas as ações realizadas em arquivos de texto (.txt), possibilitando a consulta posterior e o acompanhamento das atividades no sistema.
- **Ferramentas de Teste**: Inclui funções para limpar completamente a base de dados e inserir dados em massa, suportando testes extensivos e análise de históricos de vários anos.

Este projeto apresenta uma solução eficaz para um problema específico do agronegócio, integrando os conteúdos estudados sobre Python e bancos de dados Oracle. Atendemos a todos os requisitos estabelecidos, desde a utilização de subalgoritmos com passagem de parâmetros até a manipulação de diferentes estruturas de dados e arquivos. Além disso, buscamos trazer inovação e contribuir para a eficiência na gestão de recursos hídricos na produção de uvas.

## 📁 Estrutura de pastas

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Deve conter o arquivo env com as configurações de banco de dados

- <b>scripts</b>: Contém a criação de tabelas do banco de dados

- <b>src</b>: Contém todo o código fonte do projeto.

- <b>src/database</b>: Contém arquivos que contectam-se ao banco de dados.

- <b>src/utils</b>: Contém funções utilizarias que podem ser compartilhada entre todos os arquivos.

- <b>src/data</b>: Contém os relatórios e o log gerados pelo sistema.

- <b>README.md</b>: Contém as informações que devem ser lidas por quem deseja executar ou compreender o projeto.

## 🔧 Como executar o código

- <b>Banco de dados</b>: As informações de usuario senha e dns devem ser inseridas no arquivo src/database/connection.

- <b>Instalação de dependências</b>: Deve ser criado o .venv do projeto.

- <b>Instalação de dependências</b>: Deve ser executado o pip install de todas as dependências citadas em requirements.txt.

- <b>Execução do sistema</b>: Após os passos anteriores concluídos com sucesso, o arquivo main.py pode ser executado.


## 🗃 Histórico de lançamentos

* 1.0 - 15/10/2024


