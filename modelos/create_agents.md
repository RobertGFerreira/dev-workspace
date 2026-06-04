# create_agents.md - Procedimento de Criacao e Instalacao Seletiva

## Objetivo

Este arquivo define o procedimento operacional para criar, copiar, adaptar e instalar agentes, prompts e skills do ecossistema de IA em um projeto.

O procedimento deve ser simples agora e preparado para selecao inteligente futura.

Regra central:

1. Entender o pedido e o repositorio.
2. Selecionar o minimo util.
3. Instalar somente o que foi justificado.

---

## Escopo

Este procedimento cobre:

- Criacao basica de agentes.
- Criacao basica de prompts.
- Criacao basica de skills.
- Copia seletiva de modelos para `governance/`.
- Instalacao minima padrao.
- Especializacao progressiva por contexto.
- Validacao minima apos instalacao.
- Registro do que foi instalado e do que foi descartado.

Este procedimento nao cobre:

- Edicao direta de governanca estrutural sem guardiao.
- Copia indiscriminada de todos os modelos.
- Instalacao de agentes de dominio sem evidencia.
- Uso de dados privados em `modelos/`.
- Publicacao externa, deploy ou alteracao de codigo de produto sem pedido explicito.

---

## Estrutura Oficial

| Caminho | Papel | Conteudo esperado |
|:---|:---|:---|
| `modelos/agentes/` | Biblioteca mestre de agentes | Agentes reutilizaveis e templates |
| `modelos/prompts/` | Biblioteca mestre de prompts | Prompts reutilizaveis e templates |
| `modelos/skills/` | Biblioteca mestre de skills | Skills reutilizaveis e templates |
| `governance/agents/` | Agentes operacionais do projeto | Copias selecionadas/adaptadas |
| `governance/prompts/` | Prompts operacionais do projeto | Copias selecionadas/adaptadas, se aplicavel |
| `governance/skills/` | Skills operacionais do projeto | Copias selecionadas/adaptadas, se aplicavel |
| `governance/plans/` | Planos de demandas complexas | `YYYYMMDD-slug.plan.md` |
| `governance/tasks/` | Tarefas de demandas complexas | `YYYYMMDD-slug.tasks.md` |
| `modelos/agentes/SDD_ECOSSISTEMA_AGENTES.md` | SDD master | Arquitetura normativa do ecossistema |
| `governance/plans/YYYYMMDD-slug.sdd.md` | SDD derivado | Especificacao limitada a um plano |

Regra: `modelos/` e biblioteca mestre; `governance/` e configuracao operacional do projeto.

### Configuracao explicita do projeto

Toda instalacao deve gerar ou atualizar uma configuracao operacional do projeto antes de copiar agentes, prompts ou skills.

Destino recomendado:

| Arquivo | Quando usar | Observacao |
|:---|:---|:---|
| `governance/project.env` | Projeto com governanca versionada | Preferido para registrar selecao de agentes. |
| `.env` | Projeto que ja usa `.env` operacional | Evitar segredos; registrar somente flags de governanca. |
| `governance/project-config.md` | Quando o usuario quiser documento legivel em vez de variaveis | Pode complementar o `.env`. |

Variaveis minimas:

| Variavel | Valores esperados | Finalidade |
|:---|:---|:---|
| `PROJECT_TYPE` | `app`, `web`, `api`, `game`, `content`, `library`, `mixed` | Define dominio principal. |
| `PROJECT_STACK` | `flutter`, `android`, `godot`, `node`, `python`, `java`, `mixed`, `unknown` | Define stack dominante. |
| `PROJECT_LANGUAGE` | `dart`, `kotlin`, `gdscript`, `javascript`, `typescript`, `python`, `java`, `mixed`, `unknown` | Define linguagem dominante. |
| `PROJECT_TARGET_PLATFORM` | `android`, `ios`, `web`, `desktop`, `backend`, `console`, `mixed` | Define plataforma alvo. |
| `ENABLE_GOOGLE_PLAY_AGENT` | `true` / `false` | Ativa suporte Google Play quando fizer sentido. |
| `ENABLE_GODOT_AGENT` | `true` / `false` | Ativa linha tecnica Godot/GDScript quando o projeto for game Godot. |
| `ENABLE_SCRAPING_AGENT` | `true` / `false` | Ativa coleta publica limitada e documentada. |
| `ENABLE_SECURITY_AGENTS` | `true` / `false` | Ativa linha de seguranca transversal. |
| `ENABLE_LGPD_AGENT` | `true` / `false` | Ativa privacidade/LGPD quando houver dados pessoais. |

Regra: flags opcionais com valor `false` nao instalam agente, prompt ou skill relacionados.

### Fontes externas e `Utils/`

Pastas como `Utils/antigravity-awesome-skills-main` e `Utils/1250 Skills` sao referencias locais de auditoria. Elas podem ser lidas para comparacao, mas nao devem ser copiadas em massa, tratadas como fonte normativa ou versionadas no repositorio principal.

Ao avaliar uma fonte externa:

1. Classificar cada item como referencia, adaptacao, fusao, copia ou rejeicao.
2. Preferir referencia quando houver sobreposicao com skills locais.
3. Copiar apenas quando o item tiver escopo claro, ganho real e destino definido.
4. Adaptar antes de incorporar quando houver dependencia de ferramenta, idioma, formato ou governanca externa.
5. Manter `Utils/` no `.gitignore`.

---

## Fluxo Basico Obrigatorio

1. Receber pedido do usuario.
2. Ler arquivos citados explicitamente.
3. Detectar contexto minimo do projeto.
4. Classificar escopo.
5. Confirmar ou perguntar linguagem, stack, tipo de projeto e plataforma alvo quando a evidencia for insuficiente.
6. Gerar ou atualizar a configuracao explicita do projeto.
7. Selecionar conjunto minimo de agentes.
8. Selecionar prompts vinculados.
9. Selecionar skills vinculadas.
10. Copiar/instalar apenas o necessario.
11. Atualizar documentacao da estrutura.
12. Reportar instalado, nao instalado e motivo.

Nunca pule a etapa de leitura. Nunca instale antes de selecionar.

### Perguntas minimas ao usuario

Use perguntas somente quando a leitura do repositorio nao der evidencia suficiente.

| Pergunta | Quando perguntar | Variavel afetada |
|:---|:---|:---|
| Qual e o tipo principal do projeto? | Quando `PROJECT_TYPE` nao for claro | `PROJECT_TYPE` |
| Qual stack/linguagem deve guiar os agentes? | Quando houver stack mista ou ambigua | `PROJECT_STACK`, `PROJECT_LANGUAGE` |
| O alvo inclui Android/Google Play? | Quando houver Flutter/Android ou distribuicao mobile | `ENABLE_GOOGLE_PLAY_AGENT` |
| O jogo usa Godot/GDScript? | Quando `PROJECT_TYPE=game` | `ENABLE_GODOT_AGENT` |
| A tarefa exige coleta de dados publicos? | Quando houver pesquisa, benchmarking ou metadata publica | `ENABLE_SCRAPING_AGENT` |
| O projeto trata dados pessoais ou superficies sensiveis? | Quando houver usuarios, auth, pagamentos, API, DB ou app mobile | `ENABLE_SECURITY_AGENTS`, `ENABLE_LGPD_AGENT` |

---

## Ordem de Leitura

Leia primeiro os arquivos indicados pelo usuario.

Se precisar complementar, leia somente o necessario:

1. `README.md`
2. `AGENTS.md`
3. `CONTEXT.md`
4. Arquivos de stack:
   - `pubspec.yaml`
   - `package.json`
   - `pyproject.toml`
   - `build.gradle`
   - `app/build.gradle.kts`
   - `AndroidManifest.xml`
5. Inventarios:
   - `modelos/agentes/README.md`
   - `modelos/prompts/README.md`
   - `modelos/skills/README.md`
6. Estrutura existente:
   - `governance/agents/`
   - `governance/prompts/`
   - `governance/skills/`

Pare quando houver evidencias suficientes para selecionar.

---

## Classificacao do Pedido

| Classe | Quando usar | Resultado |
|:---|:---|:---|
| `LEITURA` | Usuario pede para ler/entender | Nao instalar |
| `REVISAO` | Usuario pede auditoria ou melhoria | Diagnosticar antes de alterar |
| `CRIACAO` | Falta agente, prompt ou skill | Criar modelo minimo necessario |
| `INSTALACAO` | Usuario pede configurar ou instalar | Copiar conjunto minimo para `governance/` |
| `DOCUMENTACAO` | Usuario pede guias, README ou estrutura | Atualizar docs operacionais |
| `GOVERNANCA` | Altera autoridade, agentes, prompts, skills ou permissoes | Exigir guardiao de agentes |

Se houver duvida, classifique como `REVISAO` e nao instale.

---

## Instalacao Minima Padrao

O conjunto minimo inicial e:

| Item | Motivo |
|:---|:---|
| `agente-base-universal` | Base comum de escopo, limites e heranca |
| `orquestrador-agentes` | Classifica, coordena e cria plan/tasks quando necessario |
| `documentacao-requisitos` | Mantem README, guias, SDD derivado e documentacao operacional |
| `spec-agent` | Mantem Spec Kit, SDD master/derivado e validacoes |
| `quality-gate` | Valida consistencia final |

Instale esses itens somente quando o pedido for de instalacao/configuracao de governanca. Para leitura ou revisao, apenas recomende.

---

## Especializacao Progressiva

Adicione especialistas somente com evidencia:

| Evidencia | Adicionar |
|:---|:---|
| Diff, bug, refatoracao, revisao de codigo | `revisor-codigo` |
| Arquitetura, fronteiras, ADRs | `agente-arquitetura` |
| Testes, cobertura, criterios de aceite | `agente-testes` |
| APIs, contratos, endpoints | `agente-api-contratos` |
| CI/CD, workflows, release | `agente-ci-cd` |
| Flutter/Dart | `flutter-revisor-codigo`, `flutter-ui-ux-pro`, `flutter-state-arch` conforme necessidade |
| Android, Play Console, AAB/APK | `google-play-support` |
| SQLite, offline, sincronizacao | `sync-data-guard` |
| Jogos | `criador-games` e apenas os especialistas necessarios |
| Conteudo editorial | `criador-conteudo` e apenas os especialistas necessarios |

Se dois agentes parecerem redundantes, selecione o mais abrangente ou redefina escopo antes de instalar.

### Agentes opcionais por stack, linguagem e dominio

| Item | Tipo | Condicao de criacao | Pergunta ao usuario | Variavel de configuracao | Destino | Observacao |
|:---|:---|:---|:---|:---|:---|:---|
| `google-play-support` | Agente opcional | Projeto Android, Flutter Android, AAB/APK, Play Console ou publicacao mobile | Deseja ativar suporte Google Play/Publicacao Android? | `ENABLE_GOOGLE_PLAY_AGENT=true` | `governance/agents/` | Subordinado a `documentacao-requisitos`; nao vira orquestrador. |
| Linha Godot/GDScript | Linha opcional de games | `PROJECT_TYPE=game` e stack Godot confirmada | O jogo usa Godot/GDScript e precisa de apoio tecnico do motor? | `ENABLE_GODOT_AGENT=true` | `governance/agents/` e `governance/skills/` | Usar `criador-games` como orquestrador; nao criar agente monolitico. |
| Raspagem/coleta publica | Agente opcional futuro | Pesquisa documental, benchmarking ou metadata publica permitida | A coleta sera apenas em fontes publicas e permitidas? | `ENABLE_SCRAPING_AGENT=true` | `governance/agents/` | Bloquear login, captcha, paywall, bypass e violacao de termos. |
| Seguranca transversal | Linha recomendada | App mobile, API, DB, auth, dados sensiveis, release ou compliance | O projeto exige revisao de seguranca tecnica? | `ENABLE_SECURITY_AGENTS=true` | `governance/agents/` | Pode usar `seguranca-conformidade` e especialistas tecnicos ja existentes. |
| Privacidade/LGPD | Linha recomendada | Dados pessoais de usuarios no Brasil ou risco regulatorio | O projeto trata dados pessoais sujeitos a LGPD? | `ENABLE_LGPD_AGENT=true` | `governance/agents/` | Pode reforcar `seguranca-conformidade`; nao criar duplicidade sem guardiao. |

### Regras para opcionais

- Google Play nunca e instalado como padrao universal.
- Godot nunca e instalado como padrao universal.
- Raspagem nunca e instalada sem limites legais e operacionais explicitos.
- Seguranca e LGPD devem ser avaliadas como linha transversal, nao como checklist superficial.
- Agente opcional sem evidencia deve ficar como `nao instalado` no relatorio final.
- Referencias externas em `triagem/` ou `Utils/` podem inspirar adaptacao, mas nao sao copia direta.

### Linha Godot sem agente monolitico

Quando `ENABLE_GODOT_AGENT=true`, a selecao deve preservar responsabilidades:

| Responsabilidade | Agente preferido | Observacao |
|:---|:---|:---|
| Orquestracao e GDD | `criador-games` | Coordena e consolida. |
| Estrutura, mecanicas e loop | `estrutura-games` | Nao assume narrativa nem HUD. |
| Historia, lore e dialogos | `narrativa-games` | Nao assume balanceamento. |
| HUD, UX e direcao criativa | `criativo-games` | Nao assume monetizacao. |
| Economia e retencao | `monetizacao-games` | Nao assume implementacao tecnica. |
| Motor Godot/GDScript | Especialista tecnico a criar somente via guardiao, se necessario | Pode derivar de `godot-gdscript-patterns` como modelo, nao copia direta. |

### Linha de seguranca e LGPD

`seguranca-conformidade` continua sendo a referencia principal. Se o projeto exigir mais profundidade, documentar subdivisao operacional antes de criar agentes:

| Subarea | Escopo | Quando ativar |
|:---|:---|:---|
| Seguranca mobile/app | Permissoes, armazenamento local, secrets, logs, auth, release | App mobile ou Android/iOS. |
| Seguranca backend/API/DB | Autenticacao, autorizacao, endpoints, banco, exposicao indevida | API, backend, banco ou integracoes. |
| Privacidade e LGPD | Dados pessoais, finalidade, consentimento, retencao, compartilhamento | Usuarios no Brasil ou dados pessoais. |

Nova subdivisao de agente so deve ocorrer se houver recorrencia, escopo duravel e validacao do guardiao.

---

## Selecao de Prompts

Para cada agente selecionado:

1. Procurar prompt correspondente em `modelos/prompts/<agente>.md`.
2. Copiar para `governance/prompts/` apenas se o projeto mantiver prompts operacionais.
3. Se nao houver prompt, criar somente quando o agente precisar de instrucao propria.
4. Nao criar prompt duplicado para skill ou regra que ja existe.

Regra: agente sem prompt pode existir apenas se a definicao do agente contiver instrucao operacional suficiente.

---

## Selecao de Skills

Para cada agente selecionado:

1. Ler skills declaradas no agente ou no README de agentes.
2. Copiar apenas skills usadas pelos agentes instalados.
3. Evitar skills genericas demais.
4. Renomear ou restringir skill se ela nao tiver dominio, entrada e saida claros.
5. Registrar skills nao instaladas e motivo.

Regra: nao instalar catalogo completo de skills por padrao.

---

## Quando Criar Novo Agente

Crie um novo agente somente se:

- Nao existir agente com escopo equivalente.
- A responsabilidade for duravel e reutilizavel.
- O agente tiver arquivos permitidos/proibidos claros.
- Houver prompt ou instrucao operacional suficiente.
- Houver ao menos uma skill relevante.
- O README de agentes puder ser atualizado pela autoridade correta.

Nao crie agente novo para uma tarefa pontual que pode ser resolvida por agente existente.

---

## Quando Criar Novo Prompt

Crie um prompt novo somente se:

- Um agente precisar de instrucao operacional especifica.
- O prompt nao duplicar o proprio agente.
- O prompt for reutilizavel.
- O nome seguir o agente ou a tarefa.

Destino mestre: `modelos/prompts/`.
Destino operacional: `governance/prompts/`, se houver copia de projeto.

---

## Quando Criar Nova Skill

Crie uma skill nova somente se:

- Ela representar capacidade modular reutilizavel.
- Tiver dominio, entrada, saida, limites e criterios claros.
- Nao duplicar skill existente.
- For vinculada a ao menos um agente.

Destino mestre: `modelos/skills/`.
Destino operacional: `governance/skills/`, se houver copia de projeto.

---

## Procedimento de Instalacao

### 1. Preparar selecao

Crie uma lista com:

- agentes obrigatorios;
- agentes opcionais;
- prompts vinculados;
- skills vinculadas;
- arquivos que serao copiados;
- arquivos que nao serao copiados.

### 2. Criar pastas

Criar apenas quando necessario:

- `governance/agents/`
- `governance/prompts/`
- `governance/skills/`
- `governance/plans/`
- `governance/tasks/`

### 3. Copiar modelos

Copiar somente itens selecionados:

```text
modelos/agentes/<nome>.md  -> governance/agents/<nome>.md
modelos/prompts/<nome>.md  -> governance/prompts/<nome>.md
modelos/skills/<nome>.md   -> governance/skills/<nome>.md
```

Se o destino ja existir:

1. Ler o arquivo existente.
2. Comparar escopo.
3. Preservar adaptacoes de projeto.
4. Atualizar somente o necessario.

### 4. Adaptar copias

Adaptar apenas a copia em `governance/`:

- nome do projeto;
- stack confirmada;
- dominio confirmado;
- caminhos reais;
- comandos reais;
- restricoes operacionais.

Nunca adaptar o modelo mestre em `modelos/` para um projeto especifico.

### 5. Documentar

Atualizar ou criar documentacao operacional com:

- estrutura instalada;
- agentes ativos;
- prompts ativos;
- skills ativas;
- itens opcionais nao instalados;
- pendencias;
- proximos passos.

---

## Validacao Minima

Antes de concluir:

- [ ] Todos os arquivos citados pelo usuario foram lidos ou marcados como ausentes.
- [ ] A demanda foi classificada.
- [ ] Linguagem, stack, tipo de projeto e plataforma alvo foram detectados ou perguntados.
- [ ] A configuracao explicita do projeto foi criada ou atualizada quando houve instalacao.
- [ ] Cada agente instalado tem motivo.
- [ ] Cada agente opcional ativado tem variavel, evidencia e pergunta registrada.
- [ ] Cada prompt instalado esta vinculado a agente ou tarefa.
- [ ] Cada skill instalada esta vinculada a agente.
- [ ] Nenhum especialista foi instalado sem evidencia.
- [ ] Google Play, Godot e raspagem nao foram instalados por padrao universal.
- [ ] Raspagem, se ativada, possui limites de compliance e fontes publicas permitidas.
- [ ] Seguranca/LGPD foi avaliada quando houver app, API, DB, auth ou dados pessoais.
- [ ] `modelos/` nao recebeu configuracao especifica de projeto.
- [ ] `governance/` concentra as copias operacionais.
- [ ] Plan e tasks, se criados, estao em `governance/plans/` e `governance/tasks/`.
- [ ] A documentacao registra o que ficou fora.

---

## Formato do Relatorio Final

Use este formato:

```markdown
1. Pedido classificado: [LEITURA|REVISAO|CRIACAO|INSTALACAO|DOCUMENTACAO|GOVERNANCA]
2. Arquivos lidos:
   - [caminho] - [CONFIRMADO|AUSENTE]
3. Contexto inferido:
   - stack:
   - dominio:
   - sinais:
4. Configuracao do projeto:
   - PROJECT_TYPE:
   - PROJECT_STACK:
   - PROJECT_LANGUAGE:
   - PROJECT_TARGET_PLATFORM:
   - ENABLE_GOOGLE_PLAY_AGENT:
   - ENABLE_GODOT_AGENT:
   - ENABLE_SCRAPING_AGENT:
   - ENABLE_SECURITY_AGENTS:
   - ENABLE_LGPD_AGENT:
5. Agentes selecionados:
   - obrigatorios:
   - opcionais:
6. Prompts selecionados:
7. Skills selecionadas:
8. Itens instalados:
9. Itens nao instalados:
10. Ajustes documentais:
11. Proximos passos:
```

Se nenhum item for instalado, declarar o motivo.

---

## Preparacao para Selecao Inteligente Futura

Este procedimento deve permitir evoluir para:

- score de relevancia por agente;
- selecao por stack;
- selecao por dominio;
- selecao por tarefa;
- instalacao incremental;
- poda de agentes sem uso;
- relatorio de cobertura de agentes, prompts e skills.

Campos futuros recomendados:

| Campo | Uso futuro |
|:---|:---|
| `stack_score` | Peso por stack detectada |
| `domain_score` | Peso por dominio detectado |
| `task_score` | Peso por tipo de demanda |
| `evidence` | Arquivos que justificam a instalacao |
| `confidence` | `alta`, `media`, `baixa` |
| `install_mode` | `recomendar`, `copiar`, `adaptar`, `criar` |

Enquanto o score nao existir, use decisao textual e conservadora.
