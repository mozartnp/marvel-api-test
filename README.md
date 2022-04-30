# marvel-api-test

Consumindo a API da Marvel com Python.

A api da Marvel está em https://developer.marvel.com/docs

Leia também https://developer.marvel.com/documentation/authorization


## Autorização

Gere um apikey no site da Marvel.

```
publicKey: 1234
privateKey: abcd
ts: 1
```

ts é timestamp

Você precisará gerar um outro token em md5.

A partir do site https://www.md5hashgenerator.com/ faça a concatenação de


`md5(ts+privateKey+publicKey)`

Ex: `1abcd1234`

Resultado: `ffd275c5130566a2916217b101f26150`

```
apikey=1234
ts=1
hash=ffd275c5130566a2916217b101f26150
```

Exemplo de endpoint:

http://gateway.marvel.com/v1/public/characters?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150


Veja os demais endpoints em https://developer.marvel.com/docs


## API REST

```
GET    - pode passar dados no cabeçalho da requisição, ex: /?search=palavra, /?name=Aslam&city=Narnia, também conhecido como query_params
POST   - envia os dados no corpo da requisição... veja também formData
PUT    - edita os dados totalmente, deve editar todos os campos
PATCH  - edita os dados parcialmente, pode editar apenas alguns campos, mesmo sendo obrigatório os demais
DELETE - deleta uai
```


## Este projeto foi feito com:

* [Python 3.10.2](https://www.python.org/)
* [Django 4.0.2](https://www.djangoproject.com/)
* [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/mozartnp/marvel-api-test.git
cd marvel-api-test
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
```

## Links

* [rich.readthedocs.io](https://rich.readthedocs.io/en/stable/index.html)
* [docs.python-requests.org](https://docs.python-requests.org/en/latest/)
