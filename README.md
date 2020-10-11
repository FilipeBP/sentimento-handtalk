# Análise de sentimentos
Repositório para o processo seletivo da HandTalk, em que o objetivo é realizar um modelo de predição para análise de sentimentos (felicidade, tristeza ou raiva)

Em analyzing.ipynb, está o treinamento do modelo.

Tem um exemplo prático do uso do modelo em using_model.ipynb.

## Preparação
1. Realizar o git clone;
2. Ir no terminal, dentro da pasta em que o repositório foi clonado;
3. Instalar bibliotecas necessárias (em um ambiente virtual, ou não);

`pip install -r requirements.txt`

4. É necessário ter o [Node](https://nodejs.org/en/) instalado;
5. Ir para pasta frontend;

`cd frontend`

6. Realizar a instalação das bibliotecas;

`npm install`

7. Realizar a instalação do vue.

`npm install -g @vue/cli`

## Uso

### Backend
1. Em um terminal, ir para pasta de backend;
2. Rodar o comando para começar o servidor do backend;

`flask run`

3. O link irá aparecer no terminal, provavelmente será http://127.0.0.1/5000/, mas não é necessário acessar o servidor do backend.

### Frontend
1. Em outro terminal (deixar o terminal do backend aberto), ir para a pasta de frontend;
2. Rodar o comando para começar o servidor do frontend;

`npm run serve`

3. Provavelmente, a webpage estará em http://127.0.0.8080/, caso não seja esse, olhar no terminal.