---
paths:
  - "**/*.py"
---

# Orientações para chatbots

Use estas regras ao criar ou alterar o fluxo conversacional, independentemente do provedor de modelo ou da interface (API, web, CLI ou outra). Siga a arquitetura e as dependências existentes; não introduza um framework ou provedor sem necessidade do projeto.

## Fluxo conversacional

- Mantenha separadas, na medida em que isso ajude a clareza, a interface de entrada/saída, a lógica de conversa, o acesso ao modelo e a persistência do histórico.
- Defina formatos explícitos para mensagens e respostas. Preserve o papel de cada mensagem (`system`, `user`, `assistant` ou ferramenta) e não misture instruções internas com conteúdo do usuário.
- Trate cada conversa e seu histórico de forma isolada. Não compartilhe estado de sessão entre usuários ou requisições; identifique conversas por um identificador opaco quando necessário.
- Envie ao modelo apenas o contexto necessário. Respeite limites de contexto e tamanho, e trunque ou resuma o histórico com uma estratégia previsível sem remover instruções essenciais.
- Construa prompts de forma legível e mantenha instruções de sistema versionáveis e fora de concatenações improvisadas. Considere todo conteúdo do usuário e de fontes recuperadas como dado não confiável, não como instrução de sistema.
- Quando o chatbot usar ferramentas ou executar ações, valide os argumentos, restrinja operações ao escopo autorizado e peça confirmação pelo fluxo do produto antes de ações externas irreversíveis.
- Retorne uma resposta de fallback útil quando não houver resposta confiável, ocorrer uma recusa ou o serviço de modelo estiver indisponível. Não invente que uma ação foi concluída.

## Provedores e falhas

- Isole chamadas específicas do provedor atrás de uma interface pequena quando houver benefício concreto, para manter a lógica conversacional testável e facilitar uma eventual troca.
- Leia chaves e configurações de ambiente por mecanismos já adotados no projeto. Nunca registre chaves, cabeçalhos de autenticação, prompts com dados privados ou conteúdo sensível das conversas.
- Configure timeouts e trate erros de rede, limites de taxa, indisponibilidade e respostas inválidas de forma explícita. Não repita chamadas automaticamente sem limite; use retentativas apenas para falhas transitórias e operações seguras para repetir.
- Valide a estrutura e os limites da resposta do modelo antes de usá-la ou devolvê-la. Não assuma que a saída gerada seja JSON válido, segura ou conforme o formato pedido.
- Se houver streaming, trate desconexões, cancelamento e encerramento do fluxo; não deixe tarefas ou conexões abertas após o cliente sair.
- Registre métricas operacionais necessárias sem coletar conteúdo de conversa por padrão. Se o produto precisar armazenar mensagens, retenha somente o necessário e siga os controles de privacidade e exclusão já definidos.

## Segurança e qualidade da resposta

- Trate respostas do modelo como conteúdo não confiável. Escape ou sanitize conteúdo antes de renderizá-lo em HTML, Markdown executável, SQL, comandos ou outros contextos interpretados.
- Não use o modelo como substituto para validação, autenticação, autorização ou regras de negócio determinísticas. Aplique essas verificações no código da aplicação.
- Evite expor dados de outros usuários no contexto, nas respostas, nos logs ou nos resultados de recuperação. Aplique autorização antes de buscar ou incluir dados privados no prompt.
- Deixe claro no contrato da aplicação quando uma resposta é gerada e pode estar incorreta, conforme a experiência definida pelo produto. Não acrescente alegações ou garantias sem suporte nos dados disponíveis.
- Mantenha limites apropriados para tamanho de entrada, histórico, saída e duração da chamada, para conter consumo inesperado de recursos.
- Quando apropriado à tarefa, verifique fluxos de sucesso, histórico vazio ou longo, entradas inválidas, indisponibilidade do provedor e isolamento entre conversas usando as ferramentas já adotadas pelo projeto.
