# REMOTE SHUTDOWN SERVER UNIX

O programa foi criado com o intuito de desligar remotamente servidores UNIX utilizando o SSH.


## Passo a passo...

###Instalando dependencias
(pip install -r requirements.txt)

###Criando arquivo .json
Por default o programa reconhece o arquivo maquinas.json. Ele deve possuir cinco campos obrigatórios seguindo o modelo abaixo:

```
[
    {
        "hostname": "IP address",
        "port": 22,
        "username": "Usuário root",
        "password": "Senha",
        "OS": "Sistema Operacional"
    },

    {
        "hostname": "IP address",
        "port": 22,
        "username": "Usuário root",
        "password": "Senha",
        "OS": "Sistema Operacional"
    }
]
```

###Alterando o config
Caso deseje mudar o nome do arquivo .json, ele estará no config.py

###O que deve acontecer
Se não houver erros, o programa imprimirá uma mensagem acusando sucesso.

###O que não deve acontecer
Caso haja erros, ele também acusará com uma mensagem alertando a exceção.
Existe também a possibilidade de não conseguir se conectar com a outra máquina. Caso isso acontença, aparecerá uma mensagem de timeout.

###Com o que isso funciona
O programa foi testado em máquinas UNIX de distribuição Debian e também no Freebsd.