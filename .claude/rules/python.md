---
paths:
  - "**/*.py"
---

# Boas práticas de Python

- Siga a versão de Python, as convenções e as ferramentas já adotadas pelo projeto. Preserve interfaces e comportamentos existentes, a menos que a tarefa peça uma mudança.
- Prefira a solução mais simples que atenda aos requisitos. Evite dependências, abstrações e refatorações sem necessidade concreta.
- Use `snake_case` para funções e variáveis, `PascalCase` para classes e `UPPER_SNAKE_CASE` para constantes. Siga PEP 8 e a formatação do projeto, incluindo quatro espaços por nível de indentação.
- Mantenha funções coesas e responsabilidades claras. Evite duplicação relevante, aninhamento excessivo, efeitos colaterais inesperados e estado global mutável.
- Prefira construções idiomáticas e diretas. Use comentários para explicar decisões ou restrições não óbvias e mantenha-os alinhados ao código.
- Adicione type hints às interfaces públicas e onde os tipos esclareçam o contrato. Use tipos compatíveis com a versão de Python do projeto; evite `Any` e conversões que escondam incompatibilidades.
- Documente módulos, classes e funções públicas quando a docstring esclarecer propósito, argumentos, retorno ou exceções; não repita o código.
- Trate exceções específicas; não use `except:` amplo nem ignore erros silenciosamente. Preserve a causa com `raise ... from exc` quando fizer sentido.
- Use `with` para gerenciar arquivos, conexões e outros recursos. Evite valores padrão mutáveis como `[]` e `{}`; use `None` e crie o valor dentro da função.
- Não inclua segredos no código nem exponha dados sensíveis em erros ou logs. Valide entradas não confiáveis antes de usá-las em consultas, caminhos, comandos ou respostas.
- Prefira bibliotecas padrão e dependências já usadas pelo projeto. Escolha algoritmos adequados e otimize quando houver uma necessidade observável, preservando a clareza.
- Considere casos-limite e caminhos de erro. Quando apropriado à tarefa e ao fluxo do projeto, cubra o comportamento com testes focados e execute as verificações relevantes.
