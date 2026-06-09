# modelos/docs/

> Biblioteca de documentação-base do workspace — templates, guias e documentos de referência para estruturar e padronizar projetos.

---

## Finalidade da Pasta

A pasta `docs/` reúne os **documentos-base oficiais** do workspace. Seu propósito é garantir que cada novo projeto comece com uma fundação documental sólida, sem depender da memória ou improviso de quem está iniciando.

Os arquivos aqui presentes são de três naturezas diferentes:

| Natureza | Descrição |
|---|---|
| **Documentação de projeto** | Explica o projeto para colaboradores e usuários (README, CONTRIBUTING, CHANGELOG) |
| **Documentação técnica** | Descreve decisões de arquitetura e design de software (SDD, ARCHITECTURE) |
| **Documentação de governança** | Define regras, limites e responsabilidades (SECURITY, templates de agentes) |

---

## Categorias e Arquivos

### 📄 Documentação Geral de Projeto

| Arquivo | Tipo | Uso |
|---|---|---|
| `README.template.md` | Template | Documento de entrada de qualquer projeto — explica o que é, como instalar e como usar |
| `CHANGELOG.template.md` | Template | Registro cronológico de mudanças, versões e breaking changes |
| `CONTRIBUTING.template.md` | Template | Guia de contribuição — padrões de branch, commit, PR e code review |
| `ROADMAP.template.md` | Template | Planejamento de funcionalidades futuras por versão ou milestone |

### 🏗️ Documentação Técnica

| Arquivo | Tipo | Uso |
|---|---|---|
| `SDD_UNIVERSAL.template.md` | Template | Software Design Document — registro de decisões de design, arquitetura, componentes e integrações |
| `ARCHITECTURE.template.md` | Template | Visão geral da arquitetura — camadas, fluxos de dados, dependências externas |
| `GOOGLE_PLAY_DEPLOY.template.md` | Template | Guia universal de preparação e publicação de apps em lojas (Google Play) |

### 🔐 Documentação de Governança e Segurança

| Arquivo | Tipo | Uso |
|---|---|---|
| `SECURITY.template.md` | Template | Política de segurança — como reportar vulnerabilidades, versões suportadas |
| `AGENTE.template.md` | Template | Versão simplificada de definição de agente (pré-AGENTE_UNIVERSAL) |

### 📊 Documentação Analítica e Ferramentas

| Arquivo | Tipo | Uso |
|---|---|---|
| `RELATORIO_ANALISE.md` | Documento | Modelo de relatório de análise técnica — diagnóstico de estado atual de um projeto |
| `AGENT_PROMPT.md` | Documento | Referência de configuração de prompt de agente — padrão de instrução estruturada |
| `create_agents.md` | Script/Guia | Guia e automação para geração/registro de agentes no ecossistema |
| `dados.template.md` | Template | Definição e mapeamento de dicionários e fluxos de dados do projeto |

### ⚙️ Configurações e Modelos de Bootstrap IA

| Arquivo | Tipo | Uso |
|---|---|---|
| `antigravity.template.json` | Config | Template de configuração para o assistente Antigravity, vinculando agentes e regras |
| `opencode.template.json` | Config | Regras de ambiente, diretórios de agentes e permissões para o ecossistema OpenCode |
| `codex.template.md` | Template | Codex de contexto e invariantes técnicos de desenvolvimento de um projeto |

### 🗂️ Templates Universais

| Arquivo | Tipo | Uso |
|---|---|---|
| `DOCUMENTO_UNIVERSAL.template.md` | Template | Documento universal completo — cobre todas as seções possíveis de documentação de projeto |

---

## Como os Documentos se Relacionam

```
DOCUMENTO_UNIVERSAL   ←── Versão completa, cobre tudo
        │
        ├── README          → Entrada pública do projeto
        ├── ARCHITECTURE    → Complementa o README com detalhes técnicos
        ├── SDD             → Aprofunda decisões de design por componente
        ├── CONTRIBUTING    → Define como colaborar com o projeto
        ├── CHANGELOG       → Registra o histórico de mudanças
        ├── ROADMAP         → Documenta o futuro planejado
        └── SECURITY        → Define política de segurança e disclosure
```

> **Regra geral**: O `README.md` é sempre obrigatório. Os demais documentos são incrementais — adicionados conforme a maturidade e necessidade do projeto.

---

## Como Escolher o Documento Certo

| Situação | Documento recomendado |
|---|---|
| Novo projeto, documentação mínima | `README.template.md` |
| Projeto com múltiplos colaboradores | `README` + `CONTRIBUTING` + `CHANGELOG` |
| Projeto com decisões de arquitetura complexas | `ARCHITECTURE.template.md` + `SDD_UNIVERSAL.template.md` |
| Projeto público ou open-source | `README` + `CONTRIBUTING` + `SECURITY` + `CHANGELOG` |
| Projeto maduro com planejamento de longo prazo | Todos os templates acima + `ROADMAP.template.md` |
| Auditoria de estado atual | `RELATORIO_ANALISE.md` |
| Cobertura total desde o início | `DOCUMENTO_UNIVERSAL.template.md` |

---

## Diferença entre os Tipos de Documentação

### Documentação de Projeto
Voltada para **usuários e colaboradores externos**. Deve ser clara, acessível e atualizada a cada versão. Exemplos: `README`, `CONTRIBUTING`, `CHANGELOG`.

### Documentação Técnica
Voltada para **desenvolvedores ativos do projeto**. Detalha decisões de design, trade-offs, componentes e integrações. Exemplos: `SDD`, `ARCHITECTURE`.

### Documentação de Governança
Voltada para **definir regras e limites**. Não descreve o projeto — descreve as responsabilidades, políticas e padrões de conduta. Exemplos: `SECURITY`, `AGENTE.template`.

---

## Critérios de Padronização

Todo documento que entra em `docs/` deve:

- Ser **genérico** — sem referência a projetos específicos.
- Ter **seções claramente delimitadas** com títulos descritivos.
- Conter **instruções de preenchimento** embutidas (para templates).
- Ser **autossuficiente** — lido isoladamente, deve fazer sentido completo.
- Estar **em português** ou ter versão em português (idioma padrão do workspace).

---

## Observações de Uso

- Arquivos com sufixo `.template.md` são **bases para cópia** — copie para o projeto, adapte e remova as instruções após o preenchimento.
- Arquivos sem sufixo `.template.md` são **documentos de referência** — use como base de leitura ou como estrutura de análise, não como templates diretos.
- O `DOCUMENTO_UNIVERSAL.template.md` é o mais completo — use-o quando quiser cobrir todas as seções possíveis de uma vez, especialmente em projetos privados de alta maturidade.
- Nunca edite os originais desta pasta — copie e adapte no repositório de destino.

> Veja também: [`agentes/README.md`](../agentes/README.md) para templates de configuração de IA.
