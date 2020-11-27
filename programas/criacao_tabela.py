import sqlite3
from sqlite3 import Error
import random


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return(conn)

def create_table(conn, create_table_sql):

    try:
        q = conn.cursor()
        q.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r".\trava\db\codigo_hex_v1.db"
    
    sql_hexcode_table = f""" CREATE TABLE hexcode_04 (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        hex TEXT UNIQUE,
                                        data TEXT NOT NULL                                        
                                    ); """

    # conecta com a database
    conn = create_connection(database)

    # cria a tabela hexcode
    if conn is not None:
        create_table(conn, sql_hexcode_table)
    else:
        print("Erro. Não foi possível conectar com a database.")

if __name__ == '__main__':
    main()