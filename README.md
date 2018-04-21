# Grupo MF

## Instalação

Instale e crie uma máquina virtual para isolar seu computador do ambiente de trabalho:

    sudo apt-get install virtualenv git build-essential python-dev
    mkdir ~/Documentos/tcc && cd ~/Documentos/tcc
    virtualenv -p python3 venv

Para utilizar a máquina virtual utilize o comando source:

    source ~/Documentos/tcc/venv/bin/activate

Clone o repósitório:

    git clone https://github.com/filipedsgn/dashboard.git

Instale o ambiente desenvolvimento para trabalhar nos códigos (PyCharm Community Edition):

    #No Ubuntu
    sudo snap install pycharm-community --classic

## Integrar IDLE com GitHub