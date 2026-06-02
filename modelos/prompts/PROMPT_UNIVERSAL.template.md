# Prompt: [TÍTULO_DO_PROMPT]

**Categoria:** Planejamento | Revisão | Arquitetura | Documentação | Refatoração | Auditoria
**Versão:** [X.Y.Z]

---

## 1. Objetivo do Prompt
### Descrição
> *Esta seção define a missão imediata e o que o prompt visa realizar quando executado por um assistente de IA.*

- **O que deve ser escrito:** Uma declaração de impacto descrevendo o que a IA deve gerar (ex: *Gerar um plano de ação atômico para refatoração de código com zero downtime...*).
- **Como preencher:** Use verbos de ação claros e defina os limites da tarefa (ex: *Analisar o código X fornecido e gerar uma lista de...*).
- **O que evitar:** Evite objetivos vagos do tipo *"Me ajude a programar melhor"*. Prefira *"Validar se a implementação Dart atende aos princípios SOLID..."*.

---

## 2. Contexto de Entrada
### Descrição
> *Mapeamento do cenário, base de código, restrições tecnológicas ou documentação de entrada.*

- **Use esta seção para:** Alimentar a IA com dados ambientais sobre a stack, dependências críticas, regras locais inegociáveis do repositório ou o contexto de negócio.
- **O que preencher:**
  - Qual o cenário operacional em que a tarefa se insere?
  - Quais arquivos, trechos de código ou documentações técnicas serão disponibilizados como insumo de entrada?

---

## 3. Entradas Esperadas
### Descrição
> *Mapeamento das variáveis e dados que o usuário deve fornecer ao acionar este prompt.*

- **O que deve ser escrito:** Uma lista dos elementos que o usuário ou o agente integrador precisa injetar na chamada do prompt (ex: *Código do Widget, Arquivo pubspec.yaml, JSON de logs de erro*).
- **Como preencher:** Classifique as entradas em **[OBRIGATÓRIO]** e **[OPCIONAL]**.

---

## 4. Regras de Execução (Lógica Operacional)
### Descrição
> *Passo a passo lógico e encadeamento de raciocínio (Chain-of-Thought) que a IA deve seguir.*

- **Como preencher:**
  - **Fase 1: Classificação e Triagem:** [Instrução de pensamento inicial. Exemplo: *Classificar a complexidade da alteração antes de qualquer sugestão...*]
  - **Fase 2: Análise e Diagnóstico:** [Instrução de auditoria técnica. Exemplo: *Investigar vazamentos de controller e null safety...*]
  - **Fase 3: Elaboração da Solução:** [Instrução de escrita de código/texto. Exemplo: *Gerar código corrigido focado e refatorado...*]

---

## 5. Restrições e Limitações (O que NÃO fazer)
### Descrição
> *Fronteiras e barreiras inegociáveis de conformidade técnica para prevenir alucinações.*

- **Como preencher:** Destaque o que a IA está terminantemente proibida de fazer.
- **Exemplos de Restrições:**
  - *Nunca sugerir a instalação de dependências externas não aprovadas.*
  - *Nunca alterar layouts visuais, cores ou temas originais sem especificação aprovada.*
  - *Nunca compactar ou resumir códigos de correção — fornecer sempre drop-in replacements completos.*

---

## 6. Critérios de Saída (Definição de Concluído)
### Descrição
> *Checklist de validação que a IA deve aplicar à sua própria resposta antes de entregá-la.*

- **O que deve ser escrito:** Condições que definem que a tarefa foi cumprida com excelência técnica (Definition of Done).
- **Exemplos de Critérios:**
  - [ ] A resposta contém o código completo corrigido sem placeholders do tipo `// resto do código...`.
  - [ ] O plano de tarefas possui a causa raiz de cada bug explicada.
  - [ ] Warnings do analyze de estática de código foram mitigados na sugestão.

---

## 7. Formato do Resultado
### Descrição
> *Definição rigorosa da estrutura markdown do output final.*

- **Use esta seção para:** Fornecer um template markdown em branco que a IA deve usar para estruturar a resposta.
- **Exemplo de Estrutura:**
  ```markdown
  ### 📋 Diagnóstico de IA — [Nome da Tarefa]
  
  #### 1. Análise Técnica
  - **Status:** [Aprovado | Rejeitado com Bloqueio]
  - **Causa Raiz:** [texto]
  
  #### 2. Código Proposto
  \```[linguagem]
  // código corrigido
  \```
  ```

---

## 8. Exemplo de Uso Prático
### Descrição
> *Demonstração de uma interação simulada (Few-shot learning) para guiar o comportamento da IA.*

- **Use esta seção para:** Apresentar uma entrada simulada simples e a respectiva saída exemplar esperada para calibrar o tom, nível de detalhamento e estilo de resposta da IA.
