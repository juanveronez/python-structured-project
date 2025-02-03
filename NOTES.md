# 1. Python Version (`Pyenv`)

A versão do Python é um dos primeiros pontos importantes de se notar quando estamos começando um projeto ou assumindo um projeto legado. Principalmente pelo fato de que o Python só se compromete a fazer correções de 3 versões anteriores ex: (3.12 (atual), 3.11 e 3.10), **sendo assim um projeto anterior pode apresentar riscos de vulnerabilidades!**

Para garantir a versão do Python o ideal é termos um arquivo `.python-version` no projeto, o ideal é usar uma solução de Env como `pyenv` para isso.

# 2. Project ENV (`Poetry`)

Outro problema comum quando lidamos com projetos Python é criarmos projetos em que dependências podem variar dependendo do desenvolvedor, ou ainda, um mesmo desenvolvedor lidar com projetos distintos. Porém, podemos fazer isso apenas usando `venv`, ou usando soluções mais complexas como o **Poetry**. Atualmente, o mais usado é o Poetry pois ele facilita o setup de projetos e torna sua estrutura mais concisa.

**Para iniciar um projeto com Poetry**:
`poetry init`

**Para definir a versão do Python e criar um venv inicial (OBRIGATÓRIO!)**:
`poetry env use <version>`
