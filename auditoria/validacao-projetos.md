# Relatório de Validação — pasta `projetos/`

> **Data:** Junho 2026
> **Tipo:** Auditoria de estrutura — somente leitura, sem alterações
> **Escopo:** `dev-workspace/projetos/` — 24 projetos catalogados

---

## Resumo Executivo

| Indicador | Resultado |
|---|---|
| Total de projetos catalogados | 24 |
| Projetos com pasta `docs/` | 24 (100%) |
| Projetos com pasta `ai-configs/` | 24 (100%) |
| Projetos com README em `docs/` | **20 (83%)** |
| Projetos sem nenhum arquivo em `docs/` | **4 (17%)** |
| Projetos sem nenhum arquivo em `ai-configs/` | **12 (50%)** |
| Projetos com configs de IA abundantes (>100 arquivos) | 8 |
| Projetos com duplicidades de nome de arquivo em `ai-configs/` | 2 (Transcricao, Server_Oracle) |

**Status geral:** ⚠️ Estrutura presente e consistente, mas com gaps de documentação e configs de IA em projetos menores.

---

## Tabela de Validação Completa

| Projeto | `docs/` | `ai-configs/` | README | Docs (nº) | AI-files (nº) | Status |
|---|---|---|---|---|---|---|
| Agentes base | ✅ | ✅ | ❌ | 0 | 59 | ⚠️ Sem docs |
| Agentes Games | ✅ | ✅ | ✅ | 6 | 128 | ✅ Completo |
| condominio-rural | ✅ | ✅ | ✅ | 4 | 3553 | ✅ Referência |
| DevTrace | ✅ | ✅ | ✅ | 20 | 3474 | ✅ Referência |
| distribuidora-mobile | ✅ | ✅ | ✅ | 3 | 0 | ⚠️ Sem configs IA |
| Documentacao_modelo | ✅ | ✅ | ❌ | 0 | 0 | ❌ Vazia |
| Farol | ✅ | ✅ | ✅ | 9 | 3470 | ✅ Completo |
| Games | ✅ | ✅ | ❌ | 0 | 0 | ❌ Vazia |
| Git_linkedln | ✅ | ✅ | ✅ | 9 | 3489 | ✅ Completo |
| IPMYTV | ✅ | ✅ | ✅ | 9 | 1 | ⚠️ AI incompleto |
| MapMyRepo | ✅ | ✅ | ✅ | 2 | 0 | ⚠️ Sem configs IA |
| My_IA | ✅ | ✅ | ✅ | 4 | 3507 | ✅ Completo |
| organizador_de_aquivos | ✅ | ✅ | ✅ | 1 | 0 | ⚠️ Sem configs IA |
| PixelStory | ✅ | ✅ | ✅ | 9 | 0 | ⚠️ Sem configs IA |
| Projeto_rual_web | ✅ | ✅ | ✅ | 14 | 3563 | ✅ Completo |
| Projeto_rural_python | ✅ | ✅ | ✅ | 15 | 3519 | ✅ Completo |
| robertgferreira | ✅ | ✅ | ✅ | 1 | 0 | ⚠️ Sem configs IA |
| Server_Oracle | ✅ | ✅ | ✅ | 4 | 35 | ⚠️ Ver inconsistências |
| Sistema-agricola | ✅ | ✅ | ❌ | 0 | 0 | ❌ Vazia |
| SmartCopilot-Showcase | ✅ | ✅ | ✅ | 1 | 0 | ⚠️ Sem configs IA |
| smartcopilot-site | ✅ | ✅ | ✅ | 1 | 0 | ⚠️ Sem configs IA |
| Studio IAa | ✅ | ✅ | ✅ | 7 | 0 | ⚠️ Sem configs IA |
| Studio-IA | ✅ | ✅ | ✅ | 1 | 0 | ⚠️ Sem configs IA |
| Transcricao | ✅ | ✅ | ✅ | 9 | 18 | ⚠️ Ver inconsistências |

---

## Detalhamento por Projeto

### ✅ Projetos Referência (docs + configs IA abundantes)

#### `condominio-rural`
- **Docs:** `BRANCHING.md`, `COMMITS.md`, `estrutura.md`, `README.md`
- **AI-configs:** 3.553 arquivos (governance completa copiada)
- **Observação:** Projeto de maior maturidade. Serve como referência de padrão.

#### `DevTrace`
- **Docs:** 20 arquivos — cobertura excepcional (`sdd_pt.md`, `architecture.md`, `flows.md`, `data_model.md`, `ui_spec.md`, `tasks.md`, `acceptance_criteria.md`, etc.)
- **AI-configs:** 3.474 arquivos
- **Observação:** Documentação mais completa de todos os projetos. Alta maturidade.

#### `Farol`
- **Docs:** `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `ROADMAP.md`, `REGRAS_IA.md`, `google_play.md`, `MANUAL_COMPLETO_SMARTCOPILOT.md`, `FIRESTORE_ISSUE.md`, `LICENSE.md`
- **AI-configs:** 3.470 arquivos
- **Observação:** Documentação de produto sólida. Destaque para `REGRAS_IA.md`.

#### `Git_linkedln`
- **Docs:** 9 arquivos — inclui `CONSTITUTION.md` e `SYSTEM.md` (padrão incomum, positivo)
- **AI-configs:** 3.489 arquivos
- **Observação:** Estrutura de governança avançada.

#### `My_IA`
- **Docs:** `README.md`, `AGENTS.md`, `CONTEXT_MYIA.md`, `implementation_plan.md`
- **AI-configs:** 3.507 arquivos
- **Observação:** Projeto de IA sobre IA — contexto rico e configs extensas.

#### `Projeto_rual_web` e `Projeto_rural_python`
- **Docs:** 14 e 15 arquivos respectivamente — incluem `.ai-context.md`, `FEATURES-SDD.md`, `FLOWS.md`, `TASKS.md`
- **AI-configs:** ~3.500 arquivos cada
- **Observação:** Par de projetos irmãos com estrutura espelhada. Alta consistência.

#### `Agentes Games`
- **Docs:** `README.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `ROADMAP.md`, `prompts-especializados-agentes.md`
- **AI-configs:** 128 arquivos
- **Observação:** Boa cobertura documental e configs de IA presentes.

---

### ⚠️ Projetos com Gaps de Documentação ou Configs IA

#### `Agentes base`
- **Docs:** Nenhum arquivo
- **AI-configs:** 59 arquivos (configs presentes, docs ausentes)
- **Sugestão:** Criar `docs/README.md` descrevendo o propósito da coleção de agentes base.

#### `distribuidora-mobile`
- **Docs:** `README.md`, `ASSINAR_APP.md`, `WARNINGS_ASSINATURA.md`
- **AI-configs:** 0 arquivos
- **Sugestão:** Verificar se o repositório original possui configs de IA e reexecutar o script.

#### `IPMYTV`
- **Docs:** 9 arquivos (documentação rica — `SDD.md`, `UX_GUIDELINES.md`, `ARCHITECTURE.md`)
- **AI-configs:** 1 arquivo apenas
- **Sugestão:** Documentação excelente mas configs de IA ausentes. Verificar repositório original.

#### `MapMyRepo`
- **Docs:** `README.md`, `PLANS.md`
- **AI-configs:** 0 arquivos
- **Sugestão:** Verificar se o projeto possui configs de IA no repositório original.

#### `organizador_de_aquivos`
> ⚠️ **Atenção: typo no nome da pasta** — `aquivos` em vez de `arquivos`

- **Docs:** `README.md`
- **AI-configs:** 0 arquivos
- **Sugestão:** Corrigir o nome da pasta no repositório original (se possível) e reexecutar o script. A correção aqui deve aguardar decisão do mantenedor.

#### `PixelStory`
- **Docs:** 9 arquivos (conteúdo rico de game design: `CHARACTER_CREATION.md`, `CLASSES.md`, `EQUIPMENT.md`, `WORLDMAP.md`)
- **AI-configs:** 0 arquivos
- **Sugestão:** Projeto de worldbuilding — verificar se há configs de IA ou se o projeto não utiliza agentes.

#### `robertgferreira`
- **Docs:** `README.md` apenas
- **AI-configs:** 0 arquivos
- **Observação:** Repositório de perfil do GitHub — configuração mínima esperada. Sem ação necessária.

#### `SmartCopilot-Showcase`, `smartcopilot-site`, `Studio-IA`
- **Docs:** `README.md` apenas
- **AI-configs:** 0 arquivos
- **Sugestão:** Verificar repositórios originais para enriquecer o catálogo.

#### `Studio IAa`
- **Docs:** 7 arquivos — `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTEXT_StudioIA.md`, `CONTRIBUTING.md`, `README.md`, `README_StudioIA.md`, `ROADMAP.md`
- **AI-configs:** 0 arquivos
- **Observação:** Documentação boa. Presença de dois READMEs (`README.md` + `README_StudioIA.md`) — possível duplicidade. Verificar qual é o canônico.
- **Sugestão:** Confirmar com o mantenedor qual README deve ser o principal.

---

### ❌ Projetos Vazios (pastas existem mas sem conteúdo)

#### `Documentacao_modelo`
- **Docs:** 0 arquivos
- **AI-configs:** 0 arquivos
- **Sugestão:** Verificar se este projeto ainda existe no repositório original ou se deve ser removido do catálogo. Aguardar decisão do mantenedor.

#### `Games`
- **Docs:** 0 arquivos
- **AI-configs:** 0 arquivos
- **Sugestão:** Mesmo que `Documentacao_modelo` — pasta vazia sem conteúdo. Verificar origem.

#### `Sistema-agricola`
- **Docs:** 0 arquivos
- **AI-configs:** 0 arquivos
- **Sugestão:** Projeto sem documentação copiada. Pode indicar que o repositório original não possui arquivos `.md` na raiz. Reexecutar scan para confirmar.

---

### ⚠️ Inconsistências Identificadas

#### `Server_Oracle` — Arquivos `.pyc` e `.py` em `ai-configs/`
- **Arquivos detectados:** `all_agents.cpython-314.pyc`, `base.cpython-314.pyc`, `__init__.cpython-314.pyc`, `coder_skills.py`, `config_generator.py`, `monitor_skills.py`, `planner_skills.py`, `security_skills.py`
- **Problema:** Arquivos de código Python compilado (`.pyc`) e arquivos de skills em Python foram copiados para `ai-configs/`. Estes não são configs de IA no sentido do workspace (não são `.md`, `.prompt`, `.skill.ai`).
- **Sugestão:** Revisar o filtro do script `organize_workspace.py` para excluir arquivos `.pyc` e `.py` da cópia para `ai-configs/`. Não excluir agora — apenas registrado.

#### `Server_Oracle` — Múltiplos `SKILL.md` com mesmo nome
- **Arquivos detectados:** 13 arquivos com o nome `SKILL.md`
- **Problema:** O script copiou skills de diferentes subdiretórios, mas como todos têm o mesmo nome, pode ter ocorrido sobrescrição. Apenas o último arquivo copiado pode ter sobrevivido.
- **Sugestão:** Verificar se o script preservou os arquivos com subdiretórios ou se houve perda de dados. Reexecutar com flatten desativado se necessário.

#### `Transcricao` — Múltiplos `SKILL.md` com mesmo nome
- **Arquivos detectados:** 17 arquivos chamados `SKILL.md` + 1 `SKILLS.md`
- **Problema:** Mesma situação do `Server_Oracle` — possível sobrescrição durante a cópia.
- **Sugestão:** Verificar o repositório original para confirmar quantas skills únicas existem.

---

## Checklist de Ações Sugeridas

> ⚠️ **Nenhuma ação foi executada.** Este checklist é apenas sugestão — todas as ações requerem aprovação do mantenedor.

```
[ ] 1. Reexecutar organize_workspace.py nos projetos com ai-configs/ vazio:
        - distribuidora-mobile
        - MapMyRepo
        - PixelStory
        - SmartCopilot-Showcase / smartcopilot-site / Studio-IA / Studio IAa

[ ] 2. Criar README.md mínimo em docs/ para projetos sem documentação:
        - Agentes base
        - (Documentacao_modelo, Games, Sistema-agricola — após confirmar se devem permanecer)

[ ] 3. Confirmar o status de pastas completamente vazias:
        - Documentacao_modelo → ativo ou arquivar?
        - Games → ativo ou arquivar?
        - Sistema-agricola → sem .md no repositório original?

[ ] 4. Corrigir o typo no nome da pasta:
        - organizador_de_aquivos → organizador_de_arquivos
        (Somente após confirmar se a correção deve acontecer no repositório original também)

[ ] 5. Revisar o script organize_workspace.py para:
        - Excluir arquivos .pyc da cópia para ai-configs/
        - Preservar estrutura de subdiretórios ao copiar skills com mesmo nome

[ ] 6. Verificar Studio IAa:
        - README.md vs README_StudioIA.md — qual é o canônico?

[ ] 7. Verificar IPMYTV:
        - Repositório original possui configs de IA? Por que apenas 1 arquivo foi copiado?
```

---

## Projetos com Documentação Exemplar (Referência para os demais)

| Projeto | Por que é referência |
|---|---|
| `DevTrace` | 20 docs cobrindo SDD, arquitetura, flows, UI spec, acceptance criteria |
| `condominio-rural` | Governança completa — branching, commits, estrutura clara |
| `Farol` | Docs de produto + `REGRAS_IA.md` como padrão de governança |
| `Projeto_rural_python` | `.ai-context.md` + `FEATURES-SDD.md` + `FLOWS.md` como padrão de contexto |
| `Git_linkedln` | `CONSTITUTION.md` + `SYSTEM.md` como inovação de governança |

---

*Relatório gerado por auditoria manual de estrutura — nenhuma alteração foi feita nos arquivos ou pastas.*
