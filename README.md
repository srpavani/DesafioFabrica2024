# :hammer: Desafio Fábrica 2024 :hammer:

Essa aplicação serve para cadastrar as informações nutricionais de um alimento no banco de dados.

## Instalação

Para instalar a aplicação é necessário um ambiente de desenvolvimento, na pasta da aplicação e no seu terminal digite:

`python -m venv venv`

Depois é necessário ativar o ambiente virtual, digite:

`.\venv\Scripts\activate`

Depois é necessário fazer as migracoes, digite:

`python manage.py makemigrations`, depois `python manage.py migrate`

Para iniciar o servidor da aplicação digite:

`python manage.py runserver`


## Uso da Aplicação

Para usar é necessário fazer requisições, para isso eu utilizei o software Insomnia (Para download [clique aqui](https://insomnia.rest/download)).

Já no Insomnia, lembre-se de verificar se a URL está assim: `127.0.0.1:8000/api/nutri/`

Feito isso, podemos usar os 4 métodos: GET, POST, PUT, DELETE

### GET

Vai te retornar os alimentos cadastrados.  
Exemplo: ![Exemplo GET](https://github.com/srpavani/DesafioFabrica2024/assets/53492119/7bf2a69b-0444-447d-8fff-5017e8e1b550)

### POST

Vamos utilizar para cadastrar os alimentos no banco de dados. Para fazer isso temos que passar um parâmetro `name` e depois o nome do alimento em inglês.  
Exemplo: ![Exemplo POST](https://prnt.sc/oORdKxKF4fxA)  
Se retornar `201`, o alimento foi incluído com sucesso no banco de dados.

### PUT

Para utilizar o PUT, precisamos passar o ID na URL, seguida do JSON com o campo que queremos alterar.  
Exemplo: ![Exemplo PUT](https://prnt.sc/sAqhme-3hmGD)

### DELETE

Para utilizar o DELETE, precisamos passar o ID na URL, em seguida ele apaga os dados do alimento no banco de dados, junto com o seu ID.

## Suporte

Obrigado por utilizar minha aplicação. Para dúvidas, entre em contato: 83 99124-3877
