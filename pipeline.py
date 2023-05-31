import pandas as pd
import requests
import psycopg2
from prefect import task, Flow
import os

@task
def extract_data():
    url = "https://dadosabertos.ans.gov.br/FTP/Base_de_dados/Microdados/dados_dbc/beneficiarios/operadoras/"
    response = requests.get(url)

    with open("dados_ans.csv", "w") as file:
        file.write(response.content.decode("utf-8"))

    data = pd.read_csv("dados_ans.csv", delimiter=";", encoding="utf-8")
    return data

@task
def load_data(data):
    conn = psycopg2.connect(database="dbname", user="user", password="password", host="localhost", port="5432")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS dados_brutos
        (cd_contr INTEGER,
        descricao TEXT,
        qtd_planos INTEGER);""")
    conn.commit()

    for index, row in data.iterrows():
        cur.execute("INSERT INTO dados_brutos (cd_contr, descricao, qtd_planos) VALUES (%s, %s, %s)", (row['cd_contr'], row['descricao'], row['qtd_planos']))
    conn.commit()

    cur.close()
    conn.close()

@task
def read_sql_query(filepath: str) -> str:
    with open(filepath, "r") as file:
        query = file.read()
    return query

@task
def create_derived_table():
    # Conecte-se ao PostgreSQL.
    conn = psycopg2.connect(
        database="dbname",
        user="user",
        password="password",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()

    # Leia a consulta SQL do arquivo planos_cat.sql.
    script_dir = os.path.dirname(__file__)
    query_path = os.path.join(
        script_dir, "pipeline", "ans", "models", "planos_cat.sql"
    )

    with open(query_path, "r") as file:
        query = file.read()

    # Execute a consulta SQL e faça commit.
    cur.execute(query)
    conn.commit()

    # Feche a conexão e o cursor.
    cur.close()
    conn.close()
    
with Flow("ANS_pipeline") as flow:
    data = extract_data()
    load_data(data)
    create_derived_table()

flow.run()