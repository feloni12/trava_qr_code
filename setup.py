import os
import sys
from setuptools import setup, find_packages
from inicial_2 import setup_1 

#!/usr/bin/env python

# É necessário iniciar o arquivo como root
if os.getpid() != 0:
    print('ERROR: Need to run as root')
    sys.exit(1)

# Instalando os requisitos necessários
print('Realizando a instalação')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Abrindo e gerando os requisitos
print('Baixando os requerimentos do sistema.')
packages = []
for line in open('requisitos.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# Run setuptools for pip
setup(
    name='fechadura_qr_code',
    version='1.0.0',
    description='Fechadura QR code, ativada tanto por código QR como por código de segurança',
    author='ETEC CCS',
    url='https://github.com/feloni12/trava_qr_code',
    install_requires=['sqlite3', 'qrcode', 'gpiozero', 'PIL'],
    packages = find_packages(),
    install_requires=packages,
    packages=find_packages(),
)

exec(open(r".\trava\programas\criacao_tabela.py").read())
exec(open(r".\trava\programas\integracao_hex_sql.py").read())
setup_1()

sys.exit(1)