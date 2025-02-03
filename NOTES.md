# 1. Python Version (`Pyenv`)

A versão do Python é um dos primeiros pontos importantes de se notar quando estamos começando um projeto ou assumindo um projeto legado. Principalmente pelo fato de que o Python só se compromete a fazer correções de 3 versões anteriores ex: (3.12 (atual), 3.11 e 3.10), **sendo assim um projeto anterior pode apresentar riscos de vulnerabilidades!**

Para garantir a versão do Python o ideal é termos um arquivo `.python-version` no projeto, o ideal é usar uma solução de Env como `pyenv` para isso.

# 2. Project ENV (`Poetry`)

Outro problema comum quando lidamos com projetos Python é criarmos projetos em que dependências podem variar dependendo do desenvolvedor, ou ainda, um mesmo desenvolvedor lidar com projetos distintos. Porém, podemos fazer isso apenas usando `venv`, ou usando soluções mais complexas como o **Poetry**. Atualmente, o mais usado é o Poetry pois ele facilita o setup de projetos e torna sua estrutura mais concisa.

**Para iniciar um projeto com Poetry**:
`poetry init`

**Para definir a versão do Python e criar um venv inicial (OBRIGATÓRIO!)**:
`poetry env use <version>`

# 3 GIT e GitHub

O uso de ferramentas de versionamento é algo excencial para conseguir ter o controle do projeto, do desenvolvimento do que foi feito e ter uma organização melhor. Importante notar que o GIT funciona bem para arquivos de texto, como arquivos com código, não arquivos binários.

Além disso, ferramentas como GitHub são serviços de "hospedagem" de projetos GIT, quase como um YouTube, que é usado para hospedar vídeos.

Além disso, podemos usar ferramentas de CI/CD para que os projetos controlados no Git sejam integrados de forma mais simples e tenham menos chance de falha ao ocorrerem atualizações, isso pode ser feito por Hooks.

## .gitignore

Um dos pontos comuns em projetos que usam git é termos arquivos que não queremos que sejam salvos no git, seja por seu tamanho ou por não serem necessários, para isso criamos o GitIgnore.

Porém, como criá-lo na mão pode ser complexo podemos usar ferramentas como o [gitignore.io](https://www.toptal.com/developers/gitignore), que já nos trás uma lista pronta, com base na tecnologia utilizada (por exemplo, Python).
