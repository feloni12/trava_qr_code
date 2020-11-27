import gpiozero

def setup_1():
    x = str(input())

    z = open(r".\trava\pass\pass1.txt", 'w')
    z.write(str(x))
    z.close()

def input_1():
    x = str(input())

    z = open(r".\trava\pass\pass2.txt", 'w')
    z.write(str(x))
    z.close()

def comparacao():

    RELAY_PIN=25
    relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)
    lcd = CharLCD(cols= 16, rows=2, pin_rs = 1, pin_e = 6, pins_data=[3, 5] )

    q = open(r".\trava\pass\pass1.txt", "r")
    w = open(r".\trava\pass\pass1.txt", "r")

    try:
        t = q.read()
        y = w.read()

    finally:
        if t == y:
            print("Abrindo...")
            relay.on()

        else:
            print("Tente novamente.")
            relay.off()

input_1()
comparacao()




