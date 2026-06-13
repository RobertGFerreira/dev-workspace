# Codex - {{PROJECT_NAME}}

> Este é o Codex do projeto, definindo o contexto central, regras de desenvolvimento e diretrizes para os agentes de IA.

---

## 1. Visão Geral do Projeto

- **Nome:** {{PROJECT_NAME}}
- **Propósito:** {{DESCRICAO_DO_PROJETO}}
- **Stack:** {{PROJECT_STACK}}
- **Linguagem:** {{PROJECT_LANGUAGE}}

---

## 2. Regras de Desenvolvimento

### Convenções de Código
- Siga as boas práticas da linguagem {{PROJECT_LANGUAGE}} e os linters configurados.
- Use tipagem estática e evite tipos implícitos.
- Escreva testes unitários para novas funcionalidades.

### Commits e Versionamento
- Siga o padrão de commits do projeto (`COMMIT_STANDARD.md`).
- Faça commits atômicos e descritivos.

---

## 3. Estrutura de Pastas e Componentes

- `src/` ou `lib/` - Código-fonte principal.
- `tests/` - Suíte de testes.
- `docs/` - Documentação do projeto.
- `governance/` - Agentes, prompts e skills da governança.

---

## 4. Instruções para Agentes

- Leia sempre a documentação pertinente antes de alterar o código.
- Respeite os limites de escopo e não altere arquivos de governança sem permissão.
- Use marcadores de estado (`[INFERIDO]`, `[PENDENTE]`) em caso de dúvida.
- Se o projeto tiver o Conselho de Decisão ativo (`ENABLE_DECISION_COUNCIL=true`), acione `/conselho` para crítica multi-perspectiva antes de decisões técnicas relevantes, SDDs formais e definição de features complexas.
