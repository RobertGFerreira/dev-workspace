# Notas Master da Triagem

## Visao geral

Esta e a fonte unica de observacoes da pasta `triagem/`.

A triagem continua separada da biblioteca oficial em `modelos/`. Nada nesta pasta instala agentes, altera governanca ou substitui arquivos oficiais. A incorporacao so deve ocorrer depois de decisao registrada e pela autoridade correta.

Regras operacionais:

1. Usar `triagem/` como area de auditoria e comparacao.
2. Manter `Utils/` como referencia externa local fora do Git.
3. Nao criar `notas.md` locais por agente, skill, prompt ou pasta.
4. Registrar observacoes, decisoes, fusoes, divisoes, descartes e proximos passos somente neste arquivo.
5. Se algo virar oficial, criar ou alterar em `modelos/` pelo fluxo de governanca aplicavel.

## Fontes analisadas

| Fonte | Tipo | Resultado | Decisao |
|:---|:---|:---|:---|
| `modelos/` | Biblioteca oficial local | Fonte normativa de agentes, prompts, skills e SDD. | Base de comparacao. |
| `Utils/antigravity-awesome-skills-main` | Local externa | Catalogo amplo com skills, plugins, docs e scripts. | Usar como referencia; manter fora do Git. |
| `Utils/1250 Skills` | Local externa | Dump heterogeneo com catalogos e bundles. | Referencia secundaria. |
| `sickn33/antigravity-awesome-skills` | Externa | Catalogo muito amplo, com mais de 1.500 skills e instaladores. | Nao incorporar em massa. |

## Arquivos copiados para analise

| Item | Tipo | Origem | Destino na triagem | Acao recomendada |
|:---|:---|:---|:---|:---|
| `agente-base-universal` | Agente | `modelos/agentes` | `agentes/agente-base-universal/AGENTE.md` | Manter como modelo de heranca. |
| `orquestrador-agentes` | Agente | `modelos/agentes` | `agentes/orquestrador-agentes/AGENTE.md` | Manter enxuto. |
| `agente-configuracao-governanca` | Agente | `modelos/agentes` | `agentes/agente-configuracao-governanca/AGENTE.md` | Manter como guardiao exclusivo. |
| `documentacao-requisitos` | Agente | `modelos/agentes` | `agentes/documentacao-requisitos/AGENTE.md` | Manter com escopo vigiado. |
| `spec-agent` | Agente | `modelos/agentes` | `agentes/spec-agent/AGENTE.md` | Manter para SDD e Spec Kit. |
| `google-play-support` | Agente | `modelos/agentes` | `agentes/google-play-support/AGENTE.md` | Manter subordinado a documentacao. |
| `criador-games` | Agente | `modelos/agentes` | `agentes/criador-games/AGENTE.md` | Manter como orquestrador de games. |
| `criador-conteudo` | Agente | `modelos/agentes` | `agentes/criador-conteudo/AGENTE.md` | Manter como orquestrador de conteudo. |
| `flutter-revisor-codigo` | Agente | `modelos/agentes` | `agentes/dev-flutter-backend/` | Manter. |
| `flutter-ui-ux-pro` | Agente | `modelos/agentes` | `agentes/dev-flutter-backend/` | Manter. |
| `agente-api-contratos` | Agente | `modelos/agentes` | `agentes/dev-flutter-backend/` | Manter; pode receber referencia de API docs. |
| `agente-ci-cd` | Agente | `modelos/agentes` | `agentes/dev-flutter-backend/` | Manter. |
| `seguranca-conformidade` | Agente | `modelos/agentes` | `agentes/dev-flutter-backend/` | Manter; evitar skills ofensivas externas. |

## Agentes

| Agente ou grupo | Situacao | Decisao | Observacao |
|:---|:---|:---|:---|
| `agente-base-universal` | Valido | Manter como agente modelo. | Nao dividir e nao fundir. Serve como base minima de heranca e escopo. |
| `agente-configuracao-governanca` | Valido | Preservar exclusividade. | Referencias externas so podem reforcar limites, nunca ampliar permissao. |
| `orquestrador-agentes` | Valido | Manter enxuto. | Coordena, classifica e cria plan/tasks; nao edita governanca. |
| `documentacao-requisitos` | Valido, mas amplo | Manter com delegacao clara. | Coordena frente documental; deve delegar Google Play, conteudo e validacao markdown quando houver especialista. |
| `spec-agent` | Valido | Manter. | Mantem SDD master/derivado e Spec Kit; nao edita agentes sem `/guard`. |
| `google-play-support` | Valido | Manter subordinado a documentacao. | Pode usar terminal apenas para validacao tecnica pratica dentro do escopo da tarefa. |
| `criador-games` | Valido | Manter como orquestrador de games. | Godot fica como referencia/modelo ate existir projeto real. |
| `criador-conteudo` | Valido | Manter como orquestrador de conteudo. | Evitar importar pacote editorial amplo sem demanda. |
| `dev-flutter-backend` | Grupo de triagem | Manter como agrupamento, nao como agente oficial. | Facilita comparar Flutter, API, CI/CD, performance e seguranca. |

## Skills

| Skill ou referencia | Origem | Compatibilidade | Acao recomendada | Motivo |
|:---|:---|:---|:---|:---|
| `scope-control` | Local | Alta | Manter. | Essencial para evitar agentes grandes demais. |
| `documentation-consistency-review` | Local | Alta | Manter. | Boa skill transversal para aderencia documental. |
| `content-orchestration` | Local | Alta | Manter. | Alinha ao papel do `criador-conteudo`. |
| `agents-md` | Externa | Media | Usar como modelo. | Boa orientacao para instrucoes curtas; precisa PT-BR e governanca local. |
| `documentation-templates` | Externa | Media | Usar como referencia. | Templates oficiais do projeto prevalecem. |
| `architecture-decision-records` | Externa | Media | Fundir/adaptar. | Pode virar checklist ADR enxuto. |
| `app-store-optimization` | Externa | Media | Fundir parcialmente. | Extrair apenas Google Play/ASO util. |
| `android_ui_verification` | Externa | Media | Usar como modelo futuro. | Adaptar de React Native para Flutter/Android e terminal controlado. |
| `app-store-changelog` | Externa | Baixa atual | Usar como referencia. | Pode apoiar release notes, mas nao e essencial. |
| `game-development` | Externa | Media | Usar como referencia. | Muito ampla para skill oficial. |
| `godot-gdscript-patterns` | Externa | Media futura | Usar como modelo. | Bom recorte por motor, linguagem e padroes. |
| `godot-4-migration` | Externa | Baixa atual | Usar como referencia. | So faz sentido em projeto Godot legado. |
| `flutter-expert` | Externa | Baixa para copia | Usar como referencia. | Ampla demais; skills Flutter locais sao mais modulares. |
| `api-documentation` | Externa | Media | Fundir. | Pode reforcar `agente-api-contratos`. |
| `api-design-principles` | Externa | Media | Usar como referencia. | Apoia desenho de contratos sem virar skill oficial agora. |
| `multi-agent-patterns` | Externa | Baixa para copia | Usar como referencia. | Pode conflitar com autoridade local. |
| `agent-orchestration-multi-agent-optimize` | Externa | Baixa para copia | Usar como referencia. | Evitar instalar agora. |
| `autonomous-agent-patterns` | Externa | Baixa para copia | Usar como referencia. | Pode inspirar limites de autonomia, sem ampliar autoridade. |
| `agent-evaluation` | Externa | Media futura | Usar como referencia. | Pode apoiar validacao de SDD, nao instalar agora. |
| `content-strategy` | Externa | Media | Usar como referencia. | Conteudo local ja tem skills especificas. |
| `content-creator` | Externa | Baixa para copia | Usar como referencia. | Amplo e potencialmente redundante. |

## Prompts

Prompts locais copiados para triagem devem permanecer vinculados ao agente correspondente em `triagem/agentes/<agente>/prompts/`.

Decisoes:

1. Nao criar prompt oficial a partir da triagem sem decisao registrada.
2. Nao substituir prompt universal por prompt especifico.
3. Prompts de orquestradores devem manter coordenacao e handoff, sem permissao estrutural.
4. Prompts de especialistas devem manter escopo unico e nao invadir orquestracao.
5. Qualquer mudanca estrutural em prompt de agente oficial deve passar pelo guardiao.

## Modelos sugeridos

| Item | Tipo | Uso recomendado |
|:---|:---|:---|
| `agents-md` | Skill | Modelo para revisar instrucoes `AGENTS.md` curtas e operacionais. |
| `android_ui_verification` | Skill | Modelo para validacao Android/ADB controlada por escopo. |
| `godot-gdscript-patterns` | Skill | Modelo para futura skill Godot, se houver projeto real. |
| `architecture-decision-records` | Skill | Modelo para checklist ADR enxuto. |

## Referencias

| Item | Uso |
|:---|:---|
| `flutter-expert` | Inventario de capacidades Flutter; nao copiar como skill oficial. |
| `game-development` | Referencia ampla para games. |
| `documentation-templates` | Comparar com templates oficiais antes de adaptar. |
| `api-design-principles` | Apoiar contratos e documentacao de API. |
| `multi-agent-patterns` | Referencia conceitual; nao altera autoridade local. |
| `agent-evaluation` | Referencia futura para validacao de SDD. |

## Fusoes recomendadas

| Origem | Fundir com | Motivo |
|:---|:---|:---|
| `architecture-decision-records` | `agente-arquitetura` + `documentation-consistency-review` | Criar checklist ADR enxuto sem nova autoridade. |
| `api-documentation` | `agente-api-contratos` | Manter documentacao de API junto de contratos. |
| `app-store-optimization` | `store-listing-optimization` | Evitar skill ASO ampla demais. |
| `agents-md` | `documentacao-requisitos` ou futura `agent-instructions-review` | Reforcar docs de agentes sem duplicar governanca. |

## Divisoes recomendadas

| Item | Divisao sugerida | Motivo |
|:---|:---|:---|
| `documentacao-requisitos` | Manter coordenacao documental; delegar Google Play, conteudo e validacao markdown. | Evitar agente documental grande demais. |
| `flutter-expert` externo | Separar em UI, estado, performance, API e lint. | A modularizacao local ja segue esse desenho. |
| `game-development` externo | Separar em estrutura, narrativa, criativo, monetizacao e motor. | Alinha com agentes de games. |

## Descartes

| Item | Motivo |
|:---|:---|
| Instalacao completa da AAS | Importacao em massa e conflito com selecao minima. |
| Skills cloud especificas sem demanda | Sem evidencia de uso imediato. |
| Skills ofensivas de seguranca sem escopo autorizado | Risco operacional e governanca. |
| Skills de marketing/SEO em massa | Fora da prioridade atual. |
| Agentes externos de meta-orquestracao | Risco de conflito com guardiao e orquestrador locais. |
| Godot como agente oficial agora | Sem projeto Godot real no ecossistema atual. |

## Ajustes recomendados

| Area | Ajuste | Prioridade |
|:---|:---|:---:|
| Agentes | Nao criar agente Godot agora; criar apenas se houver projeto Godot real. | Media |
| Agentes | Manter `google-play-support` subordinado a `documentacao-requisitos`. | Alta |
| Agentes | Manter `documentacao-requisitos` como coordenador documental, nao guardiao estrutural. | Alta |
| Skills | Criar no futuro `android-ui-verification` adaptada para Flutter/ADB, se houver demanda. | Media |
| Skills | Criar no futuro `agent-instructions-review` baseada em `agents-md`, se houver revisao recorrente de `AGENTS.md`. | Media |
| Skills | Manter skills Flutter modulares; nao copiar `flutter-expert` como skill oficial. | Alta |
| Documentacao | Manter esta triagem separada de `modelos/`. | Alta |
| Git | Manter `Utils/` no `.gitignore`. | Alta |

## Politica de instalacao condicional

Decisao consolidada: a triagem pode sugerir candidatos, mas a instalacao operacional deve ser condicional por projeto.

| Item | Tipo | Condicao de criacao | Variavel | Observacao |
|:---|:---|:---|:---|:---|
| Google Play | Opcional | Projeto Android/Flutter com publicacao Android confirmada | `ENABLE_GOOGLE_PLAY_AGENT` | Subordinado a `documentacao-requisitos`; nao vira orquestrador. |
| Godot | Opcional | Projeto de game com Godot/GDScript confirmado | `ENABLE_GODOT_AGENT` | Usar `criador-games` e especialistas; nao criar agente monolitico. |
| Raspagem publica | Opcional | Pesquisa em fontes publicas permitidas | `ENABLE_SCRAPING_AGENT` | Bloquear login, captcha, paywall, bypass e violacao de termos. |
| Seguranca | Transversal | App, API, DB, auth, release ou dados sensiveis | `ENABLE_SECURITY_AGENTS` | Reforcar `seguranca-conformidade` antes de subdividir agentes. |
| LGPD | Transversal | Dados pessoais de usuarios no Brasil | `ENABLE_LGPD_AGENT` | Tratar privacidade como criterio de arquitetura e documentacao. |

## Proximos passos

1. Revisar manualmente os arquivos copiados em `triagem/agentes/*/referencias`.
2. Escolher no maximo uma skill candidata para adaptacao por vez.
3. Se a candidata virar oficial, criar em `modelos/skills/` e atualizar `modelos/skills/README.md`.
4. Se afetar agentes, acionar `/guard`.
5. Nao copiar nada de `triagem/` para `modelos/` sem decisao registrada.
