# AUDITORIA DE IA — Projeto: condominio-rural

Esta auditoria analisa a arquitetura de governança, o ecossistema de agentes, os prompts especializados e as habilidades de Inteligência Artificial implementadas na pasta de governança do projeto **Condomínio Rural**.

---

## Agentes

### 1. Quais agentes estão definidos?
O projeto conta com um ecossistema completo de **16 agentes** definidos na governança (`governance/agents/`), operando sob um modelo de cooperação técnica:

| Nome do Agente | Ferramenta / Plataforma | Função Principal |
| :--- | :--- | :--- |
| **orquestrador-agentes** | Codex/Antigravity | Ponto de entrada. Triagem de complexidade (Simples vs Complexa) e direcionamento dos pipelines de agentes por subtipo de demanda. |
| **spec-agent** | Codex/Antigravity | Tradução de demandas complexas em especificações funcionais e planos técnicos estruturados (`spec.md`, `boundaries.md`, `tasks.md`). |
| **revisor-codigo** | Codex/Antigravity | Auditor sênior de Dart/Flutter. Revisa vazamentos de memória (dispose), null safety, performance e lógica de negócio. |
| **flutter-ui-ux-pro** | Codex/Antigravity | Especialista em design de interface operacional, responsividade, feedback de carregamento, estados de erro/vazio e temas coerentes. |
| **guardiao-fluxo** | Codex/Antigravity | Defensor e auditor de estabilidade de fluxos críticos (autenticação, sincronização, fotos, banco de dados local). Possui poder de **veto**. |
| **sync-data-guard** | Codex/Antigravity | Especialista em offline-first, garantia de idempotência no envio de dados e tratamento de filas de sincronização de rede. |
| **flutter-state-arch** | Codex/Antigravity | Auditor de gerenciamento de estado e acoplamento, checando ciclo de vida de views, controllers e rebuilds excessivos. |
| **quality-gate** | Codex/Antigravity | Portaria de conformidade transversal pré-commit (warnings, imports, print(), camelCase, specs correspondentes). |
| **commit-guardian** | Codex/Antigravity | Guardião de segurança final (proíbe chaves/segredos hardcoded, CPFs em logs) e validador de Conventional Commits. |
| **agente-configuracao-governanca**| Codex/Antigravity | Único agente habilitado a analisar e propor alterações nos arquivos estruturais e regras de governança de IA. |
| **documentacao-requisitos** | Codex/Antigravity | Responsável por garantir consistência total entre o código implementado e os artefatos de documentação (`.md`, `README`, `features.md`). |
| **repo-map-analyst** | Codex/Antigravity | Mapeia o repositório físico e auxilia na compreensão de arquivos novos e existentes. |
| **ideias-exploracao** | Codex/Antigravity | Atua no brainstorming e refinamento conceitual inicial de novas ideias e fluxos de telas. |
| **bootstrap-governanca** | Codex/Antigravity | Agente utilitário para provisionamento inicial e inicialização de regras do ecossistema. |

### 2. O agente tem contexto claro?
**Sim.** A clareza contextual é o maior trunfo desta configuração. 
- O **orquestrador** conhece as diferenças fundamentais dos dois aplicativos móveis principais (`app_v3` como cliente offline-first principal, `trabalhadores_v2` como online-first para trabalhadores).
- Ele estabelece regras e fronteiras rígidas ao lidar com o projeto `app_v3` (regras específicas de splash, logo, e o uso de `app_farol` estritamente como *referência estrutural*, proibindo a cópia de identidade visual/funcional).

### 3. O escopo está bem delimitado?
**Sim, extremamente bem delimitado.** A governança utiliza uma barreira de classificação na Etapa 0 do Orquestrador. 
- Se a solicitação for **SIMPLES** (ajustes pontuais), ela é resolvida sem o acionamento burocrático de agentes.
- Se for **COMPLEXA**, o pipeline é acionado e exige a geração detalhada de artefatos estruturados em caminhos obrigatórios (como `Documentação/[projeto]/plans/` e `tasks/`), impedindo desvios operacionais.

---

## Prompts

### 1. Prompts Encontrados
Os prompts dos agentes estão consolidados no arquivo central de documentação [prompts-especializados-agentes.md](file:///c:/Users/Robert/Documents/GitHub/condominio-rural/Documenta%C3%A7%C3%A3o/Agentes/prompts-especializados-agentes.md). Ele define a mentalidade corporativa sênior aplicável a todos os assistentes e os prompts individuais de cada agente do ecossistema.

### 2. Avaliação Técnica dos Prompts
- **Mentalidade Universal e Invariantes Inegociáveis:** (Nota: **5/5**). O bloco obrigatório em todos os prompts exige prevenção de erros clássicos do Flutter e impõe barreiras determinísticas (ex: proibição absoluta de `print()` em produção, uso exclusivo de `Color.withValues()` em vez de `withOpacity`, novos arquivos em `snake_case`).
- **Prompt do `orquestrador-agentes`:** (Nota: **5/5**). Clareza impecável ao definir fases, tabelas de subtipos de demandas complexas e os pipelines de acionamento específicos para cada tipo de tarefa.
- **Prompt do `spec-agent`:** (Nota: **4.5/5**). Estrutura perfeitamente os artefatos de entrega para modo análise vs modo feature.
- **Prompt do `revisor-codigo`:** (Nota: **4.5/5**). Altamente específico e acionável. A definição das severidades de issue (`CRÍTICO`, `ALTO`, `MÉDIO`, `BAIXO`) garante relatórios de revisão homogêneos e legíveis.
- **Reutilizabilidade Geral:** (Nota: **3/5**). Baixa a moderada, pois os prompts são extremamente específicos e direcionados às particularidades do repositório agrícola do Condomínio Rural. No entanto, sua *arquitetura estrutural* é altamente reaproveitável.

### 3. Qual o melhor prompt e por quê?
O prompt do **`orquestrador-agentes`** é o mais robusto e eficaz. Ele previne o desperdício de tokens de contexto em tarefas fáceis ao criar o bypass de demandas simples e, simultaneamente, impõe um fluxo de integridade sistêmica inabalável em tarefas complexas. O orquestrador também impede que o assistente de IA sofra de complacência (uma alucinação clássica em IA generativa), forçando-o a analisar edge cases, prever regressões e riscos no SQLite e offline-first antes de sugerir soluções.

---

## Skills

### 1. Skills Encontradas
Identificamos **19 habilidades (.md)** salvas centralizadamente na pasta `governance/skills/`. Elas cobrem todas as regras técnicas de desenvolvimento móvel offline-first:
- `anti-ai-generic-ui`
- `ui-ux-pro-review`
- `security-mobile-review`
- `flutter-performance-guard`
- `offline-sync-review`
- `sqlite-integrity-review`
- `navigation-flow-review`
- `forms-validation-review`
- `documentation-consistency-review`
- `condominio-domain-knowledge`
- `trabalhadores-domain-knowledge`
- (Demais habilidades de suporte e análise estática do Flutter)

### 2. Nível de Detalhamento
**Altíssimo.** As skills não são declarações conceituais abstratas; elas contêm diretrizes operacionais binárias. 
- Por exemplo, a skill `sqlite-integrity-review` exige expressamente migrações versionadas, queries parametrizadas e tratamento de falhas em bases de dados locais específicas (`sao_jose.db` e `vargem.db`).
- A skill `ui-ux-pro-review` impõe a obrigatoriedade de alvos de toque maiores de 48dp no Android e estados visuais obrigatórios (loading, empty, erro) para qualquer listagem.

### 3. Habilidades reutilizáveis em outros projetos
A skill **`anti-ai-generic-ui`** é uma obra-prima de governança e é **100% reutilizável** em qualquer projeto corporativo moderno. Ela atua como um guardião técnico para impedir que o assistente gere interfaces poluídas com cards excessivos e dashboards repletos de métricas fantasiosas/clichês de IA (como "Insights", "AI Summary"), priorizando telas densas de informação focadas na rotina de uso real em campo pelo trabalhador agrícola.
A skill **`sqlite-integrity-review`** e **`offline-sync-review`** também são amplamente reutilizáveis em projetos offline-first móveis que usem bancos SQL.

---

## Diagnóstico Final

### Pontos Fortes
- **Invariantes Inegociáveis Rígidas:** A blindagem técnica com exigência de `flutter analyze` limpo, proibição de `print()` e uso de Conventional Commits força uma engenharia extremamente disciplinada.
- **Combate de Alucinação Visual:** A skill `anti-ai-generic-ui` protege o produto de se tornar um portfólio de designs bonitos mas inúteis, mantendo a interface orientada a tarefas práticas de campo.
- **Controle Total de Risco de Build/Layout:** A inclusão compulsória de campos como "Causa raiz", "Nível do problema" e "Chance de quebrar" em todas as tarefas do `tasks.md` impede que alterações perigosas em Gradle, assinaturas de apps ou dependências sejam feitas sem aviso prévio.

### Gaps e o que está faltando
1. **Placeholder Pendente nos Prompts:** O prompt do `orquestrador-agentes` e `flutter-state-arch` contêm a instrução `[confirmar gerenciamento de estado via pubspec.yaml]`, indicando que a IA ainda opera com uma pequena incerteza sobre a biblioteca exata de estado utilizada.
2. **Dependência de Execução Manual:** O `quality-gate` e o `commit-guardian` são excelentes validações, mas dependem de o desenvolvedor ou a própria IA checar os checklists. Não há um hook físico integrado de pré-commit para validar segredos de forma automatizada no Git local.

### Recomendações de Melhoria
1. **Sanear Placeholders:** Atualizar o arquivo `prompts-especializados-agentes.md` para fixar a biblioteca de estado identificada no `pubspec.yaml` (GetX/Provider) e remover as pendências de confirmação estrutural.
2. **Automatizar com Git Hooks:** Criar scripts físicos em `.git/hooks/pre-commit` baseados nas regras do `commit-guardian` para bloquear pushes contendo segredos expostos de forma automatizada antes mesmo de o código alcançar o repositório remoto.
3. **Validar com Testes Físicos:** Criar cenários de testes locais para testar a aderência das IAs aos checklists de governança para validar sua resiliência a alucinações.
