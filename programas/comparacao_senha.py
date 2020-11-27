z = open("pass1.txt", 'r')
x = str(input("Coloque a senha de segurança: "))

k = z.read()

if k == x:
    i = True

else:
    i = False

