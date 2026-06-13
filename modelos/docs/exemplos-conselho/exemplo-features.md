# Exemplo — Expansão de Features com o Conselho

## Cenário

Ideia inicial: "Adicionar modo escuro (dark mode) ao aplicativo"

## Contribuições dos Conselheiros

### fora-da-caixa

**Alternativas:**
1. Modo escuro manual (alternância por usuário)
2. Modo escuro automático (segue tema do sistema)
3. Modo escuro agendado (programável pelo usuário)

**Expansões:**
- Temas customizados (cores, fonte, densidade)
- Modo sépia para leitura prolongada
- Redução de ponto branco para dispositivos OLED

### leigo-radical

**Questionamentos:**
- "Por que não começar apenas com tema do sistema?"
- "Modo escuro resolve um problema real ou é tendência?"
- "O esforço de manter 2 temas vale para o público atual?"

**Simplificação:**
MVP: apenas tema do sistema, sem alternância manual. Reduz 60% do esforço.

### caminho-correto

**Validação:**
- Tema escuro deve respeitar contraste mínimo (WCAG AA)
- Cores customizadas não podem quebrar acessibilidade
- Consistência com design system existente

### Consolidação

**Feature resultante:**
- MVP: Modo escuro automático (tema do sistema)
- V2: Alternância manual + 2 temas adicionais
- V3: Temas customizados pelo usuário

**Risco identificado:** Manter 2 temas completos dobra esforço de QA visual
