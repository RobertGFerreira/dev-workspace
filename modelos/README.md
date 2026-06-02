# modelos/

> Biblioteca de referência do `dev-workspace` — artefatos padronizados e reutilizáveis para agentes, documentação, prompts e skills.

---

## Propósito

A pasta `modelos/` é a **biblioteca oficial de padrões** do workspace. Ela reúne os artefatos de maior qualidade e maior grau de generalização, extraídos da experiência acumulada nos projetos catalogados.

Seu papel é garantir que novos projetos ou configurações comecem de um patamar de qualidade elevado, sem precisar reinventar estruturas básicas ou reproduzir erros já corrigidos.

> **Esta pasta não é um repositório de código.** É uma coleção de referências — modelos, instruções, definições e padrões que devem ser adaptados, não copiados cegamente.

---

## Organização Interna

```
modelos/
├── agentes/     ← Definições de agentes de IA por papel e domínio
├── docs/        ← Templates e documentos-base para projetos
├── prompts/     ← Instruções reutilizáveis por tipo de tarefa
└── skills/      ← Capacidades técnicas modulares para agentes
```

Cada subpasta é independente, mas os artefatos se complementam. A relação entre eles forma a espinha dorsal da configuração de IA de qualquer projeto.

---

## As Quatro Categorias e Suas Relações

### `agentes/`
Definem **quem faz o quê**. Um agente é uma entidade de IA com identidade, escopo e regras de comportamento. Cada agente referencia prompts e skills que ampliam sua capacidade de atuação.

### `docs/`
Define **o que deve existir como documentação**. Os templates desta pasta cobrem desde READMEs e changelogs até documentos de design de software (SDD), arquitetura e contribuição. São usados na inicialização e manutenção de projetos.

### `prompts/`
Definem **como tarefas específicas devem ser conduzidas**. São instruções reutilizáveis que direcionam a ação de agentes ou ferramentas de IA para um objetivo concreto — revisar código, gerar documentação, planejar uma sprint, etc.

### `skills/`
Definem **capacidades especializadas e modulares**. Uma skill é um conjunto de critérios, verificações ou conhecimentos técnicos que um agente pode invocar para ampliar sua atuação em domínios específicos — como revisão de banco de dados, análise de UI ou conformidade de segurança.

---

## Tipos de Artefatos por Subpasta

| Subpasta | Tipos de arquivos esperados |
|---|---|
| `agentes/` | `<nome-do-agente>.md` — definição completa de agente; `AGENTE_UNIVERSAL.template.md` — base para novos agentes |
| `docs/` | `README.template.md`, `SDD_UNIVERSAL.template.md`, `ARCHITECTURE.template.md`, `CHANGELOG.template.md`, etc. |
| `prompts/` | `<nome-do-prompt>.md` — prompt operacional por tarefa; `PROMPT_UNIVERSAL.template.md` — base para novos prompts |
| `skills/` | `<nome-da-skill>.md` — skill técnica por domínio; `SKILL_UNIVERSAL.template.md` — base para novas skills |

Arquivos com sufixo `.template.md` são os modelos universais — contêm instruções de preenchimento e são o ponto de partida para criar novos artefatos.

---

## Critérios de Curadoria

Um artefato só entra em `modelos/` se atender a estes critérios:

| Critério | Descrição |
|---|---|
| **Generalidade** | Aplicável a mais de um projeto, sem dependências específicas |
| **Completude** | Cobre todos os campos esperados para o seu tipo |
| **Clareza** | Qualquer colaborador consegue entender e usar sem ajuda externa |
| **Testado** | Já foi aplicado em pelo menos um projeto real e funcionou |
| **Sem segredos** | Nenhum dado sensível, token, senha ou caminho absoluto de máquina |

Artefatos muito específicos de um único projeto devem ficar no repositório daquele projeto, em `governance/` ou pasta equivalente.

---

## Fluxo de Evolução dos Modelos

```
Projeto Real
    │
    ├─► Cria agente/prompt/skill específico
    │
    ├─► Artefato se prova eficaz e reutilizável
    │
    ├─► Generalização: remove dados específicos, adiciona instruções
    │
    └─► Entra em modelos/ após revisão e validação
           │
           ├─► Outros projetos adotam o artefato
           │
           └─► Feedback gera nova versão do modelo (não apaga a anterior)
```

**Regras de evolução:**
1. Novos modelos entram com base em evidência — não por especulação.
2. Modelos existentes podem ser melhorados, mas nunca apagados sem substituto.
3. Quando um modelo for obsoleto, mova-o para um subdiretório `_deprecated/` em vez de deletar.
4. Toda mudança significativa em um modelo deve ser versionada via `git commit`.

---

## Padrão de Qualidade

Todo artefato em `modelos/` deve ser escrito com o mesmo cuidado de um documento técnico profissional:

- **Linguagem**: clara, objetiva, sem ambiguidades.
- **Estrutura**: seções bem definidas, títulos descritivos, hierarquia consistente.
- **Instruções**: explícitas sobre o que preencher, o que evitar, o que é obrigatório.
- **Exemplos**: curtos, ilustrativos, sem dados reais.
- **Manutenibilidade**: nenhum campo hardcoded que force edição em múltiplos lugares.

---

## Relação com os Projetos Reais

Os artefatos em `modelos/` **não pertencem** a nenhum projeto específico — são propriedade do workspace. O fluxo correto de uso é:

1. **Copie** o artefato desejado para o repositório do projeto.
2. **Adapte** o conteúdo às especificidades do projeto.
3. **Não modifique** o original em `modelos/` — edite apenas a cópia no projeto.
4. **Se a adaptação gerar um padrão melhor**, generalize e proponha uma atualização ao modelo original.

> Consulte [`auditoria/relatorio-geral.md`](../auditoria/relatorio-geral.md) para ver quais projetos já adotaram estes modelos.

---

## Navegação Rápida

- 📁 [agentes/](agentes/README.md) — Definições de agentes por tipo e domínio
- 📁 [docs/](docs/README.md) — Templates de documentação e documentos-base
- 📁 [prompts/](prompts/README.md) — Biblioteca de instruções por tipo de tarefa
- 📁 [skills/](skills/README.md) — Capacidades técnicas modulares

---

*Mantenha esta pasta organizada. Cada artefato aqui representa um padrão consolidado — trate-o com o rigor de um produto.*
