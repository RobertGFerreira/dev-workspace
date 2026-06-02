# Relatorio de Analise

Data: 2026-05-29

## Resumo

- Total de projetos analisados: 19
- Total de arquivos Markdown encontrados: 443
- Total de arquivos gerados por projeto: 114
- Templates universais gerados: 6
- Arquivos centrais gerados/atualizados: `project.config.json`, `AGENT_PROMPT.md`, `_PADRAO_UNIVERSAL/RELATORIO_ANALISE.md`

## Projetos com documentacao forte

- `Farol`
- `Projeto_rual_web`
- `Server_Oracle`

## Projetos com documentacao media

- `condominio-rural`
- `DevTrace`
- `My_IA_v2`
- `organizador_de_aquivos`
- `Projeto_rural_python`
- `Transcricao`

## Projetos com documentacao fraca

- `AI_Studio_v2_web`
- `IPMYTV`
- `MapMyRepo`
- `My_IA`
- `PixelStory`
- `robertgferreira`
- `Sistema-agricola`
- `SmartCopilot-Showcase`
- `smartcopilot-site`
- `Studio-IA`

## Lacunas recorrentes

- `AI_Studio_v2_web`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `condominio-rural`: faltam ROADMAP.md, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md
- `DevTrace`: faltam CHANGELOG.md, CONTRIBUTING.md
- `Farol`: faltam CHANGELOG.md, ARCHITECTURE.md
- `IPMYTV`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `MapMyRepo`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `My_IA`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `My_IA_v2`: faltam CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `organizador_de_aquivos`: faltam CHANGELOG.md, CONTRIBUTING.md, SECURITY.md
- `PixelStory`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `Projeto_rual_web`: faltam ARCHITECTURE.md, CONTRIBUTING.md
- `Projeto_rural_python`: faltam CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md
- `robertgferreira`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `Server_Oracle`: faltam CHANGELOG.md, ARCHITECTURE.md
- `Sistema-agricola`: faltam README.md, ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `SmartCopilot-Showcase`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `smartcopilot-site`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `Studio-IA`: faltam ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md
- `Transcricao`: faltam ARCHITECTURE.md, CONTRIBUTING.md

## Melhorias recomendadas

- Validar manualmente os comandos de instalacao, execucao, lint e testes antes de publicar.
- Substituir placeholders apenas por informacoes publicas e confirmadas.
- Criar ADRs especificos para projetos com arquitetura critica.
- Padronizar `SECURITY.md` e `CONTRIBUTING.md` nos projetos que ainda nao possuem esses arquivos.
- Adicionar `.env.example` seguro quando houver variaveis obrigatorias.

## Historico git: versoes antigas possivelmente melhores

- `Transcricao`: ROADMAP.md: versao anterior parece mais completa por heuristica de tamanho/estrutura; revisar commit 43fe47d.

## Privacidade e seguranca

- URLs remotas foram sanitizadas para remover credenciais embutidas.
- Caminhos locais absolutos foram substituidos por placeholders.
- Emails, telefones e tokens detectaveis foram substituidos por placeholders.
- Pastas de vault, logs, screenshots, ambientes virtuais e artefatos de build foram ignoradas por padrao.
- A documentacao gerada deve passar por revisao humana antes de ser copiada para repositorios publicos.

## Inventario por projeto

| Projeto | Markdown | Qualidade | Stack inferida | Faltando |
|:---|---:|:---:|:---|:---|
| `AI_Studio_v2_web` | 2 | fraca | Flutter, Dart | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `condominio-rural` | 21 | media | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md |
| `DevTrace` | 11 | media | {{STACK_TECNOLOGICA}} | CHANGELOG.md, CONTRIBUTING.md |
| `Farol` | 118 | forte | {{STACK_TECNOLOGICA}} | CHANGELOG.md, ARCHITECTURE.md |
| `IPMYTV` | 1 | fraca | Flutter, Dart | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `MapMyRepo` | 2 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `My_IA` | 6 | fraca | Python | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `My_IA_v2` | 28 | media | {{STACK_TECNOLOGICA}} | CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `organizador_de_aquivos` | 10 | media | Python | CHANGELOG.md, CONTRIBUTING.md, SECURITY.md |
| `PixelStory` | 9 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `Projeto_rual_web` | 84 | forte | Flutter, Dart | ARCHITECTURE.md, CONTRIBUTING.md |
| `Projeto_rural_python` | 79 | media | Python, FastAPI | CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md |
| `robertgferreira` | 1 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `Server_Oracle` | 54 | forte | {{STACK_TECNOLOGICA}} | CHANGELOG.md, ARCHITECTURE.md |
| `Sistema-agricola` | 0 | fraca | {{STACK_TECNOLOGICA}} | README.md, ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `SmartCopilot-Showcase` | 4 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `smartcopilot-site` | 1 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `Studio-IA` | 1 | fraca | {{STACK_TECNOLOGICA}} | ROADMAP.md, CHANGELOG.md, ARCHITECTURE.md, CONTRIBUTING.md, SECURITY.md |
| `Transcricao` | 11 | media | {{STACK_TECNOLOGICA}} | ARCHITECTURE.md, CONTRIBUTING.md |
