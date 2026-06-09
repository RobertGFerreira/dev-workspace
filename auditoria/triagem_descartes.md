# Registro de Triagem e Descartes

Este documento registra a análise técnica e curadoria da pasta temporária `triagem/`, indicando quais componentes foram incorporados à biblioteca oficial de modelos (`modelos/`) e quais foram rejeitados, com suas respectivas justificativas.

---

## 1. Itens Incorporados e Adaptados

Os seguintes itens possuíam escopo claro e valor durável, tendo sido adaptados para formato universal e incorporados aos modelos oficiais:

| Item de Origem | Destino / Ação | Justificativa |
| :--- | :--- | :--- |
| `agents-md.SKILL.md` | `modelos/skills/agent-instructions-review.md` | Valioso para auditoria de arquivos `AGENTS.md` e `CLAUDE.md`. Traduzido para PT-BR e universalizado. |
| `architecture-decision-records.SKILL.md` | Fundido em `agente-arquitetura.md` e `documentation-consistency-review.md` | Adicionado o checklist e o padrão estruturado de ADRs para os agentes universais de arquitetura e documentação. |
| `api-documentation.SKILL.md` | Fundido em `agente-api-contratos.md` | Incorporou-se a validação de geração de OpenAPI specs, exemplos de requests e guides na identidade do agente de APIs. |
| `app-store-optimization.SKILL.md` | Fundido em `store-listing-optimization.md` | Detalhou-se as limitações específicas da Apple Store e do Google Play Console e regras de ASO no modelo de skill existente. |

---

## 2. Itens Rejeitados / Descartados

Os seguintes itens foram avaliados e descartados por não apresentarem utilidade operacional imediata, possuírem redundância ou por estarem fora do escopo universal do repositório:

| Item | Origem | Motivo do Descarte |
| :--- | :--- | :--- |
| `android_ui_verification.SKILL.md` | `triagem/skills/google-play-android/` | Exigia uso avançado de ADB e automação de interface visual específica que não possui projeto-alvo ativo no momento. |
| `godot-gdscript-patterns.SKILL.md` | `triagem/skills/games-godot/` | Modelagem de padrões GDScript. Foi postergada e não incorporada por falta de um projeto Godot real ativo no ecossistema. |
| Agentes e Prompts Godot específicos | `triagem/agentes/` | Agentes técnicos propostos (como `godot-gameplay-systems`, `godot-engineer`, etc.) foram descartados temporariamente. A criação de agentes especializados exige demanda prática real ativa. |
| `game-development.SKILL.md` | `triagem/skills/games-godot/` | Genérico demais. O domínio de jogos já está estruturado nas skills específicas de games (`game-loop-design`, etc.). |
| `godot-4-migration.SKILL.md` | `triagem/skills/games-godot/` | Específico para migração de versão da engine Godot, sem utilidade geral durável. |
| `app-store-changelog.SKILL.md` | `triagem/skills/google-play-android/` | Redundante. O padrão de logs e release notes já é coberto pela documentação universal de releases. |
| `flutter-expert.SKILL.md` | `triagem/skills/dev-flutter-backend/` | Amplo demais. Nossos modelos de skills Flutter oficiais já são modulares e focados (UI, Estado, Performance, SQLite). |
| Outros Dumps de IA externos | `Utils/` | Importação em massa e conflito com a curadoria mínima. Devem permanecer fora do Git. |

---

*Registro concluído em Junho de 2026.*
