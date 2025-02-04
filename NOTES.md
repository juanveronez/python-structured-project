# Ambiente de Desenvolvimento

## 1. Python Version (`Pyenv`)

A versão do Python é um dos primeiros pontos importantes de se notar quando estamos começando um projeto ou assumindo um projeto legado. Principalmente pelo fato de que o Python só se compromete a fazer correções de 3 versões anteriores ex: (3.12 (atual), 3.11 e 3.10), **sendo assim um projeto anterior pode apresentar riscos de vulnerabilidades!**

Para garantir a versão do Python o ideal é termos um arquivo `.python-version` no projeto, o ideal é usar uma solução de Env como `pyenv` para isso.

## 2. Project ENV (`Poetry`)

Outro problema comum quando lidamos com projetos Python é criarmos projetos em que dependências podem variar dependendo do desenvolvedor, ou ainda, um mesmo desenvolvedor lidar com projetos distintos. Porém, podemos fazer isso apenas usando `venv`, ou usando soluções mais complexas como o **Poetry**. Atualmente, o mais usado é o Poetry pois ele facilita o setup de projetos e torna sua estrutura mais concisa.

**Para iniciar um projeto com Poetry**:
`poetry init`

**Para definir a versão do Python e criar um venv inicial (OBRIGATÓRIO!)**:
`poetry env use <version>`

## 3. GIT e GitHub

O uso de ferramentas de versionamento é algo excencial para conseguir ter o controle do projeto, do desenvolvimento do que foi feito e ter uma organização melhor. Importante notar que o GIT funciona bem para arquivos de texto, como arquivos com código, não arquivos binários.

Além disso, ferramentas como GitHub são serviços de "hospedagem" de projetos GIT, quase como um YouTube, que é usado para hospedar vídeos.

Além disso, podemos usar ferramentas de CI/CD para que os projetos controlados no Git sejam integrados de forma mais simples e tenham menos chance de falha ao ocorrerem atualizações, isso pode ser feito por Hooks.

### .gitignore

Um dos pontos comuns em projetos que usam git é termos arquivos que não queremos que sejam salvos no git, seja por seu tamanho ou por não serem necessários, para isso criamos o GitIgnore.

Porém, como criá-lo na mão pode ser complexo podemos usar ferramentas como o [gitignore.io](https://www.toptal.com/developers/gitignore), que já nos trás uma lista pronta, com base na tecnologia utilizada (por exemplo, Python).

# Qualidade de Código

## 1. Testes (pytest)

O conceito de testes unitários e testes de integração é algo muito importante, pois garante ao desenvolvedor segurança na hora de fazer uma implementação ou alteração em um código.

Quando criamos testes unitários testamos uma funcionalidade de forma isolada e seus possíveis resultados, podendo definir uma ou mais premissas que podem ser verdadeiras.

para rodar os testes usamos o `pytest`.

Já testes de integração testam como diferentes pedaços de um código interagem, sendo uma solução para testar de forma mais complexa. Importante notar que devemos focar mais em testes unitários que em testes de integração, por serem mais importantes e simples de serem feitos.

## 2. Padrões de Projeto (Ex: ISort, Blue e Pydocstyle)

Conceito em que aderimos o projeto a alguns padrões pré-determinados e mais conhecidos, como as PEPs, usado para que o time não "perca tempo" definindo padrões que já foram definidos antes. Muitas dessas bibliotecas ainda auxiliam para que não seja necessário corrigirmos os erros, corrigindo diretamente tudo que está fora do padrão.

Muitas dessas bibliotecas rodam apenas com o nome da lib, ou ainda o nome da lib e quais arquivos devem ser tocados. Como em `pydocstyle` e `isort .` (usa isort em todos os arquivos).

## 3. Tarefas (Taskipy)

Algo comum em projetos é termos diferentes comandos que precisam ser executados para situações diferentes, scripts para rodar o código, scripts de setup, scripts para testes, para documentação....

O grande problema é que esses comandos podem não ser triviais, quando adicionamos uma ferramenta de tarefas simplificamos o projeto, podendo usar algo como `task run` para rodar o projeto, sem precisar se preocupar com qual arquivo deve ser executado, ou qual comando.

Para isso só precisamos adicionar a biblioteca `taskipy` e criar as tasks que podem ser usadas, como por exemplo (deve ser adicionado no pyproject.toml):

```toml
[tool.taskipy.tasks]
run = "python src"
lint = "isort . && blue ."
test = "pytest -v "
```

## 4. Documentação (MKDocs)

Uma documentação trás mais profissionalismo ao projeto e clareza sobre a composição do projeto.

Quando criamos a doc com o MKDocs conseguimos criar uma doc mais robusta, como uma aplicação a parte que pode ser publicada e ficar pública ou privada (a depender da necessidade).

Quando precisamos mapear as funcionalidades do projeto podemos usar o `mkdocstrings`, usado para referenciar as funções ou classes da aplicação.

Sempre importante lembrar que o mkdocs usa MD, sendo uma estrutura simples de ser escrita.

### Alguns comandos importantes

- Criar uma doc nova: `mkdocs new .`
- Subir o server com a doc: `mkdocs serve`
- Buildar a doc: `mkdocs build`
- Publicar a doc no GitHub Pages: `mkdocs gh-deploy`

### Pluggins Úteis:

- mkdocstrings-python
- pygments
- mkdocs-material
- pymdown-extensions
- mkdocs-bootstrap38

### Mermaid

Como o MKDocs usa MDs para criação das páginas, sendo assim estruturas como a que temos abaixo são possíveis, ou outras opções usando MD.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;

```
