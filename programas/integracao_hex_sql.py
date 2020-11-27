import random
from time import sleep, strftime, localtime
import sqlite3
from sqlite3 import Error
import qrcode as qrc
import os
from PIL import Image

y = []
 
#código Hex

def hex():

    z = "%06x" % random.randint(0x0, 0xFFFFFFFFFFFFFFFF)         
    sleep(2)
    return(z)

    #data do dia atual

def calendario():
    x = strftime('%Y-%m-%d %H:%M', localtime())
    return(x)

    #SQLite
    #Cria a conexão entre Python e tabela
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

    #é criada uma linha na tabela
def insert_hex(conn, code):
    sql = ''' INSERT INTO hexcode_04(hex, data)
            VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, code)
    conn.commit()
    return cur.lastrowid

y = hex()

z = open(r".\trava\Hexcode\hexcode.txt", "w")
z.write(str(y))
z.close() 

def main():
    database = r".\trava\db\codigo_hex_v1.db"

    #é criada outra conexão com a database, desta vez para editar uma tabela
    conn = create_connection(database)
    with conn:
        #adiciona à tabela o código e a data de hoje
        code = (y, calendario())
        code_id = insert_hex(conn, code)

#criação do código QR

qr = qrc.QRCode(
    version=1,
    error_correction=qrc.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5)

qr.add_data(y)
qr.make(fit=True)
    
im = qr.make_image(fill='black', back_color='white')
im.save(r".\trava\Códigos QR\qrcode.png")

if __name__ == '__main__':
    main()