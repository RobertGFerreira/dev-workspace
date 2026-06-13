# Anti-Exemplos — Quando NÃO Usar o Conselho de Decisão

## Objetivo

Documentar situações onde o Conselho de Decisão é desnecessário, contraproducente ou excessivo, para evitar custo desnecessário de contexto em LLMs.

---

## Situações para EVITAR o conselho

### 1. Decisões triviais

**Exemplo:** Escolher entre padding de 8px vs 12px em um botão.

**Por que não usar:** O custo de acionar 5 agentes supera o benefício da decisão. Decisões de baixo impacto devem ser tomadas diretamente pelo executor.

### 2. Correções de bug simples

**Exemplo:** Corrigir null pointer exception em uma função bem compreendida.

**Por que não usar:** Bug com causa raiz conhecida e solução direta não requer crítica multi-perspectiva. O `revisor-codigo` é suficiente.

### 3. Projetos sem SDD formal

**Exemplo:** Projeto experimental ou protótipo descartável.

**Por que não usar:** Se não há SDD para revisar, o conselho perde seu principal caso de uso. O custo de contexto não se justifica.

### 4. Features já especificadas por autoridade competente

**Exemplo:** Feature especificada por `spec-agent` e aprovada por `quality-gate`.

**Por que não usar:** Se a especificação já passou por validação adequada, o conselho seria redundante.

### 5. Decisões puramente operacionais

**Exemplo:** Definir nome de branch, escolher ferramenta de formatação de código.

**Por que não usar:** Decisões que não afetam arquitetura, requisitos ou experiência do usuário não precisam de crítica estruturada.

### 6. Quando o prazo é crítico e o risco é baixo

**Exemplo:** Hotfix de produção com impacto bem compreendido.

**Por que não usar:** A urgência da correção supera o benefício da crítica. Documente a decisão e revise depois se necessário.

### 7. Quando o custo de contexto excede o benefício

**Exemplo:** Projeto muito pequeno (1-2 agentes, sem SDD, sem testes formais).

**Por que não usar:** O conselho adiciona 5 agentes ao contexto. Em projetos pequenos, o overhead reduz a eficiência sem ganho proporcional.

---

## Regra Geral

Acione o conselho quando:

- A decisão tem impacto arquitetural ou de produto significativo
- Há múltiplas alternativas viáveis com trade-offs reais
- O risco de erro é médio/alto
- Há SDD formal para revisar

Não acione o conselho quando:

- A decisão é trivial ou reversível
- O risco é baixo e o impacto é localizado
- O custo de contexto supera o benefício esperado
- Já houve validação por autoridade competente
