# dev-workspace

> **Espaço centralizado de desenvolvimento pessoal** — catalogação de projetos, auditorias de configuração de IA e biblioteca de modelos reutilizáveis para projetos Flutter, Data Engineering e IoT.

---

## Visão Geral

O `dev-workspace` é o repositório central de governança e documentação do portfólio de desenvolvimento. Ele **não contém código-fonte** de nenhum projeto — seu papel é organizar, auditar e padronizar os projetos que existem em outros repositórios.

Aqui ficam:
- cópias curadas de documentação dos projetos (READMEs, specs, configs de IA),
- relatórios de auditoria de qualidade e maturidade de IA,
- modelos universais reutilizáveis para novos projetos.

---

## Objetivo

| Objetivo | Descrição |
|---|---|
| **Catalogar** | Manter um inventário atualizado de todos os projetos ativos |
| **Auditar** | Avaliar a maturidade de documentação e configuração de IA por projeto |
| **Padronizar** | Fornecer modelos universais que garantam consistência entre projetos |
| **Preservar** | Garantir que nenhuma informação crítica seja perdida ou sobrescrita sem controle |

---

## Estrutura de Pastas

```
dev-workspace/
├── README.md                    ← Este arquivo (entrada principal do workspace)
├── organize_workspace.py        ← Script de automação para catalogação e cópia
├── scan_results_full.json       ← Resultado bruto do último scan de projetos
│
├── projetos/                    ← Cópias curadas de docs e configs de IA por projeto
│   ├── condominio-rural/
│   │   ├── docs/                ← READMEs, specs, PRDs copiados do repositório original
│   │   └── ai-configs/          ← Configs de IA (agentes, prompts, skills) do projeto
│   ├── distribuidora-mobile/
│   ├── SmartCopilot-Showcase/
│   └── ...                      ← Um subdiretório por projeto catalogado (24 no total)
│
├── modelos/                     ← Biblioteca de templates universais reutilizáveis
│   ├── docs/
│   │   ├── DOCUMENTO_UNIVERSAL.template.md   ← Template geral de documentação
│   │   └── SDD_UNIVERSAL.template.md         ← Software Design Document
│   ├── agentes/
│   │   └── AGENTE_UNIVERSAL.template.md      ← Definição de agente de IA
│   ├── prompts/
│   │   └── PROMPT_UNIVERSAL.template.md      ← Engenharia de prompts
│   └── skills/
│       └── SKILL_UNIVERSAL.template.md       ← Validação de skill de IA
│
└── auditoria/                   ← Relatórios gerados de auditoria por projeto
    ├── relatorio-geral.md       ← Inventário consolidado de todos os projetos
    └── condominio-rural.md      ← Auditoria detalhada do projeto condominio-rural
```

---

## Fluxo de Trabalho

### 1. Catalogação

Quando um novo projeto precisa ser registrado:

1. Execute `organize_workspace.py` para varrer os repositórios locais.
2. O script copia automaticamente todos os `.md` e configs de IA para `projetos/<nome>/`.
3. Revise o output em `scan_results_full.json` para confirmar o mapeamento.

```powershell
# Executar o script de catalogação
python organize_workspace.py
```

### 2. Auditoria

Para cada projeto catalogado, gere um relatório de auditoria:

1. Analise os arquivos em `projetos/<nome>/ai-configs/` e `projetos/<nome>/docs/`.
2. Avalie: presença de agentes, qualidade de prompts, cobertura de skills, maturidade do README.
3. Salve o resultado em `auditoria/<nome-do-projeto>.md`.

### 3. Consolidação de Modelos

Quando um padrão de qualidade for identificado em algum projeto:

1. Extraia o padrão (agente, prompt, skill, doc).
2. Generalize o conteúdo removendo dados específicos do projeto.
3. Salve o modelo universal em `modelos/<categoria>/NOME.template.md`.

### 4. Manutenção

- Rode `organize_workspace.py` sempre que projetos forem criados ou modificados.
- Atualize o relatório `auditoria/relatorio-geral.md` após cada ciclo de catalogação.
- Revise os modelos em `modelos/` quando novas boas práticas forem identificadas.

---

## Como Adicionar um Novo Projeto

Siga este checklist ao incorporar um novo repositório ao workspace:

```
[ ] 1. Execute organize_workspace.py para copiar docs e configs de IA
[ ] 2. Verifique se a pasta projetos/<nome>/ foi criada corretamente
[ ] 3. Confirme se docs/ contém o README.md do projeto
[ ] 4. Confirme se ai-configs/ contém os agentes, prompts e skills
[ ] 5. Classifique o projeto: Privado | Showcase | Site
[ ] 6. Atualize auditoria/relatorio-geral.md com a nova entrada
[ ] 7. (Opcional) Gere uma auditoria completa em auditoria/<nome>.md
[ ] 8. (Opcional) Atualize o README do projeto original usando o template padrão
```

**Classificação de projetos:**

| Tipo | Descrição | Nível de detalhe esperado |
|---|---|---|
| **Privado** | Produto real, uso pessoal ou comercial | Alto — docs técnicas completas, SDDs, agentes |
| **Showcase** | Repositório público para portfólio | Médio — README impecável, demo funcional |
| **Site** | Landing page ou site estático | Leve — apenas README e stack |

---

## Projetos Catalogados

> Atualizado em: Junho/2026 — 24 projetos

| Projeto | Tipo | README | Config IA |
|---|---|---|---|
| condominio-rural | Privado | ✅ | ✅ Agentes + Skills |
| distribuidora-mobile | Privado | ✅ | ✅ |
| SmartCopilot-Showcase | Showcase | ✅ | ✅ |
| DevTrace | Showcase | ✅ | ✅ |
| Farol | Privado | ✅ | ✅ |
| MapMyRepo | Showcase | ✅ | ✅ |
| PixelStory | Showcase | ✅ | ⚠️ Parcial |
| Studio-IA | Privado | ✅ | ✅ |
| IPMYTV | Privado | ✅ | ⚠️ Parcial |
| smartcopilot-site | Site | ✅ | ❌ |
| robertgferreira | Showcase | ✅ | ❌ |
| *demais projetos* | — | — | — |

> Para o inventário completo e detalhado, consulte [`auditoria/relatorio-geral.md`](auditoria/relatorio-geral.md).

---

## Modelos Disponíveis

Todos os templates estão em `modelos/` e são **genéricos e reutilizáveis**:

| Modelo | Caminho | Uso |
|---|---|---|
| Documentação Universal | `modelos/docs/DOCUMENTO_UNIVERSAL.template.md` | README e docs gerais de projeto |
| SDD Universal | `modelos/docs/SDD_UNIVERSAL.template.md` | Software Design Document |
| Agente Universal | `modelos/agentes/AGENTE_UNIVERSAL.template.md` | Definição de agente de IA |
| Prompt Universal | `modelos/prompts/PROMPT_UNIVERSAL.template.md` | Engenharia de prompts |
| Skill Universal | `modelos/skills/SKILL_UNIVERSAL.template.md` | Validação de skill de IA |

**Para usar um template:**
1. Copie o arquivo para o repositório de destino.
2. Renomeie conforme o contexto (`README.md`, `agente-backend.md`, etc.).
3. Preencha cada seção seguindo as instruções internas do template.
4. Remova as instruções após o preenchimento.

---

## Segurança e Preservação de Arquivos

> ⚠️ **Regra fundamental:** nada neste workspace deve ser apagado sem autorização explícita.

- **Nunca sobrescreva** arquivos em `projetos/` sem confirmar com o proprietário do repositório original.
- **Nunca delete** entradas de `auditoria/` — relatórios antigos têm valor histórico.
- **Sempre versione** alterações via `git commit` antes de modificar modelos em `modelos/`.
- Arquivos copiados em `projetos/` são **cópias de referência**, não os originais — edite sempre nos repositórios de origem.
- Secrets, tokens, senhas e dados sensíveis **jamais** devem ser copiados para este workspace.

---

## Automação

O script [`organize_workspace.py`](organize_workspace.py) realiza as seguintes operações automaticamente:

- Varre todos os repositórios em `C:\Users\Robert\Documents\GitHub\`
- Copia arquivos `.md`, `README`, `CHANGELOG`, `PRD` para `projetos/<nome>/docs/`
- Copia configs de IA (`.antigravity/`, `governance/`, `agents/`, `skills/`, `prompts/`) para `projetos/<nome>/ai-configs/`
- Ignora diretórios de build (`node_modules/`, `.dart_tool/`, `build/`, `dist/`, `.git/`)
- Gera `scan_results_full.json` com o resultado completo do scan

---

## Contato e Responsável

| Campo | Valor |
|---|---|
| **Mantenedor** | Robert G. Ferreira |
| **GitHub** | [@robertgferreira](https://github.com/robertgferreira) |
| **Última atualização** | Junho 2026 |

---

*Este workspace é um instrumento de governança pessoal. Trate-o com o mesmo cuidado que você trata os projetos que ele documenta.*
