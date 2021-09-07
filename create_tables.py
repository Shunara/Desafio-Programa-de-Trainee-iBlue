import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """Criando o banco de dados spartifydb.
    Se ele já existir, deleta-o e cria um novo.
    Retorna:
        cursor(psycopg2.cursor): The psycopg2 cursor
        connection(psycopg2.connection): The sparkifydb connection
    """
    # Conectando-se ao banco de dados padrão
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=paris"
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Criando o banco de dados sparkfydb com decodificação UTF-8
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"
    )

    # Encerrando a conexão com o banco de dados padrão
    conn.close()

    # Conectando-se ao banco de dados sparkfy
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=postgres password=paris"
    )
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """Leia DROP queries de `sql_queries.drop_table_queries` e executa-os.
    Argumentos:
        cur (psycopg2.cursor): O cursor psycopg2
        filepath (str): O local do arquivo de música
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Leia DROP queries de `sql_queries.drop_table_queries` e executa-os.
    Argumentos:
        cur (psycopg2.cursor): O cursor psycopg2
        conn (psycopg2.connection): A conexão com o Banco de Dados
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()