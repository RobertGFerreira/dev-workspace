# Guia de Uso do Conselho de Decisão

## Visão Geral

O **Conselho de Decisão** é um módulo especializado em análise crítica sistemática de decisões, SDDs, features e requisitos. Ele coordena 4 conselheiros com perspectivas diferentes para fornecer pareceres consolidados antes de decisões importantes.

---

## Quando Acionar o Conselho

### ✅ Gatilhos Recomendados (QUANDO USAR)

| Situação | Por que acionar | Conselheiros Prioritários |
|:---|:---|:---|
| **Decisões arquiteturais significativas** | Impacto de longo prazo, difícil reverter | Todos os 4 |
| **SDD de features críticas** | Alto impacto no negócio/usuários | caminho-correto + cata-falhas |
| **Requisitos ambíguos ou conflitantes** | Precisa de clareza antes de implementar | leigo-radical + fora-da-caixa |
| **Mudanças com alto impacto/risco** | Consequências significativas se falhar | cata-falhas + caminho-correto |
| **Features com múltiplas alternativas viáveis** | Precisa expandir espaço de soluções | fora-da-caixa + leigo-radical |
| **Situações com histórico de falhas similares** | Aprender com erros passados | cata-falhas |
| **Derivação de critérios de aceite/testes** | Garantir cobertura completa | caminho-correto + cata-falhas |
| **Expansão de ideias de features** | Brainstorm estruturado | fora-da-caixa |
| **Overengineering suspeito** | Complexidade pode ser desnecessária | leigo-radical |
| **Validação de conformidade** | Verificar aderência a padrões | caminho-correto |

### ❌ Quando NÃO Acionar

| Situação | Por que evitar | Alternativa |
|:---|:---|:---|
| **Decisões triviais ou de baixo impacto** | Custo de contexto > benefício | Decida diretamente ou com agente responsável |
| **Urgência extrema (time crítico)** | Conselho leva 1-2 iterações | Agente responsável decide, documenta depois |
| **Decisões já validadas recentemente** | Redundância desnecessária | Reutilize parecer existente |
| **Preferências pessoais/cosméticas** | Não é decisão estrutural | Discuta com equipe diretamente |
| **Quando você já tem dados conclusivos** | Análise não vai mudar nada | Implemente baseado nos dados |
| **Orçamento de contexto esgotado** | Limite de 3 consultas por feature | Priorize outras consultas |

---

## Como Acionar

### Via Tag (Recomendado)

```
/conselho
Tipo de Demanda: [decisão | sdd | testes | feature]

Contexto:
[descrição do contexto]

Decisão / Feature / SDD:
[descrição detalhada]

Alternativas Consideradas:
[opções, se houver]

Restrições:
[limitações conhecidas]

Impacto Esperado:
[resultado esperado]
```

### Tags Específicas

| Tag | Uso | Exemplo |
|:---|:---|:---|
| `/conselho` | Revisão completa | `/conselho Tipo: decisão...` |
| `/sdd-review` | Revisão de SDD | `/sdd-review [link para SDD]` |
| `/test-derivation` | Derivar testes | `/test-derivation [feature]` |
| `/decision-critique` | Criticar decisão | `/decision-critique [decisão]` |

---

## Estrutura do Conselho

### Orquestrador

**Agente:** `conselho-decisao`

**Papel:** Coordena os 4 conselheiros, seleciona quais são relevantes para cada demanda, consolida pareceres e gera recomendação final.

### Conselheiros

| Conselheiro | Arquivo | Papel | Quando é Prioritário |
|:---|:---|:---|:---|
| **caminho-correto** | `caminho-correto.md` | Valida padrões, convenções, melhores práticas | Decisões que precisam de conformidade |
| **cata-falhas** | `cata-falhas.md` | Busca falhas, riscos, pontos cegos | Decisões de alto risco |
| **fora-da-caixa** | `fora-da-caixa.md` | Propõe alternativas criativas | Brainstorm, múltiplas opções |
| **leigo-radical** | `leigo-radical.md` | Questiona pressupostos, simplifica | Suspeita de overengineering |

---

## Fluxo Operacional

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Usuário aciona com /conselho + contexto                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Orquestrador analisa tipo de demanda                     │
│    - Decisão arquitetural? → todos os 4                     │
│    - Revisão de código? → caminho-correto + cata-falhas     │
│    - Brainstorm? → fora-da-caixa + leigo-radical            │
│    - Validação? → caminho-correto                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Conselheiros selecionados geram pareceres em paralelo    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Orquestrador consolida pareceres                         │
│    - Identifica convergências                                │
│    - Highlight divergências                                  │
│    - Gera recomendação final                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Saída:                                                   │
│    - Parecer por conselheiro                                 │
│    - Recomendação (aprovar/aprovar com ressalvas/reprovar)   │
│    - Critérios de aceite derivados (quando aplicável)        │
│    - Testes derivados (positivos/negativos/borda/proibidos)  │
│    - Handoff recomendado (para qual agente encaminhar)       │
└─────────────────────────────────────────────────────────────┘
```

---

## Orçamento de Contexto

### Limites Recomendados

| Métrica | Limite | Justificativa |
|:---|:---:|:---|
| **Consultas por feature complexa** | 3 | Evitar excesso de tokens e paralisia |
| **Iterações por consulta** | 2 | SLA informal para não travar fluxo |
| **Conselheiros por consulta** | 2-4 | Selecionar baseado no tipo de demanda |

### Como Otimizar

1. **Seja específico na entrada:** Quanto mais contexto claro, menos iterações necessárias.

2. **Acione apenas conselheiros relevantes:** Não use todos os 4 se apenas 1-2 são necessários.

3. **Agrupe demandas relacionadas:** Em vez de 3 consultas pequenas, faça 1 consulta abrangente.

4. **Reutilize pareceres:** Se conselho já analisou tema similar, adapte em vez de reconsultar.

---

## Interpretação da Saída

### Recomendações do Conselho

| Status | Significado | Ação Recomendada |
|:---|:---|:---|
| **✅ Aprovar** | Conselho vê valor, riscos mitigados | Prossiga com implementação |
| **⚠️ Aprovar com ressalvas** | Aprovado, mas há condições | Atenda condições antes de implementar |
| **❌ Reprovar com justificativa** | Riscos/benefícios desbalanceados | Reavalie decisão, considere alternativas |

### Critérios de Aceite Derivados

Use como checklist para validar implementação:

```markdown
### Critérios de Aceite Derivados
- [ ] [critério 1] ← Deve ser atendido para considerar feature completa
- [ ] [critério 2]
```

### Testes Derivados

Use como input para `agente-testes` implementar:

```markdown
### Testes Derivados

#### Positivos
- [cenário 1] ← Happy path que deve funcionar

#### Negativos
- [cenário 1] ← Falha esperada que deve ser tratada

#### Edge Cases
- [cenário 1] ← Valor limite que deve ser testado

#### Comportamentos Proibidos
- [o que nunca deve acontecer] ← Deve ser bloqueado/prevenido
```

---

## Fronteiras com Outros Agentes

### Matriz de Responsabilidades

| Atividade | Conselho | Spec-Agent | Agente-Testes | Agente-Arquitetura |
|:---|:---|:---|:---|:---|
| Criar SDD | C | R | I | C |
| Derivar critérios de aceite | R | C | I | I |
| Implementar testes | I | I | R | I |
| Criticar decisão arquitetural | R | I | I | C |
| Propor alternativas | R | I | I | C |
| Validar padrões | R | C | I | I |
| Identificar riscos | R | I | I | C |

**Legenda:** R=Executa, A=Aprova, C=Consulta, I=Informado

### Handoffs Típicos

| De | Para | O que entregar |
|:---|:---|:---|
| Conselho → Spec-Agent | Critérios de aceite derivados | Lista de critérios para incorporar na spec |
| Conselho → Agente-Testes | Cenários de teste derivados | Testes positivos/negativos/borda/proibidos |
| Conselho → Agente-Arquitetura | Parecer sobre decisão | Análise de riscos, alternativas, recomendação |

---

## Exemplos de Uso

### Exemplo 1 — Decisão Arquitetural

**Entrada:**
```
/conselho
Tipo de Demanda: decisão arquitetural

Contexto: App mobile precisa funcionar offline-first

Decisão: Usar SQLite local + sincronização manual quando online

Alternativas Consideradas:
1. SQLite + sync manual (decisão atual)
2. Realm Database + MongoDB Realm Sync (sync automático)
3. WatermelonDB (React Native only)

Restrições:
- Equipe de 3 devs Flutter
- Prazo 3 meses
- Usuários frequentemente em áreas sem conexão

Impacto Esperado: UX consistente mesmo offline
```

**Saída Esperada:** Parecer dos 4 conselheiros + recomendação consolidada

---

### Exemplo 2 — Derivação de Testes

**Entrada:**
```
/test-derivation
Feature: Upload de fotos de perfil

Descrição: Usuários podem fazer upload de foto JPG/PNG até 5MB

Comportamento Esperado: Foto salva, redimensionada e exibida no perfil

Restrições: Máximo 5MB, apenas JPG/PNG, redimensionar para 800x800
```

**Saída Esperada:** Critérios de aceite + testes positivos/negativos/borda/proibidos

---

### Exemplo 3 — Revisão de SDD

**Entrada:**
```
/sdd-review
SDD: Sistema de Pagamentos com Pix

[link para SDD ou conteúdo]

Contexto: E-commerce integrando pagamentos via Pix

Pontos de Atenção:
- Timeout de confirmação do Pix
- Reembolso automático
- Conciliação bancária
```

**Saída Esperada:** Validação de padrões + riscos identificados + critérios de aceite derivados

---

## Anti-Exemplos

### ❌ Mau Uso: Consulta Trivial

**Entrada:**
```
/conselho
Devo usar camelCase ou snake_case para variáveis?
```

**Por que é mau uso:** Decisão trivial, já existe convenção na maioria das linguagens.

**Alternativa:** Consulte guia de estilo da linguagem ou convenção do projeto.

---

### ❌ Mau Uso: Sem Contexto

**Entrada:**
```
/conselho
Isso está certo?
```

**Por que é mau uso:** Sem contexto, sem decisão clara, sem restrições.

**Alternativa:** Forneça contexto completo conforme template.

---

### ❌ Mau Uso: Urgência Extrema

**Entrada:**
```
/conselho
Produção caiu! Qual solução usamos?
```

**Por que é mau uso:** Situação crítica exige ação imediata, não análise de conselho.

**Alternativa:** Agente responsável decide, documenta depois, conselho revisa post-mortem.

---

## FAQ

### P: O conselho tem poder de veto?

**R:** Não. O conselho apenas **recomenda** com justificativa. Decisão final é humana ou do agente responsável.

---

### P: Quantas vezes posso acionar o conselho por feature?

**R:** Recomenda-se máximo de **3 consultas** por feature complexa para evitar excesso de tokens e paralisia.

---

### P: Posso acionar apenas 1 conselheiro?

**R:** Sim. O orquestrador seleciona conselheiros baseado no tipo de demanda. Você pode sugerir quais quer acionar.

---

### P: Quanto tempo leva uma consulta?

**R:** SLA informal é de **até 2 iterações**. Se passar disso, há risco de paralisia por análise.

---

### P: O conselho implementa algo?

**R:** Não. O conselho **analisa e recomenda**. Implementação fica com agentes responsáveis (agente-testes, agente-arquitetura, etc.).

---

### P: Quando o conselho é obrigatório?

**R:** Depende da política do projeto. Recomenda-se tornar obrigatório para:
- Decisões arquiteturais significativas
- Features críticas de negócio
- Mudanças com alto risco

---

## Métricas de Sucesso

### Como Saber se o Conselho Está Funcionando

| Métrica | Ideal | Alerta |
|:---|:---:|:---:|
| **Recomendações seguidas** | >70% | <50% (conselho ignorado) |
| **Falhas em produção após aprovação** | <10% | >30% (conselho não identificou riscos) |
| **Iterações por consulta** | 1-2 | >3 (paralisia) |
| **Satisfação do usuário** | >4/5 | <3/5 |

---

## Contribuição

Para sugerir melhorias neste guia ou nos agentes do conselho:

1. Abra issue descrevendo a melhoria
2. Justifique com exemplos de uso real
3. Submeta PR com mudanças nos arquivos relevantes

---

**Versão deste guia:** 1.0.0  
**Última atualização:** 2026-06-12  
**Manutenção:** `conselho-decisao` (orquestrador)
