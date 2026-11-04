# Princípios gerais de engenharia de software

Estas orientações valem para todo o projeto. Siga primeiro os requisitos da tarefa e as convenções existentes no repositório; use estes princípios para orientar decisões quando não houver uma regra mais específica.

## Princípios

- Prefira soluções simples, explícitas e fáceis de manter. Acrescente abstrações quando resolverem uma necessidade concreta.
- Use nomes claros, responsabilidades coesas e fluxo de controle direto.
- Preserve comportamento e interfaces existentes, salvo quando a tarefa pedir uma mudança. Evite alterações alheias ao escopo.
- Reduza duplicação quando houver uma única fonte de verdade clara. Não force a unificação de comportamentos com motivos distintos para mudar.
- Separe responsabilidades quando isso melhorar a compreensão ou permitir mudanças localizadas. Evite camadas sem benefício prático.
- Valide dados nos limites do sistema, preserve informação útil sobre falhas e evite ocultar problemas.
- Considere segurança, privacidade, acessibilidade e desempenho de acordo com o contexto e o impacto real.
- Prefira dependências já adotadas no projeto. Antes de introduzir uma nova, avalie se a biblioteca padrão ou o código existente atende ao caso.

## Como trabalhar com o código

- Antes de editar, examine os arquivos relacionados, o fluxo que os utiliza, as convenções do projeto e o estado atual das mudanças.
- Identifique o comportamento esperado e os limites da tarefa. Faça a menor alteração completa que resolva o pedido.
- Reutilize padrões existentes quando forem adequados. Não replique um padrão que esteja causando o problema em questão.
- Ao alterar uma interface, considere os chamadores e efeitos sobre compatibilidade. Atualize documentação e exemplos afetados.
- Revise a mudança como um todo: procure inconsistências, código morto, casos-limite e efeitos colaterais fora do escopo.
- Verifique o resultado com os meios apropriados ao projeto e à tarefa. Informe claramente o que foi verificado e o que não foi.
