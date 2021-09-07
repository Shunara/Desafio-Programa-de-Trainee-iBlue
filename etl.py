  
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Lendo um arquivo de música e
    Insere os dados de música e dos artistas na tabela
    Argumentos:
        cur (psycopg2.cursor): O cursor psycopg2
        filepath (str): O local do arquivo de música
    """
    # Abrindo o arquivo de música
    df = pd.read_json(filepath, lines=True)
    df['year'] = df['year'].apply(lambda x: x if x != 0 else None)
    df = df.replace({pd.np.nan: None, "": None})
    
    # Inserindo o arquivo de música
    song_data = df[[
        'song_id',
        'title',
        'artist_id',
        'year',
        'duration'
    ]].values[0]
    cur.execute(song_table_insert, song_data)

    # Inserindo os dados do artista
    artist_data = df[[
        'artist_id',
        'artist_name',
        'artist_location',
        'artist_latitude',
        'artist_longitude'
    ]].values[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Lendo o arquivo e
    inserindo dados às tabelas de tempo, usuários e
    Argumentos:
        cur (psycopg2.cursor): O cursor psycopg2
        filepath (str): O local do arquivo de música
    """
    # Abrindo o arquivo
    df = pd.read_json(filepath, lines=True)

    # Filtrando para a música Nextsong
    df = df[df['page'] == 'NextSong']

    # Convertendo a coluna de tempo
    t = pd.to_datetime(df['ts'], unit='ms')

    # Inserindo os valores de tempo
    time_data = pd.concat([
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday], axis=1)
    column_labels = [
        'start_time',
        'hour',
        'day',
        'week',
        'month',
        'year',
        'weekday'
    ]
    time_df = pd.DataFrame(data=time_data.values, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # Carregando a tabela de usuários
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # Inserindo os valores de usuários
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # Inserindo os valores de músia
    for index, row in df.iterrows():

        # Pegando o songid e o artistid das tabelas de música e artistas
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # Inserindo os valores de música
        songplay_data = (
            pd.to_datetime(row.ts, unit='ms'),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """Lendo todos os arquivos do diretório passado e
    executando a função específca
    Argumentos:
        cur (psycopg2.cursor): O cursor psycopg2
        conn (psycopg2.connection): A conexão com o banco de dados
        filepath (str): O local onde os arquivos devem ser processados
        func (function): A função a ser executada
    """

    # achando todos os arquivos cuja extensão seja json no diretório
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # Achando o número total de arquivos encontrados
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # Iterando e processando os arquivos
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=postgres password=paris"
    )
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()