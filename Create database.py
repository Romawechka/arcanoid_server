import psycopg2

conn = psycopg2.connect(host="localhost", user="student", password="study", dbname="postgres")
cursor = conn.cursor()

cursor.execute("""create table public.Arcanoid_game (
                    id varchar not null PRIMARY KEY,
                    login varchar not null,
                    password varchar not null,
                    points varchar,
                    almaz varchar);""")


cursor.execute("""insert into public.Arcanoid_game values(1, 'uvolka', '1234')""")
conn.commit()
conn.close()