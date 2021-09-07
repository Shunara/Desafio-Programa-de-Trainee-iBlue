# Excluindo tabelas

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS usuarios"
song_table_drop = "DROP TABLE IF EXISTS musicas"
artist_table_drop = "DROP TABLE IF EXISTS artistas"
time_table_drop = "DROP TABLE IF EXISTS tempo"

# Criando tabelas

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id serial primary key,
    start_time timestamp not null,
    user_id varchar not null,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int not null,
    location varchar,
    user_agent text
)
""")

user_table_create = ("""
CREATE TABLE usuarios(
    user_id int primary key,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
)
""")

song_table_create = ("""
CREATE TABLE musicas(
    song_id varchar primary key,
    title varchar not null,
    artist_id varchar not null,
    year int,
    duration float
)
""")

artist_table_create = ("""
CREATE TABLE artistas(
    artist_id varchar primary key,
    name varchar not null,
    location varchar,
    lattitude float,
    longitude float
)
""")

time_table_create = ("""
CREATE TABLE tempo(
    start_time timestamp primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
)
""")

# Inserindo valores

songplay_table_insert = ("""
INSERT INTO songplays(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO usuarios(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO musicas(song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artistas(artist_id, name, location, lattitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO tempo(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# Achando músicas

song_select = ("""
select s.song_id songid, s.artist_id artistid
from musicas s inner join artistas a on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s
""")

# Consultando listas

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]