# Auditoria Seletiva de Skills Externas

## 1. Diagnostico das fontes analisadas

| Fonte | Tipo | Diagnostico | Acao recomendada |
|:---|:---|:---|:---|
| `sickn33/antigravity-awesome-skills` | Repositorio externo | Catalogo amplo com mais de 1.500 skills, bundles e plugins. Util como referencia, perigoso como importacao direta. | Usar como referencia e fonte de ideias. |
| `Utils/antigravity-awesome-skills-main` | Copia local externa | Espelha o repositorio externo, com `CATALOG.md`, skills, plugins, docs, scripts e testes. | Manter fora do Git; auditar por catalogo. |
| `Utils/1250 Skills` | Dump local | Catalogo grande, heterogeneo e menos alinhado ao nosso padrao. | Usar apenas como referencia secundaria. |
| `modelos/` | Biblioteca mestre local | Ja possui agentes, prompts e skills focados na nossa governanca. | Fonte normativa local. |

Conclusao: nao incorporar em massa. A utilidade real esta em extrair padroes pontuais para fortalecer skills ja existentes.

## 2. Inventario resumido

| Origem | Itens observados | Observacao |
|:---|:---|:---|
| `antigravity-awesome-skills-main` | `CATALOG.md`, `README.md`, `skills/`, `plugins/`, `tools/`, `docs_zh-CN/` | Estrutura grande e orientada a instaladores/plugins. |
| `CATALOG.md` externo | 1.508 skills em categorias como architecture, development, security, testing e workflow | Bom para descoberta; ruim para copia direta. |
| `Utils/1250 Skills` | `skills_index_lite.txt`, `skills_index.json`, `catalog.json`, bundles | Dump amplo, com muitos itens especificos ou genericos. |
| `modelos/skills/` | 54 skills locais | Mais restritas e alinhadas aos agentes atuais. |

## 3. Itens que fazem sentido incorporar

| Item | Tipo | Origem | Compatibilidade | Acao recomendada | Destino sugerido | Observacao |
|:---|:---|:---|:---|:---|:---|:---|
| `agents-md` | Skill | AAS | Media | Copiar com adaptacao | `modelos/skills/agent-instructions-review.md` | Aproveitar criterio de AGENTS.md curto; adaptar para PT-BR e nossa governanca. |
| `architecture-decision-records` | Skill | AAS | Media | Fundir com item existente | `modelos/skills/documentation-consistency-review.md` ou nova `adr-governance.md` | Util para ADR, mas nao copiar exemplos longos. |
| `api-documentation` | Workflow/skill | AAS | Media | Usar como referencia | `modelos/skills/` se houver demanda de API docs | Nosso `agente-api-contratos` ja cobre parte do escopo. |
| `app-store-optimization` | Skill | AAS | Baixa-media | Fundir parcialmente | `modelos/skills/store-listing-optimization.md` | Aproveitar apenas checklist de ASO; evitar pacote completo Apple/Google. |
| `android_ui_verification` | Skill | AAS | Media | Copiar com adaptacao futura | `modelos/skills/android-ui-verification.md` | Util se houver rotina ADB; hoje fica como candidata, nao instalar agora. |
| `powershell-windows` | Skill | AAS | Media | Usar como referencia | Documentacao operacional | Pode reforcar regras de terminal Windows sem virar skill agora. |

## 4. Itens apenas como referencia

| Item | Tipo | Motivo |
|:---|:---|:---|
| `flutter-expert` | Skill ampla | Nosso ecossistema ja divide Flutter em revisao, UI/UX, estado, performance e SQLite. |
| `multi-agent-patterns` | Skill ampla | Sobrepoe o SDD e o orquestrador; risco de conflito de autoridade. |
| `agent-orchestration-*` | Skills de meta-orquestracao | Podem contradizer guardiao e orquestrador local. |
| `documentation`, `docs-architect`, `documentation-templates` | Skills/docs | Sobrepoem `documentacao-requisitos` e `validador-documentacao`. |
| Bundles especializados | Bundle | Podem instalar demais; usar apenas para descoberta de candidatos. |

## 5. Itens redundantes ou descartaveis

| Item | Tipo | Acao | Motivo |
|:---|:---|:---|:---|
| Skills genericas de `security` | Skill | Rejeitar copia direta | Ja temos `security-mobile-review`; externas sao amplas demais. |
| Skills de marketing/SEO em massa | Skill | Rejeitar agora | Nosso foco atual e governanca de agentes, nao growth stack. |
| Skills cloud especificas Azure/AWS | Skill | Rejeitar agora | Sem evidencia de necessidade no repositorio atual. |
| Skills com automacao de terceiros | Skill | Rejeitar agora | Dependem de MCP/API/credenciais e aumentam risco operacional. |
| Conteudos em idioma ou dominio alheio | Skill/prompt | Referencia ou rejeicao | Exigem adaptacao alta e baixo retorno imediato. |

## 6. Copia direta

Nenhum item deve ser copiado diretamente neste momento.

Motivo: todos os candidatos relevantes precisam de adaptacao para:

- PT-BR tecnico;
- separacao `modelos/` versus `governance/`;
- autoridade exclusiva do guardiao;
- formato local de skill;
- vinculo com agentes existentes.

## 7. Precisa de adaptacao

| Item | Adaptacao minima |
|:---|:---|
| `agents-md` | Remover regras de Claude/AGENTS genericas, alinhar com Codex/OpenCode/Antigravity e governanca local. |
| `architecture-decision-records` | Reduzir exemplos, transformar em checklist ADR integrado a `agente-arquitetura`. |
| `android_ui_verification` | Adaptar de React Native para Android/Flutter e regras de terminal controlado. |
| `app-store-optimization` | Extrair apenas Google Play/ASO compativel com `google-play-support`. |

## 8. Rejeitar

| Grupo | Motivo |
|:---|:---|
| Instalacao completa da AAS | Importacao em massa, duplicidade e perda de controle. |
| `Utils/1250 Skills` como base operacional | Dump heterogeneo, sem curadoria suficiente. |
| Skills de ataque ofensivo sem escopo autorizado | Alto risco e baixa necessidade atual. |
| Skills que exigem credenciais de plataformas externas | Dependencia operacional e risco de seguranca. |

## 9. Proposta de destino

| Caso | Destino |
|:---|:---|
| Referencia de auditoria | `Utils/` local, fora do Git |
| Skill adaptada e reutilizavel | `modelos/skills/` |
| Prompt adaptado e reutilizavel | `modelos/prompts/` |
| Agente novo reutilizavel | `modelos/agentes/` somente via guardiao |
| Copia operacional de projeto | `governance/skills/`, `governance/prompts/`, `governance/agents/` |
| Relatorio de avaliacao | `modelos/` ou documentacao operacional, conforme escopo |

## 10. Riscos de governanca e redundancia

| Risco | Impacto | Mitigacao |
|:---|:---|:---|
| Importar skills em massa | Polui catalogo e enfraquece selecao inteligente | Incorporar no maximo por lote pequeno e justificado. |
| Duplicar escopo local | Agentes ficam inconsistentes | Fundir com skill existente sempre que possivel. |
| Trazer meta-orquestradores externos | Conflito com guardiao e orquestrador | Usar apenas como referencia. |
| Misturar referencia com incorporacao real | Dificulta manutencao | Marcar origem e destino de cada item. |
| Versionar `Utils/` | Repo cresce e inclui dumps externos | Manter `Utils/` no `.gitignore`. |

## 11. `.gitignore`

`Utils/` deve ficar no `.gitignore`.

Justificativa:

- contem bibliotecas externas;
- contem dumps e instaladores;
- contem assets, scripts, testes e dados que nao sao nossa fonte normativa;
- deve servir como referencia local de auditoria, nao como parte do repositorio principal.

## 12. Proximos passos

1. Nao incorporar nada automaticamente agora.
2. Se houver demanda real, criar primeiro uma skill adaptada por vez.
3. Prioridade de candidatos: `agents-md`, `architecture-decision-records`, `android_ui_verification`.
4. Atualizar `modelos/skills/README.md` somente quando uma skill for realmente incorporada.
5. Manter `Utils/` fora do versionamento.
