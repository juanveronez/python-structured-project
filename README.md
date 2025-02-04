# Data Project Starter Kit

## Sobre o Projeto

A parte técnica do projeto se trata de uma ETL responsável por receber um grupo de arquivos Excel de mesmo formato e consolidar em um único Excel.

Este é um projeto criado com base no Workshop "Como estruturar um projeto de dados do Zero" do [Luciono Filho](https://github.com/lvgalvao) e o Ebook de mesmo tema. Se tratando de um projeto prático mostrando boas práticas e conceitos ideias para uma estrutura de projeto.

## Começando

### Pré-requisitos

- **Git e GitHub**: Usados para o versionamento do projeto, necessário para fazer o clone do projeto caso deseje. [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).

- **Pyenv**: É usado para gerenciar versões do Python. [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation). Vamos usar nesse projeto o Python 3.11.3. Para usuários Windows, é recomendado assistirem esse tutorial [Youtube](https://www.youtube.com/watch?v=TkcqjLu1dgA).

- **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências. [Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation).Se você é usuário Windows, recomendo assistir esse vídeo: [Youtube](https://www.youtube.com/watch?v=BuepZYn1xT8). Que instala o Python, Poetry e VSCode. Mas um simples comando PIP INSTALL POETRY já resolve.

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/juanveronez/python-structured-project.git
cd python-structured-project
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
poetry env use 3.12.1
source .venv/bin/activate
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```

8. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões ou feedbacks:

- **Juan Monteiro Veronez** - [juan.monteirov@gmail.com](mailto:juan.monteirov@gmail.com)
