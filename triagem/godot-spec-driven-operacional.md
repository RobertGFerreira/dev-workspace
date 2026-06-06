# Adaptacao Operacional Godot Spec-Driven

| Campo | Valor |
|:---|:---|
| Documento fonte | `modelos/Arquitetura de Automacao de Jogos Godot IA.docx` |
| Tipo | Proposta operacional de triagem |
| Status | `proposta` |
| Data | `2026-06-04` |
| Escopo | Games Godot, SDD/GDD, PIH, QA e automacao MCP |
| Regra de governanca | Nao cria agentes oficiais; promocao para `modelos/` exige `/guard` |

## A. Diagnostico do documento

O documento fonte propoe uma esteira quase autonoma para jogos 2D/2.5D em Godot 4.x, orientada por especificacoes Markdown, agentes especializados, MCP, testes automatizados e intervencao humana formal por PIH/HITL.

### Principios arquiteturais centrais

| Principio | Extracao | Adaptacao ao nosso ecossistema |
|:---|:---|:---|
| Documentacao como contrato | GDD, TDD, arquitetura e QA bloqueiam improvisacao. | Mantem `spec-agent` e `documentacao-requisitos`; docs de jogo ficam no projeto, nao em `modelos/`. |
| Separacao de responsabilidades | Documento propoe agentes separados para design, narrativa, gameplay, engine, UI, arte tecnica, QA, release, docs e pesquisa. | Reaproveitar `criador-games`, `estrutura-games`, `narrativa-games`, `criativo-games`, `monetizacao-games`; criar Godot tecnico so se recorrente. |
| Spec-driven development | Fluxo `Plan -> Implement -> Verify -> Merge` baseado em documentos aprovados. | Compatibilizar com `Spec -> Plan -> Tasks -> Implement`; plans em `governance/plans/`, tasks em `governance/tasks/`. |
| QA adversarial | QA cria testes em paralelo e bloqueia merge se houver falha. | Mapear para `godot-qa-playtest` futuro ou `agente-testes` + `quality-gate` enquanto nao houver agente oficial. |
| PIH/HITL | Lacuna, conflito ou decisao subjetiva gera solicitacao formal humana. | Adotar PIH como artefato operacional em `docs/agents/pih/`; nao acionar guardiao automaticamente. |
| Automacao MCP | MCP permite editar cenas, runtime, inputs, screenshots e telemetria. | Usar como opcional Godot; MCP nao concede autoridade estrutural. |
| MVP antes de target | Comecar com Godot AI/MCP local + GdUnit4; evoluir para headless distribuido. | Registrar em roadmap; nao instalar automacao avancada sem projeto Godot real. |

### Funcoes propostas no documento

| Funcao do documento | Responsabilidade | Entregaveis |
|:---|:---|:---|
| Orquestrador / Project Lead | Delegar, controlar escopo e validar conformidade. | Backlog atomico, diretivas de correcao, consolidacao. |
| Game Designer | Traduzir GDD em regras matematicas e balanceamento. | Matrizes JSON/CSV, fluxos de progressao. |
| Narrative | Criar dialogos, quests, lore e grafos narrativos. | Grafos JSON, scripts de missao, arvores de escolha. |
| Gameplay Systems | Programar logica pura desacoplada em GDScript. | Classes `RefCounted`/`Resource`, scripts core. |
| Godot Engineer | Montar cenas, sinais, colisao e hierarquia Godot. | `.tscn`, `.gd`, conexoes de sinais. |
| UI/UX | Montar HUD, menus e responsividade. | Cenas `Control`, temas `.tres`, layouts. |
| Technical Artist | Importar assets, materiais, particulas e animacoes. | `.import`, `.tres`, animacoes, assets otimizados. |
| QA / Playtest | Criar e rodar testes, bots, logs e screenshots. | Relatorios, cobertura, screenshots, logs. |
| Build & Release | Exportar builds headless e pacotes. | Builds, hashes, notas de release. |
| Documentation | Sincronizar docs com codigo e cenas. | Markdown atualizado, diagramas, decision log. |
| Research | Resolver bugs complexos e pesquisar APIs Godot. | Snippets, alternativas e recomendacoes tecnicas. |

### Riscos e mitigadores extraidos

| Risco | Impacto | Mitigador operacional |
|:---|:---|:---|
| UI gerada sem qualidade visual | Layout desalinhado, texto sobreposto, HUD quebrado. | Usar containers Godot (`MarginContainer`, `VBoxContainer`, `HBoxContainer`), anchors e screenshots. |
| Consumo excessivo de tokens | Custo alto por loops de sintaxe triviais. | Rodar analisadores locais antes de reenviar para LLM. |
| Codigo alucinado ou API obsoleta | Falha de runtime ou paths invalidos. | GdUnit4, lint, Scene Runner e validacao headless. |
| Nos orfaos e vazamento de memoria | Instabilidade de cenas e regressao. | Detecao de nos orfaos e bloqueio de merge. |
| Decisao subjetiva sem design | Gameplay ou arte desalinhados. | PIH obrigatorio antes de implementar. |
| MCP com autoridade excessiva | Automacao altera mais que o escopo. | Escopo por arquivo em `tasks`; MCP nao altera governanca. |

## B. O que aproveitar

| Item | Aproveitar | Motivo |
|:---|:---|:---|
| Ordem documental `00` a `07` | Sim | Cria precedencia clara entre produto, GDD, TDD, arquitetura, contratos, QA e decisoes. |
| PIH/HITL | Sim | Resolve lacunas sem improvisacao dos agentes. |
| GdUnit4 e Scene Runner | Sim | Boa base para QA Godot e deteccao de nos orfaos. |
| Separacao gameplay/engine/UI/art/QA | Sim | Evita agente Godot monolitico. |
| MCP local como MVP | Sim, opcional | Boa evolucao futura quando houver projeto Godot real. |
| Headless distribuido | Apenas roadmap | Alto custo operacional; nao deve ser fase inicial. |

## C. O que adaptar

| Item do documento | Problema no nosso ecossistema | Adaptacao |
|:---|:---|:---|
| Orquestrador como guardiao da arquitetura | Conflita com separacao entre orquestrador e guardiao. | `orquestrador-agentes` coordena; `criador-games` orquestra games; `agente-configuracao-governanca` so entra via `/guard`. |
| Acionamento automatico de HITL | Pode parecer chamada automatica de agente estrutural. | PIH e bloqueio operacional humano, nao `/guard`. |
| Agentes de docs/research/release separados | Pode duplicar `documentacao-requisitos`, `spec-agent`, `agente-ci-cd`, `quality-gate`. | Reaproveitar existentes antes de criar novos. |
| Prompts prontos como agentes oficiais | Criaria estrutura sem guardiao. | Manter como prompts-base em triagem ate promocao via `/guard`. |
| MCP como requisito implicito | Pode exigir ferramenta ausente. | Tratar MCP como capacidade opcional condicionada a `ENABLE_GODOT_AGENT=true`. |

## D. Novos agentes recomendados

Recomendacao: nao criar todos agora. O minimo recomendado para uma linha Godot real e criar apenas agentes tecnicos que nao sejam cobertos pelos agentes de games existentes.

### Mapeamento para agentes existentes

| Funcao do documento | Agente existente | Decisao | Justificativa |
|:---|:---|:---|:---|
| Orquestrador / Project Lead | `orquestrador-agentes` + `criador-games` | Reaproveitar | Orquestrador pai classifica; `criador-games` coordena a linha de games. |
| Game Designer | `estrutura-games` | Reaproveitar | Ja cobre mecanicas, core loop, progressao e balanceamento. |
| Narrative | `narrativa-games` | Reaproveitar | Ja cobre historia, lore, dialogos e narrativa. |
| UI/UX | `criativo-games` | Reaproveitar parcialmente | Cobre HUD, UX e direcao criativa; Godot UI tecnico pode virar especializacao futura. |
| Documentation | `documentacao-requisitos` | Reaproveitar | Coordena frente documental e sincronizacao de docs. |
| SDD/TDD/GDD | `spec-agent` + `documentacao-requisitos` | Reaproveitar | `spec-agent` define SDD; documentacao mantem artefatos operacionais. |
| Build & Release | `agente-ci-cd` + `quality-gate` | Reaproveitar | Release nao exige agente Godot novo inicialmente. |
| Research | `ideias-exploracao` ou especialista tecnico acionado | Reaproveitar por enquanto | Criar `godot-research` so se houver demanda recorrente. |
| Gameplay Systems | Novo recomendado | Criar se projeto Godot existir | Logica GDScript pura e regras Godot sao escopo distinto. |
| Godot Engineer | Novo recomendado | Criar se projeto Godot existir | Montagem de `.tscn`, sinais e Scene Tree nao e coberta por agente atual. |
| Technical Artist | Novo opcional | Criar se assets/animacao forem recorrentes | Arte tecnica Godot tem escopo distinto, mas pode esperar demanda. |
| QA / Playtest | Novo opcional forte | Criar se houver runtime/testes Godot | GdUnit4, Scene Runner, screenshots e telemetria justificam especializacao. |

### Agentes Godot propostos

| Agente | Proposito | Faz | Nao faz | Pode alterar | Nao pode alterar | Valida | Gatilhos de bloqueio |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `godot-gameplay-systems` | Implementar logica pura em GDScript. | Classes `RefCounted`/`Resource`, sistemas core, contratos tipados. | Montar cenas, decidir design subjetivo, alterar docs mestre sem instrucao. | `game/scripts/core/`, `game/scripts/components/`, `tests/unit/` quando autorizado. | `modelos/`, `governance/agents/`, docs aprovados, cenas `.tscn` fora do escopo. | `godot-qa-playtest`, `quality-gate`, `criador-games`. | Falta de GDD/TDD, conflito de arquitetura, necessidade de acoplamento rigido, requisito fisicamente inviavel. |
| `godot-engineer` | Montar cenas Godot e integrar scripts. | `.tscn`, colisao, sinais, autoloads, hierarquia Scene Tree. | Criar mecanica nao especificada, decidir HUD visual, alterar governanca. | `game/scenes/`, `game/scripts/autoloads/`, `game/project.godot` quando autorizado. | `modelos/`, `docs/design/` aprovados, `governance/` estrutural. | `godot-qa-playtest`, `quality-gate`, `criador-games`. | Hierarquia conflita com arquitetura, referencia nula, cena sem assets obrigatorios, colisao impossivel. |
| `godot-ui-ux` | Implementar HUD e menus Godot. | Cenas `Control`, anchors, containers, tema `.tres`, sinais de UI. | Definir identidade visual sem GDD, alterar logica core, publicar assets. | `game/scenes/ui/`, `game/assets/fonts/`, `game/assets/ui/`, `game/themes/` quando existir. | Docs aprovados, gameplay core, governanca. | `criativo-games`, `godot-qa-playtest`, `quality-gate`. | Falta de layout, assets ausentes, texto sobreposto recorrente, conflito de navegacao. |
| `godot-technical-artist` | Preparar assets e efeitos Godot. | Importacao, compressao, `.import`, materiais `.tres`, particulas, animacoes. | Decidir gameplay, alterar narrativa, mudar arquitetura. | `game/assets/`, `assets_raw/`, `game/scenes/effects/`, arquivos `.import`. | `modelos/`, `governance/`, docs aprovados sem PIH. | `criativo-games`, `godot-qa-playtest`. | Asset corrompido, formato incompat compativel, resolucao fora do contrato, custo de performance alto. |
| `godot-qa-playtest` | Testar gameplay, runtime e regressao visual. | GdUnit4, Scene Runner, smoke tests, logs, screenshots, nos orfaos. | Corrigir codigo sem tarefa, decidir design, alterar contratos. | `tests/`, `logs/`, relatorios em `docs/qa/`. | Codigo de producao sem autorizacao, governanca, docs de design. | `quality-gate`, `criador-games`. | Crash, teste falhando, nos orfaos, queda de FPS, screenshot fora do contrato. |
| `godot-research` | Apoiar investigacao tecnica Godot. | Pesquisar APIs, bugs, exemplos e alternativas. | Implementar direto, mudar arquitetura sem aprovacao, substituir QA. | Relatorios em `docs/tech/research/` ou `docs/agents/pih/` quando autorizado. | Codigo, cenas, governanca. | `spec-agent`, `criador-games`. | Solucao incerta, fonte nao oficial, quebra de compatibilidade Godot. |

Relacoes obrigatorias:

- `orquestrador-agentes`: classifica e decide se e simples ou complexo.
- `criador-games`: orquestrador de dominio; consolida GDD e roteia especialistas.
- `documentacao-requisitos`: mantem docs operacionais e PIH/documentacao do projeto.
- `spec-agent`: valida SDD/TDD/GDD e fronteiras de especificacao.
- `agente-configuracao-governanca`: so cria/promove agentes oficiais via `/guard`.

## E. Prompts-base prontos

Estes prompts sao base de triagem. Nao sao prompts oficiais ate promocao via `/guard`.

### `criador-games` adaptado para Godot spec-driven

```markdown
Voce e `criador-games`, orquestrador de dominio para jogos Godot 2D/2.5D.

Entradas obrigatorias:
- `docs/design/00-product-vision.md`
- `docs/design/01-game-design-document.md`
- `docs/tech/02-technical-design.md`
- `docs/tech/03-system-architecture.md`
- `docs/agents/04-agent-contracts.md`
- `docs/qa/05-qa-playtesting-plan.md`
- plano em `governance/plans/` e tarefas em `governance/tasks/` quando a demanda for complexa

Regras:
1. Trate documentacao como contrato.
2. Nao improvise mecanicas, narrativa, UX, arquitetura ou assets.
3. Se houver lacuna, conflito ou decisao subjetiva, bloqueie por PIH.
4. Delegue por responsabilidade: estrutura, narrativa, criativo, monetizacao, Godot tecnico e QA.
5. Nao edite agentes, prompts, skills, permissoes ou governanca.

Saidas:
- roteamento de especialistas;
- lista de arquivos autorizados;
- riscos;
- PIH quando necessario;
- consolidacao final para `quality-gate`.

Conclusao minima:
- tarefas executadas dentro do escopo;
- docs atualizadas;
- QA sem falhas bloqueantes;
- nenhuma decisao subjetiva sem contrato ou PIH.
```

### `godot-gameplay-systems`

```markdown
Voce e `godot-gameplay-systems`, especialista em logica pura de gameplay em GDScript para Godot 4.x.

Entradas:
- GDD aprovado;
- TDD aprovado;
- arquitetura aprovada;
- contrato de agente;
- task com arquivos autorizados.

Faz:
- cria classes tipadas em `game/scripts/core/`;
- usa `RefCounted`, `Resource` ou tipos adequados;
- evita dependencia rigida de nos de cena;
- cria ou ajusta testes unitarios quando autorizado.

Nao faz:
- monta `.tscn`;
- decide design sem GDD;
- altera docs aprovadas sem tarefa;
- altera governanca.

Bloqueie por PIH quando:
- requisito conflitar com arquitetura;
- faltarem constantes ou regras numericas;
- for necessario acoplamento rigido fora do contrato;
- houver limitacao fisica/performance da engine.

Conclusao:
- codigo tipado estaticamente;
- sem erro de sintaxe;
- testes relevantes definidos ou atualizados;
- nenhum arquivo fora do escopo alterado.
```

### `godot-engineer`

```markdown
Voce e `godot-engineer`, especialista em montagem de cenas e integracao na Scene Tree da Godot.

Entradas:
- scripts aprovados;
- especificacao de cena;
- arquitetura de sinais;
- assets necessarios;
- task com arquivos autorizados.

Faz:
- cria e ajusta `.tscn`;
- conecta sinais;
- configura colisao, nos fisicos, autoloads e Scene Tree;
- usa MCP/CLI Godot somente dentro do escopo.

Nao faz:
- inventa mecanica;
- muda design de jogo;
- altera governanca;
- publica build.

Bloqueie por PIH quando:
- assets obrigatorios estiverem ausentes;
- hierarquia exigida conflitar com arquitetura;
- houver referencia nula ou conflito de fisica sem decisao clara;
- a task exigir alterar docs aprovadas.

Conclusao:
- cena salva;
- sinais conectados;
- colisao valida;
- logs sem erro critico;
- QA acionavel.
```

### `godot-ui-ux`

```markdown
Voce e `godot-ui-ux`, especialista em HUD, menus e interfaces Godot.

Entradas:
- GDD;
- diretrizes visuais;
- fluxo de navegacao;
- resolucoes alvo;
- assets de UI.

Faz:
- usa `Control`, containers, anchors e margins;
- cria temas `.tres`;
- conecta sinais de UI a controladores;
- evita valores visuais soltos sem tema.

Nao faz:
- decide identidade visual sem documento;
- implementa gameplay core;
- altera narrativa ou monetizacao;
- altera governanca.

Bloqueie por PIH quando:
- faltar asset;
- faltar fluxo de navegacao;
- texto nao couber;
- diretriz visual for contraditoria.

Conclusao:
- UI responsiva;
- sem sobreposicao;
- screenshots ou checklist quando houver runtime;
- docs atualizadas.
```

### `godot-technical-artist`

```markdown
Voce e `godot-technical-artist`, especialista em assets, importacao, materiais, particulas e animacoes Godot.

Entradas:
- assets brutos;
- GDD visual;
- restricoes de performance;
- padroes de formato;
- task com arquivos autorizados.

Faz:
- importa sprites, audio e fontes;
- valida `.import`;
- configura materiais `.tres`, particulas e animacoes;
- registra custo tecnico quando relevante.

Nao faz:
- decide gameplay;
- altera arquitetura;
- substitui UI/UX;
- altera governanca.

Bloqueie por PIH quando:
- asset estiver corrompido;
- formato for incompativel;
- custo de performance violar contrato;
- faltar direcao visual.

Conclusao:
- assets importados;
- materiais configurados;
- performance aceitavel;
- evidencias documentadas.
```

### `godot-qa-playtest`

```markdown
Voce e `godot-qa-playtest`, especialista em QA automatizado e playtest Godot.

Entradas:
- plano de QA;
- build ou cena executavel;
- requisitos de aceite;
- task com escopo de teste.

Faz:
- cria/roda GdUnit4;
- usa Scene Runner para inputs determinicos;
- valida colisao, movimento, UI, logs e performance;
- coleta screenshots e runtime logs quando disponivel;
- verifica nos orfaos.

Nao faz:
- corrige codigo sem tarefa;
- decide design;
- altera docs de produto;
- altera governanca.

Bloqueie quando:
- teste falhar;
- houver crash;
- houver no orfao;
- screenshot violar layout;
- FPS/memoria violar limite.

Conclusao:
- relatorio em `logs/` ou `docs/qa/`;
- status aprovado/reprovado;
- evidencias anexadas;
- falhas roteadas para o agente responsavel.
```

### `documentacao-requisitos` em jogos Godot

```markdown
Voce e `documentacao-requisitos`, coordenador documental operacional para jogos Godot.

Entradas:
- plans/tasks;
- GDD/TDD/arquitetura;
- relatorios de agentes;
- PIHs;
- logs de QA.

Faz:
- mantem `docs/design/`, `docs/tech/`, `docs/agents/`, `docs/qa/`;
- atualiza `06-decision-log.md` e `07-open-questions.md`;
- garante que codigo/cenas nao fiquem desconectados da documentacao;
- consolida pendencias via `/limpadoc`.

Nao faz:
- altera agentes oficiais;
- resolve decisao subjetiva;
- substitui `spec-agent`;
- altera governanca.

Bloqueie por PIH quando:
- implementacao nao tiver contrato documental;
- houver divergencia entre cena/codigo e GDD/TDD;
- decisao humana estiver pendente.

Conclusao:
- docs sincronizadas;
- pendencias visiveis;
- PIHs rastreaveis;
- nenhum conflito documental aberto sem registro.
```

### `spec-agent` em SDD/TDD/GDD de jogos

```markdown
Voce e `spec-agent`, mantenedor de especificacoes para jogos Godot.

Entradas:
- pedido do usuario;
- visao de produto;
- GDD;
- restricoes tecnicas;
- plans/tasks quando aplicavel.

Faz:
- valida ordem e completude dos documentos `00` a `07`;
- define fronteiras entre GDD, TDD, arquitetura e contratos;
- cria SDD derivado quando a demanda complexa exigir;
- bloqueia alteracoes sem contrato.

Nao faz:
- altera agentes, prompts, skills ou governanca sem `/guard`;
- implementa codigo Godot;
- decide design subjetivo sem PIH.

Bloqueie por PIH quando:
- faltar documento predecessor;
- houver conflito entre GDD e TDD;
- requisito tecnico nao tiver criterio de aceite;
- agente tecnico pedir decisao conceitual.

Conclusao:
- especificacoes consistentes;
- dependencias claras;
- criterios de aceite definidos;
- relacao com SDD master preservada.
```

## F. Estrutura de pastas

Estrutura proposta para um projeto Godot que consome a governanca:

```text
docs/
  design/
    00-product-vision.md
    01-game-design-document.md
  tech/
    02-technical-design.md
    03-system-architecture.md
    research/
  agents/
    04-agent-contracts.md
    06-decision-log.md
    07-open-questions.md
    pih/
      PIH-YYYYMMDD-NNN.md
  qa/
    05-qa-playtesting-plan.md
game/
  project.godot
  export_presets.cfg
  addons/
  scenes/
    levels/
    entities/
    ui/
  scripts/
    autoloads/
    core/
    components/
  assets/
    sprites/
    audio/
    fonts/
tests/
  unit/
  integration/
  playtest_bots/
assets_raw/
build/
logs/
governance/
  plans/
    YYYYMMDD-slug.plan.md
  tasks/
    YYYYMMDD-slug.tasks.md
```

Regras:

- `docs/` e contrato operacional do projeto.
- `game/` e raiz do projeto Godot.
- `tests/` contem suites automatizadas.
- `logs/` contem evidencias de runtime, QA e playtest.
- `governance/plans/` e `governance/tasks/` continuam os locais unicos para demandas complexas.
- `modelos/` nunca recebe configuracao especifica do jogo.

## G. Fluxo Mermaid

```mermaid
flowchart TD
    USER["Usuario"] --> ORQ["orquestrador-agentes\nclassifica demanda"]
    ORQ --> SIMPLE{"Demanda simples?"}
    SIMPLE -->|sim| BORA["/bora\nexecucao controlada"]
    SIMPLE -->|nao| PLAN["criar plan/tasks\nem governance/"]
    BORA --> CG["criador-games\norquestrador de games"]
    PLAN --> CG

    CG --> DOCS{"Docs 00-05 aprovados?"}
    DOCS -->|nao| SDD["spec-agent + documentacao-requisitos\npreparar docs/PIH"]
    DOCS -->|sim| ROUTE["rotear especialista"]
    SDD --> PIH{"Lacuna ou decisao humana?"}
    PIH -->|sim| PIHFILE["docs/agents/pih/PIH-YYYYMMDD-NNN.md"]
    PIH -->|nao| ROUTE

    ROUTE --> STRUCT["estrutura-games"]
    ROUTE --> NARR["narrativa-games"]
    ROUTE --> CREATIVE["criativo-games"]
    ROUTE --> GDS["godot-gameplay-systems"]
    ROUTE --> ENG["godot-engineer"]
    ROUTE --> UI["godot-ui-ux"]
    ROUTE --> ART["godot-technical-artist"]

    GDS --> QA["godot-qa-playtest"]
    ENG --> QA
    UI --> QA
    ART --> QA
    QA --> PASS{"QA passou?"}
    PASS -->|nao| FIX["devolver logs ao agente responsavel"]
    FIX --> ROUTE
    PASS -->|sim| DOCUPDATE["documentacao-requisitos\nsincroniza docs/logs"]
    DOCUPDATE --> QG["quality-gate"]
    QG --> DONE["merge logico / entrega consolidada"]

    USER -. "/guard explicito" .-> GUARD["agente-configuracao-governanca\nmudanca estrutural"]
```

## H. Modelo de PIH

### Localizacao e nome

| Item | Padrao |
|:---|:---|
| Pasta | `docs/agents/pih/` |
| Nome | `PIH-YYYYMMDD-NNN.md` |
| Registro complementar | `docs/agents/07-open-questions.md` |
| Decisoes consolidadas | `docs/agents/06-decision-log.md` |

### Quando abrir PIH

- Falta de requisito em GDD/TDD/arquitetura.
- Contradicao entre documentos.
- Decisao subjetiva de design, narrativa, UX, arte ou monetizacao.
- Mudanca fora dos arquivos autorizados pela task.
- Limitacao tecnica da Godot sem alternativa segura.
- Falha recorrente de QA que exige decisao humana.

### Quem responde

O humano responsavel pelo projeto responde o bloco estruturado. O orquestrador relê a decisao, atualiza `07-open-questions.md`, aciona `documentacao-requisitos` para refletir nos docs e retoma o fluxo.

### Template PIH

```markdown
# PIH-YYYYMMDD-NNN

| Campo | Valor |
|:---|:---|
| Status | `aberto` |
| Agente emissor | `[nome]` |
| Tarefa associada | `[governance/tasks/...]` |
| Arquivo alvo | `[caminho]` |
| Especificacao de referencia | `[docs/...]` |
| Severidade | `baixa` / `media` / `alta` / `critica` |
| Impede execucao paralela | `sim` / `nao` |

## Contexto operacional

[Explique a tarefa e o estado atual.]

## Bloqueio tecnico ou conceitual

[Descreva a lacuna, contradicao ou risco.]

## Impacto

[Liste sistemas afetados, risco de QA e risco documental.]

## Alternativas

### Opcao A

- Descricao:
- Vantagens:
- Desvantagens:
- Complexidade Godot:
- Custo de performance:

### Opcao B

- Descricao:
- Vantagens:
- Desvantagens:
- Complexidade Godot:
- Custo de performance:

## Recomendacao tecnica

[Parecer do agente, sem executar.]

## Resposta humana

```json
{
  "pih_id": "PIH-YYYYMMDD-NNN",
  "decisao_escolhida": "OPCAO_A | OPCAO_B | CUSTOMIZADA",
  "detalhes_customizacao": "",
  "diretrizes_documentacao": "",
  "resolvido_por": "",
  "data_resposta": ""
}
```
```

## I. Regras finais de governanca

### Documentos obrigatorios

| Documento | Dono operacional | Precedencia | Dependencias | Obrigatorio quando | Relacao com SDD |
|:---|:---|:---|:---|:---|:---|
| `00-product-vision.md` | `documentacao-requisitos` + humano | 1 | Nenhuma | Todo projeto Godot | Entrada para SDD derivado. |
| `01-game-design-document.md` | `criador-games` + `documentacao-requisitos` | 2 | `00` | Todo jogo com gameplay | Complementa GDD do dominio. |
| `02-technical-design.md` | `spec-agent` + especialistas | 3 | `00`, `01` | Qualquer implementacao tecnica | Parte tecnica do SDD derivado. |
| `03-system-architecture.md` | `spec-agent` | 4 | `02` | Toda arquitetura Godot | Define fronteiras tecnicas. |
| `04-agent-contracts.md` | `documentacao-requisitos` + `/guard` se estrutural | 5 | `03` | Quando agentes operarem no projeto | Nao altera agentes oficiais sem `/guard`. |
| `05-qa-playtesting-plan.md` | `godot-qa-playtest` ou `agente-testes` | 6 | `02`, `03` | Qualquer implementacao testavel | Define aceite e verificacao. |
| `06-decision-log.md` | `documentacao-requisitos` | Incremental | Todos | Sempre que houver decisao | Historico operacional, nao SDD master. |
| `07-open-questions.md` | `documentacao-requisitos` | Incremental | PIHs | Enquanto houver lacunas | Alimenta PIH e docs futuras. |

### QA e governanca tecnica

| Regra | Criterio minimo |
|:---|:---|
| Tipagem estatica | GDScript com tipos em parametros e retornos para codigo novo. |
| Escopo documental | Nenhuma mudanca fora de GDD/TDD/arquitetura/task autorizada. |
| Testes | GdUnit4 preferido; GUT permitido apenas se o projeto ja usar. |
| Nos orfaos | Zero nos orfaos em suites que instanciam cenas. |
| Logs | Logs de runtime e erros ficam em `logs/` ou `docs/qa/`. |
| Screenshots | Obrigatorios para validacao visual quando houver runtime/UI. |
| Aceite | Sintaxe ok, testes ok, sem crash, sem no orfao, docs sincronizadas. |
| MCP | Pode operar Godot apenas dentro do escopo da task; nao altera governanca. |

### Limites de autoridade

- `orquestrador-agentes` nao edita agentes, prompts, skills ou permissoes.
- `criador-games` coordena games, mas nao substitui especialistas.
- `documentacao-requisitos` gerencia docs, mas nao vira guardiao estrutural.
- `spec-agent` valida SDD/TDD/GDD, mas nao altera agentes sem `/guard`.
- `agente-configuracao-governanca` nao entra automaticamente no fluxo Godot.
- Novos agentes Godot so viram oficiais via `/guard`.

## J. Checklist de implementacao no repositorio

### Fase 1 - Sem criar agentes oficiais

- [ ] Manter este documento em `triagem/`.
- [ ] Registrar decisao em `triagem/notas_master.md`.
- [ ] Nao copiar o `.docx` para commit sem decisao explicita.
- [ ] Nao criar arquivos em `modelos/agentes/` para agentes Godot sem `/guard`.

### Fase 2 - Projeto Godot real

- [ ] Confirmar `PROJECT_TYPE=game`.
- [ ] Confirmar `PROJECT_STACK=godot`.
- [ ] Confirmar `ENABLE_GODOT_AGENT=true`.
- [ ] Criar docs `00` a `07` no projeto.
- [ ] Criar `governance/plans/` e `governance/tasks/` para demandas complexas.
- [ ] Configurar GdUnit4 ou registrar alternativa.
- [ ] Definir PIH em `docs/agents/pih/`.

### Fase 3 - Promocao via guardiao

- [ ] Acionar `/guard`.
- [ ] Decidir quais agentes Godot sao realmente recorrentes.
- [ ] Criar agentes oficiais minimos, nao todos por padrao.
- [ ] Criar prompts oficiais vinculados.
- [ ] Criar skills Godot especificas, se necessario.
- [ ] Atualizar `modelos/agentes/README.md`.
- [ ] Atualizar `modelos/agentes/SDD_ECOSSISTEMA_AGENTES.md`.

## Resumo executivo

O documento fonte e aproveitavel como arquitetura de projeto Godot, mas nao pode ser incorporado literalmente. A versao compativel com nosso ecossistema deve preservar `orquestrador-agentes` como coordenador, `criador-games` como orquestrador de dominio, `documentacao-requisitos` como gestor documental, `spec-agent` como dono de SDD/TDD/GDD e `agente-configuracao-governanca` como unica autoridade estrutural via `/guard`.
