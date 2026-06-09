# modelos/skills/

> Biblioteca de capacidades técnicas modulares — habilidades especializadas que ampliam o escopo de atuação de agentes de IA.

---

## Finalidade da Pasta

A pasta `skills/` reúne as **capacidades técnicas reutilizáveis** do workspace. Cada skill é um conjunto estruturado de critérios, verificações e conhecimentos técnicos que pode ser invocado por um agente para executar tarefas especializadas com maior precisão.

Skills funcionam como **módulos de conhecimento** — elas não executam por conta própria, mas ampliam o que um agente consegue fazer quando as invoca.

> Se um agente é o chef, a skill é a técnica culinária que ele domina. Sem ela, o prato pode ser feito — mas com ela, é feito corretamente.

---

## O que é uma Skill

Uma skill é um arquivo que define:

| Elemento | Descrição |
|---|---|
| **Domínio** | A área técnica coberta (Flutter, banco de dados, segurança, etc.) |
| **Critérios** | O que deve ser verificado ou executado dentro desse domínio |
| **Padrões** | Os padrões de qualidade esperados como resultado |
| **Restrições** | O que nunca deve acontecer no contexto deste domínio |
| **Gatilho** | Quando esta skill deve ser invocada por um agente |

---

## Quando Usar uma Skill

Uma skill deve ser usada quando uma tarefa exige **conhecimento técnico aprofundado** que vai além da instrução geral de um prompt. Exemplos:

- Revisar uma migração de banco de dados SQLite → `sqlite-integrity-review.md`
- Auditar a segurança de um app mobile → `security-mobile-review.md`
- Verificar padrões de UI em Flutter → `flutter-ui-standards.md`
- Avaliar performance de widgets → `flutter-performance-guard.md`

---

## Tipos de Skills

### UI/UX
Capacidades de avaliação e criação de interfaces visuais com base em princípios de design e padrões de qualidade.

### Banco de Dados
Capacidades de verificação de integridade, modelagem e boas práticas em bancos de dados relacionais e locais.

### Sincronização Offline
Capacidades de auditoria de fluxos offline-first — conflitos, merge, integridade de dados em sincronização.

### Segurança
Capacidades de revisão de práticas de segurança em aplicações mobile — autenticação, armazenamento, exposição de dados.

### Revisão de Código
Capacidades gerais e específicas de revisão — linting, padrões de nomenclatura, cobertura, complexidade.

### Qualidade
Capacidades de validação de formulários, fluxos de navegação e conformidade com padrões definidos.

### Integração
Capacidades de verificação de integrações com APIs, serviços externos e fluxos de dados.

### Performance
Capacidades de monitoramento, auditoria e otimização de desempenho, consumo de recursos e latência.

### Documentação
Capacidades de revisão de consistência e completude de documentação técnica e de projeto.

### Domínio Específico
Conhecimento especializado de um domínio de negócio — regras, terminologia, restrições e contexto do mundo real.

---

## Lista de Skills por Categoria

### 🎨 UI/UX
| Arquivo | Descrição |
|---|---|
| `anti-ai-generic-ui.md` | Previne geração de interfaces genéricas — força identidade visual e intenção de design |
| `flutter-ui-standards.md` | Padrões de implementação de UI em Flutter |
| `ui-ux-pro-review.md` | Revisão avançada de UX com critérios de qualidade visual e interação |

### 🗄️ Banco de Dados
| Arquivo | Descrição |
|---|---|
| `sqlite-integrity-review.md` | Revisão de integridade de banco SQLite — constraints, índices, migrações |
| `flutter-sqlite-review.md` | Revisão de uso de SQLite em projetos Flutter |

### 🔄 Sincronização Offline
| Arquivo | Descrição |
|---|---|
| `offline-sync-review.md` | Auditoria de fluxos offline-first — conflitos, merge e integridade |

### 🔐 Segurança
| Arquivo | Descrição |
|---|---|
| `security-mobile-review.md` | Revisão de segurança em aplicações mobile — autenticação, dados sensíveis, permissões |

### 🔍 Revisão de Código

| Arquivo | Camada | Descrição |
|---|:---:|---|
| `code-review-universal.md` | **Universal** | Revisão de qualidade — sem especificidade de linguagem ou framework |
| `flutter-code-review.md` | Flutter | Revisão geral de código Flutter — boas práticas, padrões, organização |
| `flutter-analyze-lint.md` | Flutter | Análise de lint e conformidade com regras do `flutter analyze` |
| `flutter-state-review.md` | Flutter | Revisão de gerenciamento de estado — consistência, reatividade, vazamentos |

### ✅ Qualidade e Navegação
| Arquivo | Descrição |
|---|---|
| `forms-validation-review.md` | Revisão de validação de formulários — campos obrigatórios, feedback, UX |
| `flutter-navigation-review.md` | Revisão de fluxos de navegação — rotas, deeplinks, estado de navegação |
| `navigation-flow-review.md` | Auditoria de fluxo completo de navegação entre telas |
| `scope-control.md` | Controle de escopo, autoridade e fronteiras entre agentes |

### 🔗 Integração
| Arquivo | Descrição |
|---|---|
| `flutter-api-integration.md` | Revisão de integrações com APIs REST — erros, timeouts, cache |
| `flutter-photos-files.md` | Revisão de acesso a fotos e sistema de arquivos em Flutter |

### ⚡ Performance
| Arquivo | Camada | Descrição |
|---|:---:|---|
| `performance-universal.md` | **Universal** | Auditoria e otimização de performance geral, uso de recursos, concorrência e banco de dados |
| `flutter-performance-guard.md` | Flutter | Monitoramento de performance — renderização, janks, memory leaks |

### 📄 Documentação
| Arquivo | Descrição |
|---|---|
| `agent-instructions-review.md` | Auditoria de clareza, concisão e comandos de guias de agentes (AGENTS.md) |
| `documentation-consistency-review.md` | Revisão de consistência entre código e documentação técnica |
| `documentation-consistency.md` | Validação de consistência cruzada entre arquivos do repositório |
| `template-adherence.md` | Validação de correspondência com as diretrizes do template original |
| `structure-review.md` | Validação estrutural de documentos, H1-H6 e índices markdown |
| `markdown-quality.md` | Lint geral de Markdown (links, formatação, espaçamento) |
| `placeholder-governance.md` | Rastreamento e bloqueio de placeholders não preenchidos |

### 🎮 Desenvolvimento de Jogos (Games)
| Arquivo | Descrição |
|---|---|
| `game-structure-planning.md` | Planejamento de fluxos, cenas, fases e estruturas gerais de jogos |
| `game-narrative-design.md` | Estruturação de enredos, lore de mundo, diálogos ramificados |
| `game-loop-design.md` | Modelagem do loop de jogabilidade central (core loop) e ciclos de retenção |
| `game-mechanics-balance.md` | Balanceamento de mecânicas de jogo, regras e curvas de progressão |
| `game-ux-ui.md` | Princípios de UI/UX aplicados a games, layouts de HUD e feedback |
| `game-monetization-strategy.md` | Economia in-game, passes, anúncios e compras integradas |
| `game-release-readiness.md` | Validação de builds de jogos, assets e readiness para publicação |

### Conteúdo Editorial
| Arquivo | Descrição |
|---|---|
| `content-orchestration.md` | Orquestração entre roteiro, documentação, estratégia, revisão e publicação |
| `editorial-structure.md` | Estruturação editorial de peças, documentos, roteiros e publicações |
| `narrative-structure.md` | Estrutura narrativa para roteiros, vídeos, aulas e storytelling |
| `audience-targeting.md` | Definição de público, canal, tom e intenção de comunicação |
| `publication-readiness.md` | Prontidão editorial para publicação em canais digitais ou docs versionadas |
| `quality-review.md` | Revisão final de qualidade, clareza, consistência e aderência ao objetivo |

### 📢 Marketing de Sistemas
| Arquivo | Descrição |
|---|---|
| `product-positioning.md` | Posicionamento competitivo de software, SaaS e apps em mercados alvo |
| `audience-segmentation.md` | Segmentação de público-alvo, criação de personas e perfis de clientes |
| `value-proposition-writing.md` | Redação de propostas de valor claras e impactantes para software |
| `launch-campaign-planning.md` | Planejamento de campanhas de lançamento digital e aquisição |
| `conversion-copy-review.md` | Revisão de copy para otimização de conversão (CRO) e CTAs |
| `feature-storytelling.md` | Conversão de características técnicas em histórias e benefícios do usuário |

### 📦 Distribuição e Lojas
| Arquivo | Descrição |
|---|---|
| `play-console-checklist.md` | Checklist estruturado de etapas e formulários para o Google Play Console |
| `store-listing-optimization.md` | Otimização de metadados para busca (ASO) na listagem da loja |
| `android-policy-review.md` | Auditoria de conformidade com as políticas de desenvolvedor do Google Play |
| `asset-compliance.md` | Auditoria de formatos e resoluções de imagens exigidas pelas lojas |
| `release-readiness.md` | Validação final de chaves, assinaturas, tamanho e bundle (AAB) |
| `privacy-disclosure-review.md` | Auditoria de políticas de privacidade e declaração de coleta de dados |

### 📄 Template Base
| Arquivo | Descrição |
|---|---|
| `SKILL_UNIVERSAL.template.md` | Template universal para criação de novas skills |

---

## Como Usar uma Skill

1. **Identifique a necessidade** — qual capacidade técnica a tarefa exige?
2. **Localize a skill correspondente** na lista acima.
3. **Vincule ao agente** — na seção `## Skills Ativas` do arquivo de agente, adicione a referência.
4. **Forneça o contexto de entrada** — a skill precisa do artefato que será avaliado (código, spec, banco de dados).
5. **Interprete o resultado** — a skill produz critérios e verificações; o agente é responsável por consolidar e reportar.

### Exemplo de vínculo em um agente
```markdown
## Skills Ativas
- skill: flutter-code-review.md
- skill: sqlite-integrity-review.md
- skill: security-mobile-review.md
```

---

## Critérios de Curadoria

Uma skill entra em `skills/` quando:

| Critério | Descrição |
|---|---|
| **Especialização** | Cobre um domínio técnico que exige conhecimento específico |
| **Modularidade** | Pode ser invocada de forma independente por qualquer agente |
| **Generalidade** | Aplicável a mais de um projeto, sem hardcode de dados específicos |
| **Testada** | Já foi usada em pelo menos um projeto real com resultado satisfatório |
| **Sem dados sensíveis** | Nenhuma referência a senhas, tokens, caminhos absolutos ou dados de produção |

Skills muito específicas de um único contexto de negócio do projeto destino são permitidas para uso local, mas devem ser criadas na pasta `governance/skills/` do próprio projeto — não na biblioteca de modelos universais.

---

## Relação com Agentes e Prompts

```
Skill
  │
  ├─► é invocada por → Agentes (que definem quando e como a skill é usada)
  └─► complementa   → Prompts (que definem a tarefa; a skill fornece o conhecimento técnico)
```

A hierarquia é:
- **Agente** → define identidade e orquestra o uso de skills e prompts.
- **Prompt** → define a instrução da tarefa a ser executada.
- **Skill** → fornece o conhecimento técnico especializado para execução correta.

> Consulte [`agentes/README.md`](../agentes/README.md) e [`prompts/README.md`](../prompts/README.md) para entender como os três artefatos se integram.
