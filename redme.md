# Desafio de Engenharia de Dados

Este repositório contém a solução de um desafio de engenharia de dados, onde foi desenvolvida uma pipeline em Prefect para extrair, carregar e transformar dados das operadoras de planos de saúde do site da ANS. A solução consiste em extrair os dados, armazená-los em uma tabela PostgreSQL e criar uma tabela derivada usando DBT. A tabela derivada mostra o total de planos de saúde por categoria em dezembro de 2019.

## Implementação

A implementação foi realizada utilizando Python, especificamente as bibliotecas `pandas`, `requests`, `psycopg2` e `prefect`. O projeto consiste em tarefas Prefect que executam a extração dos dados, carregam os dados em uma tabela no PostgreSQL e criam uma tabela derivada no banco de dados utilizando uma consulta SQL para DBT.

As seguintes etapas foram desenvolvidas:

1. Implementação de uma função para extração dos dados através da biblioteca `requests` e `pandas`.

2. Implementação de uma função para carregar os dados no PostgreSQL usando a biblioteca `psycopg2`.

3. Implementação de uma função para criar a tabela derivada utilizando uma consulta SQL para DBT.

## Como executar

Primeiro, instale todas as dependências usando `pip`:

```
pip install pandas requests prefect psycopg2-binary
```

Em seguida, certifique-se de ter uma instância PostgreSQL em execução, e atualize as variáveis de conexão no arquivo `pipeline.py` (usuário, senha, nome do banco de dados, host e porta) com as informações corretas do seu banco de dados.

Finalmente, execute a pipeline usando:

```
python pipeline.py
```

## Resultados

Após a correta execução da pipeline, você deve ser capaz de visualizar os resultados na tabela derivada no PostgreSQL, mostrando o total de planos por categoria em dezembro de 2019.

---

### Sobre o autor

O desenvolvedor deste projeto tem uma vasta experiência trabalhando com Python e projetos de engenharia de dados, tendo colaborado com gigantes como IBM e Microsoft. Se você estiver interessado em conferir mais projetos do autor, visite o [GitHub](https://github.com/dougdotcon) e siga-o nas redes sociais.

**CTA:** Se você quer melhorar a qualidade e eficiência de seus projetos de engenharia de dados e agregar valor ao seu negócio, entre em contato diretamente com o autor ou visite o [portfólio](https://meusprojetos.uwu.ai/) para ver mais detalhes sobre projetos realizados e serviços oferecidos.

Se você tiver alguma dúvida sobre este projeto ou precisar de assistência adicional, por favor, não hesite em entrar em contato. A excelência no atendimento é uma das prioridades do autor!

---

Agradeço por sua atenção e espero que este projeto tenha sido de grande valia. Se você gostou deste projeto, não se esqueça de compartilhá-lo com seus colegas e me seguir nas redes sociais para ficar atualizado sobre novos projetos e contribuições interessantes!