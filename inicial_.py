import gpiozero
from time import sleep
from RPLCD import CharLCD

while True: 
    exec(open(r".\trava\programas\integracao_hex_sql.py").read())
    exec(open(r".\trava\programas\qrcode_leitor.py").read())


    RELAY_PIN=25
    relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)
    lcd = CharLCD(cols= 16, rows=2, pin_rs = 1, pin_e = 6, pins_data=[3, 5] )

    
    z = open("hexcode.txt", 'r') 
    x = open("codigo_hexQR.txt", 'r')
    
    try:
        w = z.read()
        v = x.read()

    finally:
        if w == v:
            print("Abrindo...")
            relay.on()
        else:
            print("Tente novamente.")
            relay.off()

sleep(900)


