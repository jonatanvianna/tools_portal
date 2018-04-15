## Diretiva App

Aplicação que oferece uma ferramenta para comunicação de diretivas temporárias entre equipes de forma assíncrona.


#### Para rodar localmente 

```
$ git clone https://github.com/jonatanvianna/tools_portal.git

$ cd tools_portal

$ python -m venv env

$ source env/bin/activate

$ pip install -r requirements.txt

$ cd src/

$ python manage.py runserver

```

##### Default user

O usuário administrator padrão é ```admin``` e a senha ```djangoadmin```

Ou é possível criar seu próprio superuser, basta rodar o comando abaixo e seguir os passos para configurar.

```$ python manage.py createsuperuser```


##### Dados de exemplo

A aplicação vem com dados fictícios pré preenchidos para demonstração de uso.
