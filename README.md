# FastCRUD 

## Descrição do Projeto
O projeto `FastCRUD` tem como objetivo aplicar conceitos relacionados a `manipulação de dados` através das quatro operações básicas (CRUD), respectivamente:

* Create - Inserção de dados
* Read - Leitura de dados
* Update - Atualização de dados
* Delete - Exclusão de dados

Além disso, seu escopo consiste nas diferenças entre o emprego de bancos de dados relacionais (SQL) e bancos de dados não-relacionais (NoSQL), em termos de desempenho, escalabilidade e flexibilização.

## Funcionalidades 
O projeto consiste em uma simples interface de usuário, utilizando JavaScript, HTML e CSS, onde é possível realizar as quatro operações mencionadas na descrição do projeto. 

Além disso, o servidor da aplicação foi interamente construído utilizando-se Python e FastAPI, utilizando banco de dados relacional (MySQL) e expandindo-se para banco de dados não-relacional (MongoDB), constituindo duas formas diferentes de se persistir dados.

## Pré-requisitos
Para que seja possível executar eficientemente o projeto e comparar as diferenças de funcionalidade entre os diferentes tipos de bancos de dados, o usuário deve ter instalado as seguintes dependências em sua máquina:

⚠️ [Python](https://www.python.org/downloads/)

⚠️ [MySQL](https://www.mysql.com/downloads/)

⚠️ [MongoDB](https://www.mongodb.com/try/download/community)

## Como rodar a aplicação ▶️
1. No terminal, clone o projeto:
    ```
    git clone https://github.com/HenriqueCosta05/FastAPI_CRUD.git
    ```
2. Navegar no diretório backend e criar o ambientes virtual de desenvolvimento, aqui nomeado de backend:
    ```
    cd back

    python -m venv backend 
    ```
3. Salvar as dependências necessárias para o funcionamento do projeto no ambiente de desenvolvimento:

```python
    pip install fastapi uvicorn # garante que algumas dependências sejam instaladas devidamente antes de salvá-las.
    pip freeze > requirements.txt
```

4. Ativar o ambiente de desenvolvimento python, dentro da pasta `back`:
    ```python
     # Windows
    backend-services\Scripts\activate

    # Linux ou MacOS
    source backend-services/bin/activate
    ```
5. Executar a aplicação, executando-se os seguintes comandos:

```
    uvicorn main:app --reload --port 8000
```

6. Abrir outro terminal, navegar para a pasta `front` e ativar o live-server.

```javascript
cd frontend
npx live-server //Aqui, poderá ser requerido instalar o live-server, caso seja a primeira vez que o usuário o utilize.
```

### Como alternar entre diferentes bancos de dados na aplicação?
No diretório `back`, dentro do arquivo principal, `main.py`, temos a seguinte estrutura de importações:

```python

from fastapi import FastAPI
from models import Item
from SQL.controllers import create_item, get_all_items, update_item, delete_item
from NoSQL.controllers import create_item, get_all_items, update_item, delete_item
from fastapi.middleware.cors import CORSMiddleware

```

Dependendo da necessidade, o usuário pode usar um banco de dados relacional, no caso, o `MySQL`, deixando a estrutura de importações da seguinte forma:

```python
from fastapi import FastAPI
from models import Item
from SQL.controllers import create_item, get_all_items, update_item, delete_item
#from NoSQL.controllers import create_item, get_all_items, update_item, delete_item
from fastapi.middleware.cors import CORSMiddleware
```

Caso queira-se utilizar o MongoDB:

```python
from fastapi import FastAPI
from models import Item
#from SQL.controllers import create_item, get_all_items, update_item, delete_item
from NoSQL.controllers import create_item, get_all_items, update_item, delete_item
from fastapi.middleware.cors import CORSMiddleware
```

 
> [!TIP]
> Basicamente, adiciona-se um comentário com `#` para alternar entre os diferentes bancos de dados. 


> [!WARNING]
> Como estamos tratando de diferentes bancos de dados, cada banco terá seus próprios dados sendo tratados de diferentes formas, o que significa que o usuário não poderá recuperar um dado similar entre os dois bancos de dados.


