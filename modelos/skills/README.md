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
| Arquivo | Descrição |
|---|---|
| `flutter-code-review.md` | Revisão geral de código Flutter — boas práticas, padrões, organização |
| `flutter-analyze-lint.md` | Análise de lint e conformidade com regras do `flutter analyze` |
| `flutter-state-review.md` | Revisão de gerenciamento de estado — consistência, reatividade, vazamentos |

### ✅ Qualidade e Navegação
| Arquivo | Descrição |
|---|---|
| `forms-validation-review.md` | Revisão de validação de formulários — campos obrigatórios, feedback, UX |
| `flutter-navigation-review.md` | Revisão de fluxos de navegação — rotas, deeplinks, estado de navegação |
| `navigation-flow-review.md` | Auditoria de fluxo completo de navegação entre telas |

### 🔗 Integração
| Arquivo | Descrição |
|---|---|
| `flutter-api-integration.md` | Revisão de integrações com APIs REST — erros, timeouts, cache |
| `flutter-photos-files.md` | Revisão de acesso a fotos e sistema de arquivos em Flutter |
| `flutter-performance-guard.md` | Monitoramento de performance — renderização, janks, memory leaks |

### 📄 Documentação
| Arquivo | Descrição |
|---|---|
| `documentation-consistency-review.md` | Revisão de consistência e completude de documentação técnica |

### 🌾 Domínio Específico
| Arquivo | Descrição |
|---|---|
| `condominio-domain-knowledge.md` | Contexto de domínio para projetos de condomínio rural |
| `trabalhadores-domain-knowledge.md` | Contexto de domínio para gestão de trabalhadores rurais |

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

Skills muito específicas de um único contexto de negócio (como `condominio-domain-knowledge.md`) são permitidas, mas devem ser claramente identificadas como **conhecimento de domínio** — não como regras técnicas universais.

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
