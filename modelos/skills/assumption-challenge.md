# Skill: assumption-challenge

| Campo | Valor |
|:---|:---|
| **Versão** | `1.0.0` |
| **Domínio** | `Questionamento de Pressupostos` |
| **Tipo** | `Análise` |
| **Reutilizável** | `Sim` |
| **Atualizado em** | `2026-06-12` |

---

## Propósito

Identificar e questionar pressupostos ocultos em decisões, requisitos e features — forçando clareza sobre o que está sendo assumido como verdadeiro sem evidência explícita.

---

## Quando usar

- Antes de aprovar decisões complexas
- Durante revisão de requisitos para identificar ambiguidades
- Ao planejar features para validar necessidade real
- Para reduzir overengineering e complexidade acidental

---

## Entrada

```markdown
## Decisão / Feature / Requisito

**Descrição:**
[descrição do que está sendo proposto]

**Justificativa Declarada:**
[razões explícitas para esta decisão]

**Contexto:**
[situação atual, problema a resolver]

**Stakeholders:**
[quem está envolvido/impactado]
```

---

## Processo

### 1. Identificar Pressupostos

Para cada afirmação, pergunte:
- [ ] O que está sendo assumido como verdadeiro?
- [ ] Esta suposição é explícita ou implícita?
- [ ] Quem fez esta suposição?

### 2. Classificar Pressupostos

| Tipo | Descrição | Exemplo |
|:---|:---|:---|
| **Fático** | Sobre fatos do mundo | "Usuários têm conexão constante" |
| **Técnico** | Sobre tecnologia | "Precisamos de microserviços" |
| **Negócio** | Sobre necessidades | "Usuários querem feature X" |
| **Temporal** | Sobre timing | "Precisamos disso agora" |

### 3. Validar Cada Pressuposto

Para cada pressuposto:
- [ ] Há evidência direta?
- [ ] É opinião ou dado?
- [ ] Foi testado/validado?
- [ ] Pode ser falsificado?

### 4. Questionar com Técnicas

#### Inversão
"E se o oposto fosse verdadeiro?"

#### Primeiro Princípios
"Qual é o fundamento básico aqui?"

#### Cinco Porquês
"Pergunte 'por quê?' 5 vezes para chegar na raiz"

#### E Se Removêssemos?
"O que acontece se eliminarmos este componente/feature?"

### 5. Propor Alternativas Simples

Para cada pressuposto questionado:
- [ ] Existe versão mais simples?
- [ ] Podemos validar antes de construir?
- [ ] Existe solução manual temporária?

---

## Saída

```markdown
## Challenge de Pressupostos: {{TEMA}}

### Pressupostos Identificados

| ID | Pressuposto | Tipo | Fonte | É Válido? |
|:---|:---|:---:|:---|:---:|
| P01 | [suposição 1] | Fático/Técnico/Negócio | [quem] | ✅/❓/❌ |
| P02 | [suposição 2] | Fático/Técnico/Negócio | [quem] | ✅/❓/❌ |

### Validação por Pressuposto

#### P01: [Nome do Pressuposto]

**É válido?** ✅ Sim / ❓ Precisa validar / ❌ Não

**Evidência:**
- [dados que suportam ou refutam]

**Risco se falso:**
- [o que acontece se esta suposição estiver errada]

**Como validar:**
- [método para testar esta suposição]

#### P02: [Nome do Pressuposto]

[mesma estrutura]

### Perguntas Desestabilizadoras

**Sobre Existência:**
- [pergunta 1]
- [pergunta 2]

**Sobre Complexidade:**
- [pergunta 1]
- [pergunta 2]

**Sobre Timing:**
- [pergunta 1]
- [pergunta 2]

### Simplificações Possíveis

| Componente/Feature | Versão Atual | Versão Simplificada | Trade-off |
|:---|:---|:---|:---|
| [nome] | [complexo] | [simples] | [o que perde] |

### Dados Necessários para Decisão

| Dado | Por que precisamos? | Como obter? | Prioridade |
|:---|:---|:---|:---:|
| [métrica] | [justificativa] | [método] | Alta/Média |

### Recomendações

#### Ação Imediata
1. [ação para validar pressuposto crítico]
2. [ação para simplificar com base em pressuposto questionado]

#### Validação Necessária
1. [teste/experimento para validar suposição]

#### Decisão Pendente
- [decisão que precisa de mais dados antes de prosseguir]

### Frase Síntese

"[frase curta que resume o insight principal]"
```

---

## Critérios de Qualidade

- [ ] Todos os pressupostos identificados estão explícitos
- [ ] Cada pressuposto foi classificado corretamente
- [ ] Validação baseada em evidência, não opinião
- [ ] Riscos de pressupostos falsos avaliados
- [ ] Simplificações propostas são viáveis
- [ ] Plano de validação é executável

---

## Exemplo de Uso

**Entrada:**
```
Decisão: Implementar sistema de recomendação com IA

Justificativa: Aumentar conversão através de personalização

Contexto: E-commerce com 10k usuários, 3 meses de operação

Stakeholders: PM, Tech Lead, CEO
```

**Saída:**
```markdown
## Challenge de Pressupostos: Sistema de Recomendação com IA

### Pressupostos Identificados

| ID | Pressuposto | Tipo | Fonte | Válido? |
|:---|:---|:---:|:---|:---:|
| P01 | Usuários querem recomendações personalizadas | Negócio | PM | ❓ |
| P02 | IA aumenta conversão no nosso caso | Negócio | CEO | ❌ |
| P03 | Temos dados suficientes para treinar | Técnico | Tech Lead | ❌ |

### Validação

#### P01: Usuários querem personalização

**É válido?** ❓ Precisa validar

**Evidência:** Nenhuma pesquisa com usuários feita

**Risco se falso:** Construir feature que ninguém usa

**Como validar:** Survey com 100 usuários, entrevistas qualitativas

#### P02: IA aumenta conversão

**É válido?** ❌ Sem evidência no nosso contexto

**Evidência:** Artigo genérico, não aplicado ao nosso domínio

**Risco se falso:** Investir 3 meses em feature sem ROI

**Como validar:** Teste A/B com regras simples primeiro

### Simplificações Possíveis

| Feature | Versão Atual | Simplificada | Trade-off |
|:---|:---|:---|:---|
| IA customizada | Modelo treinado | Regras "quem viu X viu Y" | Menos personalização |

### Recomendações

**Ação Imediata:**
1. Validar com usuários se personalização é desejada
2. Implementar regras simples e medir impacto antes de IA

**Frase Síntese:**
"IA é solução cara para problema não validado. Comece manual, escale depois."
```

---

## Agentes que usam esta skill

- `conselho-decisao` (orquestrador)
- `leigo-radical`
- `fora-da-caixa`
