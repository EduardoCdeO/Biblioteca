<h1 align="center">📖📚&nbsp Biblioteca &nbsp📖📚</h1>
Em meio aos meus estudos, foi produzido este projeto de sistema de biblioteca feito para conhecer tecnologias novas e aprimorar minhas habilidades nas que eu já tinha conhecimento. O intuito deste sistema é de gerenciar seus livros e empréstimos.

## :sparkles: Funcionalidades ##
- Sistema de cadastro e login
- Cadastro de categoria
- Cadastro de livros com imagem
- Modificar livros cadastrados
- Empréstimo de livros
- Devolução de empréstimo
- Histórico de empréstimo
- Avaliação de empréstimo

## :rocket: Tecnologias ##

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite3](https://docs.djangoproject.com/en/4.2/ref/databases/#sqlite-notes)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [Bootstrap](https://getbootstrap.com/)
- [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

## Imagens de exemplo do projeto:
<img src="/Imagens-Projeto/Imagem1.jpeg">
<hr>
<img src="/Imagens-Projeto/Imagem2.jpeg">
<hr>
<img src="/Imagens-Projeto/Imagem3.jpeg">
<hr>
<img src="/Imagens-Projeto/Imagem4.jpeg">
<hr>
<img src="/Imagens-Projeto/Imagem5.jpeg">

# Clonando o Projeto
Abra Git Bash.<br>
Altere o diretório de trabalho atual para o local em que deseja ter o diretório clonado.
```bash
git clone https://github.com/EduardoCdeO/Biblioteca.git
```

# Configurando ambiente virtual(opcional, mas recomendado)
Abra seu terminal e entre na pasta (altere o caminho-do-diretório pelo nome do local em que você clonou o repositório)<br>
```bash
cd caminho-do-diretório/Biblioteca
```
## Criando o ambiente virtual:
```bash
python -m venv venv
```
## Ativando o ambiente virtual:

No Windows:
```bash
venv\Scripts\activate
```

No macOS/Linux:
```bash
source venv/bin/activate
```

# Instale as dependências
```bash
pip install -r requirements.txt
```

# Configure o banco de dados
```bash
python manage.py migrate
```

# Inicie o servidor
```bash
python manage.py runserver
```

## A aplicação vai inicializar em <http://127.0.0.1:8000/auth/cadastro/>
