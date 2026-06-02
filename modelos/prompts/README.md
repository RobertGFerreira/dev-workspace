# modelos/prompts/

> Biblioteca de instruções reutilizáveis — prompts estruturados por tipo de tarefa para uso com agentes e ferramentas de IA.

---

## Finalidade da Pasta

A pasta `prompts/` é a **biblioteca de instruções operacionais** do workspace. Cada arquivo representa uma instrução estruturada que direciona um agente ou ferramenta de IA para executar uma tarefa com precisão e consistência.

Prompts não são respostas — são **receitas de execução**. Eles definem o quê, como e com qual critério de qualidade uma tarefa deve ser realizada.

> Diferente de um agente (que define identidade e escopo), um prompt define **como uma ação específica deve ser executada**.

---

## Tipos de Prompts

### Prompt Operacional
Instrui a execução direta de uma tarefa técnica — gerar código, criar estrutura, configurar ambiente. São orientados a *fazer*.

**Exemplos:** `bootstrap-governanca.md`, `commit-guardian.md`

### Prompt de Análise
Instrui a avaliação de um artefato existente — código, documentação, arquitetura. Produzem diagnósticos, relatórios e recomendações. São orientados a *avaliar*.

**Exemplos:** `revisor-codigo.md`, `quality-gate.md`, `repo-map-analyst.md`

### Prompt de Geração
Instrui a criação de documentação, especificações, roadmaps ou outros artefatos textuais estruturados. São orientados a *produzir*.

**Exemplos:** `documentacao-requisitos.md`, `spec-agent.md`, `orquestrador-planejamento.md`

---

## O que um Bom Prompt Deve Conter

| Elemento | Descrição |
|---|---|
| **Objetivo claro** | O que deve ser feito — sem ambiguidade |
| **Contexto** | Informações necessárias para execução correta |
| **Critérios de saída** | Como deve ser o resultado — formato, extensão, estrutura |
| **Restrições** | O que não deve ser feito, o que evitar |
| **Exemplos** | Quando útil, um exemplo curto do output esperado |
| **Gatilho de uso** | Quando este prompt deve ser invocado |

---

## Lista de Prompts por Categoria

### 🚀 Operacional — Bootstrap e Configuração
| Arquivo | Descrição |
|---|---|
| `bootstrap-governanca.md` | Inicializa a estrutura de governança de um novo projeto |
| `commit-guardian.md` | Verifica pré-condições antes de executar um commit |

### 🔍 Análise — Revisão e Qualidade
| Arquivo | Descrição |
|---|---|
| `revisor-codigo.md` | Revisão sistemática de código com critérios de qualidade |
| `quality-gate.md` | Gate final de qualidade antes de entrega ou merge |
| `repo-map-analyst.md` | Análise e mapeamento de estrutura de repositório |
| `seguranca-conformidade.md` | Auditoria de segurança e conformidade técnica |
| `guardiao-fluxo.md` | Verificação de desvios arquiteturais e de processo |

### 📋 Geração — Documentação e Especificação
| Arquivo | Descrição |
|---|---|
| `documentacao-requisitos.md` | Levantamento e estruturação de requisitos |
| `spec-agent.md` | Geração de especificações técnicas detalhadas |
| `orquestrador-planejamento.md` | Planejamento de ciclo de desenvolvimento e orquestração de tarefas |

### 🎨 Front-end / UI/UX
| Arquivo | Descrição |
|---|---|
| `design-ui-ux-pro.md` | Design de interfaces com padrões avançados de UX |

### 🗄️ Back-end / Banco de Dados
| Arquivo | Descrição |
|---|---|
| `database-architect.md` | Arquitetura e modelagem de banco de dados |

### 🌾 Domínio Específico
| Arquivo | Descrição |
|---|---|
| `agro-domain-guard.md` | Regras de domínio para projetos do setor agrícola/rural |

### 💡 Exploração e Ideação
| Arquivo | Descrição |
|---|---|
| `ideias-exploracao.md` | Prompt de exploração criativa para ideação de features |

### 🤝 Orquestração
| Arquivo | Descrição |
|---|---|
| `orquestrador-agentes.md` | Instrução de orquestração de fluxo entre agentes |

### 📄 Template Base
| Arquivo | Descrição |
|---|---|
| `PROMPT_UNIVERSAL.template.md` | Template universal para criação de novos prompts |

---

## Como Escolher um Prompt

```
Qual é a tarefa?
    │
    ├─► Configurar ou inicializar algo   → Operacional (bootstrap, commit-guardian)
    │
    ├─► Avaliar ou auditar algo          → Análise (revisor-codigo, quality-gate, seguranca)
    │
    ├─► Criar documentação ou spec       → Geração (documentacao-requisitos, spec-agent)
    │
    ├─► Trabalhar com interface visual   → UI/UX (design-ui-ux-pro)
    │
    ├─► Trabalhar com banco de dados     → Back-end (database-architect)
    │
    ├─► Domínio agrícola/rural           → Domínio (agro-domain-guard)
    │
    └─► Explorar ideias ou possibilidades → Ideação (ideias-exploracao)
```

---

## Boas Práticas de Uso

1. **Leia o prompt completo antes de usar** — entenda o contexto e os critérios de saída esperados.
2. **Adapte o contexto** — substitua referências genéricas pelas especificidades da tarefa atual.
3. **Não misture prompts** — cada prompt tem um propósito único; evite combinar dois prompts em uma única instrução.
4. **Forneça o input correto** — muitos prompts esperam um artefato de entrada (código, spec, repositório). Garanta que ele esteja disponível.
5. **Valide o output** — o resultado de um prompt de análise deve ser revisado por um humano antes de ser considerado definitivo.
6. **Documente o uso** — se um prompt foi invocado em um ciclo de desenvolvimento, registre no changelog ou relatório do projeto.

---

## Critérios de Evolução

Um prompt deve ser atualizado quando:
- O padrão de qualidade que ele exige evoluiu no projeto de origem.
- O formato de saída precisar ser alterado para compatibilidade com novas ferramentas.
- O domínio coberto se ampliou e o prompt original ficou incompleto.

Novos prompts entram em `prompts/` quando:
- São testados e validados em pelo menos um projeto real.
- Cobrem um caso de uso que ainda não está representado na biblioteca.
- São genéricos o suficiente para ser reutilizados em mais de um projeto.

> Para criar um novo prompt, use `PROMPT_UNIVERSAL.template.md` como ponto de partida.

---

## Relação com Agentes e Skills

```
Prompt
  │
  ├─► é invocado por → Agentes (para executar tarefas específicas)
  └─► complementa   → Skills (habilidades técnicas que fornecem o contexto de execução)
```

Um prompt define **o quê fazer** e **como fazer**. O agente define **quem executa**. A skill fornece **o conhecimento especializado** necessário para a execução correta.

> Consulte [`agentes/README.md`](../agentes/README.md) e [`skills/README.md`](../skills/README.md) para entender como esses artefatos se complementam.
