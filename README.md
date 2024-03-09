:hammer: Desafio Fabrica 2024 :hammer:

<h4>Essa aplicao serve para cadastrar as informacoes nutricionais de um alimento no banco de dados.

<h4> Para instalar a aplicação é necessário um ambiente de desenvolvimento, na pasta da aplicao e no seu terminal digite :python -m venv venv

<h4> Depois é necessário ativar, digite:   .\venv\Scripts\activate

<h4> Para iniciar o servidor da aplicação digite: python manage.py runserver

<h4> Para usar é necessário fazer requisições, para isso eu utilizei o software Insomini (Para download https://insomnia.rest/download)



<h4> Ja no insomnia, lembre-se de verificar se a url está assim => 127.0.0.1:8000/api/nutri/

<h4> Feito isso podemos usar os 4 métodos: GET, POST, PUT, Delete

<h4> GET = vai te retornar os alimentos cadastrados 
https://prnt.sc/jWX5GgA1_SZV

<h4> POST = vamos utilizar para cadastrar os alimentos no banco de dados 
para fazer isso temos que passar um parametro name e depois o nome do alimento em ingles

https://prnt.sc/oORdKxKF4fxA

se retornar 201, o alimento foi incluido com sucesso no banco de dados

<h4> PUT = para utilizar o put, precisamos passar o id na url, seguida do json com o campo que queremos alterar

https://prnt.sc/sAqhme-3hmGD  

<h4> DELETE = Para ultilizar o delete, precisamos passar o id na url, em seguida ele apaga os dados do alimento no banco de dados, junto com o seu id</h4>

<H4>Obrigado por utilizar minha aplicação, duvidas entre em contato 83 99124-3877 </h4>

