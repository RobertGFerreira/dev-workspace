# Skill: decision-critique

| Campo | Valor |
|:---|:---|
| **Versão** | `1.0.0` |
| **Domínio** | `Crítica Estruturada de Decisões` |
| **Tipo** | `Análise` |
| **Reutilizável** | `Sim` |
| **Atualizado em** | `2026-06-12` |

---

## Propósito

Fornecer estrutura para crítica sistemática de decisões técnicas e de produto — analisando validade, riscos, alternativas e consequências antes de consolidar recomendações.

---

## Quando usar

- Revisão de decisões arquiteturais (ADRs)
- Validação de escolhas tecnológicas
- Análise de trade-offs entre alternativas
- Crítica de decisões de produto/feature

---

## Entrada

```markdown
## Decisão a Criticar

**Contexto:**
[descrição do contexto da decisão]

**Decisão Proposta:**
[o que foi decidido ou está sendo proposto]

**Alternativas Consideradas:**
[opções avaliadas, se houver]

**Restrições:**
[limitações conhecidas: tempo, orçamento, equipe, tecnologia]

**Impacto Esperado:**
[resultado esperado da decisão]
```

---

## Processo

### 1. Validar Fundamentação

- [ ] Decisão é baseada em dados ou opiniões?
- [ ] Premissas estão explícitas e validadas?
- [ ] Critérios de decisão são claros e objetivos?

### 2. Analisar Consequências

- **Primeira ordem:** O que acontece imediatamente após implementar?
- **Segunda ordem:** O que acontece como consequência da primeira ordem?
- **Terceira ordem:** Qual o impacto de longo prazo?

### 3. Avaliar Alternativas

- [ ] Todas as alternativas viáveis foram consideradas?
- [ ] Trade-offs entre opções estão claros?
- [ ] Existe opção "não fazer nada" avaliada?

### 4. Identificar Riscos

- [ ] Riscos técnicos identificados?
- [ ] Riscos de negócio considerados?
- [ ] Riscos operacionais mapeados?
- [ ] Plano de mitigação existe?

### 5. Verificar Reversibilidade

- **Tipo 1 (reversível):** Pode desfazer com custo baixo
- **Tipo 2 (irreversível):** Decisão permanente ou custo alto de reverter

Qual é esta decisão? Decisões irreversíveis exigem mais análise.

---

## Saída

```markdown
## Crítica de Decisão: {{TEMA}}

### Fundamentação

**Base:** Dados / Opiniões / Misto
**Premissas válidas:** [lista]
**Premissas questionáveis:** [lista]

### Consequências

#### Primeira Ordem
- [consequência imediata 1]
- [consequência imediata 2]

#### Segunda Ordem
- [consequência de segunda ordem 1]
- [consequência de segunda ordem 2]

#### Longo Prazo
- [impacto de longo prazo]

### Alternativas

| Alternativa | Prós | Contras | Recomendação |
|:---|:---|:---|:---|
| [opção A] | [prós] | [contras] | [avaliação] |

### Riscos Identificados

| Risco | Impacto | Probabilidade | Mitigação |
|:---|:---:|:---:|:---|
| [risco 1] | Alto/Médio/Baixo | Alta/Média/Baixa | [mitigação] |

### Reversibilidade

**Tipo:** 1 (reversível) / 2 (irreversível)

**Custo de reverter:** [baixo/médio/alto]

**Estratégia de rollback:** [como reverter se necessário]

### Recomendação Final

**Status:** ✅ Aprovar | ⚠️ Aprovar com ressalvas | ❌ Reprovar

**Justificativa:**
[explicação detalhada da recomendação]

**Condições para aprovar:**
- [condição 1, se houver ressalvas]
- [condição 2]
```

---

## Critérios de Qualidade

- [ ] Análise baseada em evidências, não opiniões
- [ ] Consequências de múltiplas ordens consideradas
- [ ] Alternativas avaliadas honestamente
- [ ] Riscos priorizados por impacto/probabilidade
- [ ] Reversibilidade classificada corretamente
- [ ] Recomendação clara com justificativa

---

## Exemplo de Uso

**Entrada:**
```
Decisão: Migrar banco de dados PostgreSQL para MongoDB

Contexto: Sistema atual tem problemas com schema flexível para features de personalização

Alternativas consideradas:
1. Manter PostgreSQL + JSONB
2. Migrar para MongoDB
3. Usar PostgreSQL + cache Redis

Restrições: Equipe de 4 devs, prazo 2 meses
```

**Saída:** Crítica estruturada com análise de consequências, riscos, alternativas e recomendação.

---

## Agentes que usam esta skill

- `conselho-decisao` (orquestrador)
- `caminho-correto`
- `cata-falhas`
- `agente-arquitetura`
